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