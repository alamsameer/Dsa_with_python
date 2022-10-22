def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        curr=head
        length=1
        while curr.next:
            curr=curr.next
            length+=1
#       connecting to head
        curr.next=head
        k=length-(k%length)
        while k>0:
            curr=curr.next
            k-=1
        newHead=curr.next
        curr.next=None
        return newHead