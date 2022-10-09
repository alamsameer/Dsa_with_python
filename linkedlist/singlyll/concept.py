class Node():
    def __init__(self, data=None):
        self.data = data
        self.next = None


class linkedlist():
    def __init__(self, node=None):
        self.head = node

    def add_node_to_lst(self, x):
        newNode = Node(x)
        if self.head is None:
            self.head = newNode
            return self.head
        ptr = self.head
        while ptr.next != None:
            ptr = ptr.next
        ptr.next = newNode
        return self.head
    def deleteNode(self,x):
        ptr=self.head
        temp=None
        while ptr is not None:
            if ptr.data ==x:
                break
            temp=ptr # this is a node which store the previous node so that when we wnat to use our head node
            # after arriving at this point whatever will be the next node ,so to use that node 
            # print(temp.data,"temp")
            ptr=ptr.next
            # print(ptr.data,"ptr")
        if ptr is not None:
            temp.next=ptr.next # here we are cutting the link from the node which we want to delete and linking to the next of the node 
        else:
            print("node does not exist")
        ptr=None
        
    def traverse_linkedlist(self):
        ptr=self.head
        while ptr is not None:
            print(ptr.data)
            ptr=ptr.next


list1 = linkedlist()
list1.add_node_to_lst(5)
list1.add_node_to_lst(4)
list1.add_node_to_lst(3)
list1.add_node_to_lst(2)
list1.add_node_to_lst(1)
# list1.traverse_linkedlist()
print("new line")
list1.deleteNode(3)
list1.traverse_linkedlist()

