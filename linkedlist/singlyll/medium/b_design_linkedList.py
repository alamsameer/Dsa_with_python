# class Node:
#     def __init__(self,val,nextN=None) -> None:
#         self.val=val
#         self.next=nextN

# class MyLinkedList:
#     def __init__(self):
#         self.head=None
#         self.size=0

#     def get(self, index: int) -> int:
#         if (self.size+1)<index or index<0:
#             return -1
#         dummy=self.head
#         count=0
#         while dummy.next != None:
#             if index-1 ==count:
#                 return dummy.val
#             count+=1
#             dummy=dummy.next
#         return -1
        
        

#     def addAtHead(self, val: int) -> None:
#         newNode=Node(val)
#         newNode.next=self.head
#         self.head=newNode
#         self.size+=1
#         return self.head

#     def addAtTail(self, val: int) -> None:
#         addTail=Node(val)
#         getTail=self.head
#         while getTail.next:
#             getTail=getTail.next
#         getTail.next=addTail
#         return 
        

#     def addAtIndex(self, index: int, val: int) -> None:
#         if (self.size+1)<index or index<0:
#             print("item can't be added here ,use valid index between 0 and"+str(self.size+1))
#             return 
#         newNode=Node(val)
#         count=0
#         dhead=self.head
        
#         while dhead:
#             print(count)
#             if count==index-1:
#                 # print('count==index-1: ', count==index-1)
#                 # print(count,index-1)
#                 temp=dhead.next
#                 dhead.next=newNode
#                 dhead.next.next=temp
#                 dhead=dhead.next
#                 self.size+=1
#                 break
#             dhead=dhead.next
#             count+=1
#         return 
        

#     # def deleteAtIndex(self, index: int) -> None:
#     def traverse(self):
#         getall=self.head
#         while getall:
#             print(getall.val)
#             getall=getall.next
        


# # Your MyLinkedList object will be instantiated and called as such:

# obj=MyLinkedList()
# obj.addAtHead(4)
# obj.addAtHead(3)
# obj.addAtHead(2)
# obj.addAtHead(1)
# obj.addAtHead(0)
# obj.traverse()
# param_1=obj.get(2)
# print('param_1: ', param_1)
# param_2=obj.get(4)
# print('param_2: ', param_2)



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