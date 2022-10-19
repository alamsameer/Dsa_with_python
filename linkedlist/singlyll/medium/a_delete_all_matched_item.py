def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
       sential=ListNode(0,head)
       # sential.next=head
       pred=sential
       while head:
           if head.next and head.val==head.next.val:
               while head.next and head.next.val==head.val:
                   head=head.next
               pred.next=head.next
           else:
               pred=pred.next
           head=head.next
       return sential.next