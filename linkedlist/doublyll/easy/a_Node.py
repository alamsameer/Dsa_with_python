class Node :
    def __init__(self,val,prev=None,Next=None) -> None:
        self.val=val
        self.prev=prev
        self.next=Next
    def getPrev(self):
        print(self.prev)
    def getVal(self):
        print(self.val)