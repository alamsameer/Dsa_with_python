# You are given the head of a linked list, and an integer k.
# Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).

def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
#         convert head into array
#         swap two element 
#         then rebuild head
        array=[]
        while head:
            array.append(head.val)
            head=head.next
        print("before swap",array)
        array[k-1],array[-k]=array[-k],array[k-1]
        print("after swap",array)
        head=ListNode(array[0])
        temp=head
        for i in range(1,len(array)):
            dummy=ListNode(array[i])
            temp.next=dummy
            temp=temp.next
        # print(head)
        return head

# 2nd sol 

def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
#         next approach is two pointer 
#  intialized left pointer
        left=head
        #  intialized right pointer
        right=head
         #  intialized curr pointer to move forward
        curr=head
        counter=1
        while curr:
            # when counter is less than k will move left
            if (counter<k):
                left=left.next
            # when counter is greater  than k will move right
            if (counter>k):
                right=right.next
            curr=curr.next
            counter+=1
        temp=left.val
        # swaping the value 
        left.val=right.val
        right.val=temp
        return head