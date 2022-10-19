# Delete when only node value is give 
# The linked list is empty, i.e. the head node is None.
# Multiple nodes with the target value in a row.
# The head node has the target value.
# The head node, and any number of nodes immediately after it have the target value.
# All of the nodes have the target value.
# The last node has the target value.

def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
       
        dummy=ListNode(-1)
        dummy.next=head
        ptr=dummy
        while ptr.next is not None:
            print(dummy)
            print("----------------------")
            if ptr.next.val == val:
                ptr.next=ptr.next.next
            else:
                ptr=ptr.next
        return dummy.next