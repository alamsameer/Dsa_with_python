def middleNode(self, head):
        count=0
        current=head
        # getting the length of the linked list 
        while current is not None:
            count+=1
            current=current.next
        mid=int(count/2)
        current=head
        # intializing the res variable so to store our result
        res=None
        # getting the node which is middle and that will store all the value after it 
        while mid>=0 and current is not None:
            if mid ==0:
                res=current
                break
            mid-=1
            current=current.next
        return res