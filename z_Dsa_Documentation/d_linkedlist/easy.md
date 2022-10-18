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