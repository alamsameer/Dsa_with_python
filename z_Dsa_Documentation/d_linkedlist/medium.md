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

### Design the Linked List :

```python
class Node(object):

    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = 0

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= self.size:
            return -1

        if self.head is None:
            return -1

        curr = self.head
        for i in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list.
        After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        node = Node(val)
        node.next = self.head
        self.head = node

        self.size += 1

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        curr = self.head
        if curr is None:
            self.head = Node(val)
        else:
            while curr.next is not None:
                curr = curr.next
            curr.next = Node(val)

        self.size += 1

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list.
        If index equals to the length of linked list, the node will be appended to the end of linked list.
        If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        if index < 0 or index > self.size:
            return

        if index == 0:
            self.addAtHead(val)
        else:
            curr = self.head
            for i in range(index - 1):
                curr = curr.next
            node = Node(val)
            node.next = curr.next
            curr.next = node

            self.size += 1

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        if index < 0 or index >= self.size:
            return

        curr = self.head
        if index == 0:
            self.head = curr.next
        else:
            for i in range(index - 1):
                curr = curr.next
            curr.next = curr.next.next

        self.size -= 1

```

### You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

### concept
 using floyd two pointer approach

```python
def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
    # dealing with the edge case when only one element is there
        if head.next==None:
            return None
    #  intialized two pointer where slow start from position first and fast point start from 3rd element
        slow,fast=head,head.next.next
        # moving slow pointer by 1 step and fast pointer by 2 step 
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        # now when fast pointer have reached to last then slow pointer is 1 step behind middle and we need to delete it so our next pointer will point the next node of the middle 
        slow.next=slow.next.next
        return head
```

### Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

<hr>
 
### Given the head of a linked list, remove the nth node from the end of the list and return its head.

### concept
Naive approach 
- get length of linked List
- if n from last then find what from start
- total_len-last
-  use while loop to dummy.next and nth>1
-  change dummy point and decrease  nth by one 
- then dummy.next=dummy.next.next

```python
def removeNthFromEnd( head, n: int):
        if head.next == None:
            head=None
            return head
        count=0
        getlen=head
        # print(getlen)
        while getlen:
            count+=1
            getlen=getlen.next
        nth=count-n
        dummy=head
        if nth == 0:
            head=head.next
            return head
        while dummy.next and nth>1:
            nth-=1
            dummy=dummy.next
        print(dummy)
        dummy.next=dummy.next.next
        return head
```
### better approach to above problem
### concept 
- what happen is this that move fast pointer by one for n time ,
- after that then move slow pointer until fast.next is None, 
then at that time slower pointer i one step behind the element to be deleted  
-  after we just shange the next pointer to next of next to get desired result  
```python
def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow,fast=head,head
        for i in range(n):
            fast=fast.next
        if not fast:
            return head.next
        while fast.next:
            slow=slow.next
            fast=fast.next
        slow.next=slow.next.next
        return head
```