## Reverse LinkedList
<img src="images\reverse ll.gif"/>


```python
def reverseList( head):
       prev=None
       current=head
       while current is not None:
           temp=current.next #locally storing the next node of the current node 
           current.next=prev # assinging  the current's next node to be previous
           prev=current # now we are previous value as current value
           current=temp # reassining the locally next stored value as current so that we can go to next value
       return prev
```

## Delete Node of Likedlist 
```python
def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
#         assuming that the given node is to be deleted 
#        storing the next value of a node that has to be deleted 
        nextNode=node.next
#     assinging the current node's val to its next value
        node.val=nextNode.val
#     storing the next value of current.next.next
        node.next=nextNode.next
#     removing the next link of the current link 
        nextNode.next=None
#     after the work has done for the nextNode ,now it has to be deleted
        del(nextNode)
```

## Detect Cycle in Linked List 

### Approach 
 - Hashset
 - floyd cycle Detection Algorithm 
    This Approach uses two pointer  one is fast and other is slow , fast will two node at time and slow will move at one node at a time 
    and according to this algorithm ,these two point meet at some point if there is cycle in the linkedlist 
   - space complexity is constant

## python code 

```python
# logic code 
    if not head:
        return False
    slow =head
    fast=head.next
    while slow !=fast:
        if fast is None or fast.next is None :
            return False
        slow=slow.next
        fast=fast.next.next
    return True
```
   