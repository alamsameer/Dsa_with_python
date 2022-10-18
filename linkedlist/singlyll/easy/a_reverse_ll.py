def reverseList( head):
       prev=None
       current=head
       while current is not None:
           temp=current.next
           current.next=prev
           prev=current
           current=temp
       return prev

#  optimal solution 
def isPalindrome(self, head) -> bool:
       slow, fast, prev = head, head, None
       while fast and fast.next:
           slow, fast = slow.next, fast.next.next
       prev, slow, prev.next = slow, slow.next, None
       while slow:
           slow.next, prev, slow = prev, slow, slow.next
       fast, slow = head, prev
       while slow:
           if fast.val != slow.val: return False
           fast, slow = fast.next, slow.next
       return True

#  approach is same as above but time limit is excceded 
# def isPalindrome(self, head: Optional[ListNode])->Optional[ListNode]:
#         if head == None or head.next == None:
#             return True
#         slow,fast=head,head
#         while fast.next and fast.next.next:
#             slow=slow.next
#             fast=fast.next.next
#         slow.next=self.reverseList(slow.next)
#         slow=slow.next
#         print(slow)
#         while slow:
#             if slow.val !=head.val:
#                 return False
#             slow=slow.next
#             head=head.next
#         return True

#     def reverseList(self, slow: Optional[ListNode])->Optional[ListNode]:
#         prev=None
#         current=slow
#         while current is not None:
#             temp=current.next
#             current.next=prev
#             prev=current
#             current=temp
#         return prev