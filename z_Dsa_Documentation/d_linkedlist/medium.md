### Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well

#### concept 
<img src="./images/WhatsApp Image 2022-10-19 at 7.20.01 PM.jpeg">

```python
 def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sential=ListNode(0,head)
        pred=sential
        while head:
            if head.next and head.val==head.next.val:
                # move head until it is true 
                while head.next and head.next.val==head.val:
                    head=head.next
                # after moving we will move our predecessor ahead of head node so that we can get a new elemenr
                pred.next=head.next
            else:
                # if false we will still inceas the predecessor
                pred=pred.next
            head=head.next
        return sential.next
```