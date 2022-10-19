
class Node:
    def __init__(self,val,nextN=None) -> None:
        self.val=val
        self.next=nextN

class MyLinkedList:
    def __init__(self):
        self.head=None

    def get(self, index: int) -> int:
        if index<0:
            return -1
        dummy=head
        count=0
        while dummy.next != None:
            if index>count:
                return -1
            if index ==count:
                return dummy.val
            count+=1
            dummy=dummy.next
        return -1
        
        

    def addAtHead(self, val: int) -> None:
        newNode=Node(val)
        newNode.next=self.head
        self.head=newNode
        return self.head

    def addAtTail(self, val: int) -> None:
        addTail=Node(val)
        getTail=self.head
        while getTail.next:
            getTail=getTail.next
        getTail.next=addTail
        return 
        

    def addAtIndex(self, index: int, val: int) -> None:
        newNode=Node(val)
        count=0
        dhead=self.head
        while dhead:
            if count==index:
                temp=dhead.next
                dhead.next=newNode
                dhead.next=temp
                break
            count+=1
        return 
        

    def deleteAtIndex(self, index: int) -> None:
        


# Your MyLinkedList object will be instantiated and called as such:
obj=MyLinkedList()
param_1 = obj.get(index)
print(param_1)
obj.addAtHead(val)
obj.addAtTail(val)
obj.addAtIndex(index,val)
obj.deleteAtIndex(index)