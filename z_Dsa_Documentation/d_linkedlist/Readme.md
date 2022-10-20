[Go to ](#easy-problems-ac-leetcode-☺️😎)
[Go to ](#medium-level)
# Easy problems a/c leetcode ☺️😎
## Reverse LinkedList 
<img src=".\images\reverse ll.gif"/>

### concept 
what we did in this problem ,is intitalized  two global variable to track current node  and previous node  
```python
def reverseList( head):
       prev=None
       current=head
       while current is not None:
           nextNode=current.next #locally storing the next node of the current node 
           current.next=prev # assinging  the current's next node to be previous
           prev=current # now we are previous value as current value
           current=nextNode # reassining the locally next stored value as current so that we can go to next value
       return prev
```

## Delete Node of Likedlist 
### concept 
Basically what happen here is that ,the node which we want to delete is re initialized to its next value properties
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
    # in this loop we are checking ,if slow or both can meet at some point then we will break out of the loop and will return true (ie: it is cyclic)
    while slow !=fast:
        # at this point we are checking the fast and its next node ,if somewhere either of the value is none then we got to know that it is not cyclic therefore we  will return false 
        if fast is None or fast.next is None :
            return False
        # setting slow pointer one step ahead
        slow=slow.next
        # setting fast pointer two step ahead
        fast=fast.next.next

    return True
```
## finding the middle node in linkedlist

#### my approach 
```python
def middleNode(self, head):
        count=0
        current=head
        # getting the length of the linked list 
        while current is not None:
            count+=1
            current=current.next
        mid=int(count/2)
        current=head
        # intializing the res variable so to store our result
        res=None
        # getting the node which is middle and that will store all the value after it 
        while mid>=0 and current is not None:
            if mid ==0:
                res=current
                break
            mid-=1
            current=current.next
        return res
```
## this can be done using floyd two pointer approach

```python

```
## Delete node when the value is given inspite the actual node 

### concept
- The linked list is empty, i.e. the head node is None.
- Multiple nodes with the target value in a row.
- The head node has the target value.
- The head node, and any number of nodes immediately after it have the target value.
- All of the nodes have the target value.
- The last node has the target value.

 <b>when a new variable is defied and if you refer to head ,it means it is reffering to the actual address of the head if you change to this variable head is also change </b>
 
```python
def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
    #    creating a dummy node that so to work from first element ,if it matches
        dummy=ListNode(-1)
        # here we are referencing the head value to next of the dummy to have all the linked node 
        dummy.next=headnow 
        #this time  another varialble is defined to store the dummy address to work on it inspite working directly on the head
        
        ptr=dummy
        # exiting condition 
        while ptr.next is not None:
            # it the value of one step ahead node value matche so  we can point to next of next
            if ptr.next.val == val:
                ptr.next=ptr.next.next
            #otherwise we are moving foreward to look into this 
            else:
                ptr=ptr.next
        return dummy.next
```
### palindrome cheaker in linkedList 
### concept 
using floyd two pointer algorithm 
- find middle 
- reverse right half ,slow = slow.next
- compare head and slow 
- if all are equal then return true otherwise False 
```python
def isPalindrome(self, head: Optional[ListNode])->Optional[ListNode]:
        if head == None or head.next == None:
            return True
        slow,fast=head,head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        slow.next=self.reverseList(slow.next)
        slow=slow.next
        print(slow)
        while slow:
            if slow.val !=head.val:
                return False
            slow=slow.next
            head=head.next
        return True

    def reverseList(self, slow: Optional[ListNode])->Optional[ListNode]:
        prev=None
        current=slow
        while current is not None:
            temp=current.next
            current.next=prev
            prev=current
            current=temp
        return prev
```

# Medium level

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
