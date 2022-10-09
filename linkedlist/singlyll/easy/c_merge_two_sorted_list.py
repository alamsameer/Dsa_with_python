import a_a_node
ListNode=a_a_node.Node
def mergeTwoLists(list1,list2):
       # dummy node 
           curr=dumpy=ListNode()
           while list1 and list2:
               if list1.val<=list2.val:
                   dumpy.next=list1
                   list1=list1.next
               else:
                   dumpy.next=list2
                   list2=list2.next
               dumpy=dumpy.next
           dumpy.next=list1 or list2
           return curr.next