from a_Node import Node

class doublyll():
    def __init__(self) -> None:
        self.head=None
        self.length=0
    def addHead(self,val):
        newNode=Node(val)
        newNode.next=self.head
        self.head=newNode
        self.length+=1
        # self.traversal()
        pass
    def addTail(self,val):
        newNode=Node(val)
        if not self.head:
            self.length+=1
            self.head=newNode
            return 
        temp=self.head
        while temp.next:
            temp=temp.next
        self.length+=1
        temp.next=newNode
        newNode.prev=temp
        return 

    def addToIndex(self,index,val):
        newNode=Node(val)
        temp=self.head
        for i in range(index-1):
            temp=temp.next
        self.length+=1
        newNode.next=temp.next
        temp.next=newNode
        newNode.prev=temp
        return 
    def deleteVal(self,index):
        pass
    def traversal(self):
        temp=self.head
        print(temp)
        while temp != None:
            print(temp.val)
            temp=temp.next
        pass
firstDbl=doublyll()


firstDbl.addTail(0)
firstDbl.addTail(1)
firstDbl.addToIndex(1,"i am at index 1")
firstDbl.traversal()