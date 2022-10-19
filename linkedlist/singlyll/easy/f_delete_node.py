#  delete when only nod e is give 

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