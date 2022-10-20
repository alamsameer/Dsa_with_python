# my naive approach 
# get length of linked List
# if n from last then find what from start
# total_len-last
#  use while loop to dummy.next and nth>1
#  change dummy point and decrease  nth by one 
# then dummy.next=dummy.next.next

def removeNthFromEnd( head, n: int):
        if head.next == None:
            head=None
            return head
        count=0
        getlen=head
        # print(getlen)
        while getlen:
            count+=1
            getlen=getlen.next
        nth=count-n
        dummy=head
        if nth == 0:
            head=head.next
            return head
        while dummy.next and nth>1:
            nth-=1
            dummy=dummy.next
        print(dummy)
        dummy.next=dummy.next.next
        return head
            
#  better solution 
def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow,fast=head,head
        for i in range(n):
            fast=fast.next
        if not fast:
            return head.next
        while fast.next:
            slow=slow.next
            fast=fast.next
        slow.next=slow.next.next
        return head