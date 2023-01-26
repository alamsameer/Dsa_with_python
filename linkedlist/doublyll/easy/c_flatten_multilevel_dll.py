def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is not None :
            self.flatten_rec(head)
        return head
def flatten_rec(self,head:'Optional[Node]')->'Optional[Node]':
    curr,tail=head,head
    while curr :
        child=curr.child
        next=curr.next
        # if there is child we will use recursion 
        #  child will be new Head move until it is None
        if child:
            # we will get one level down linkedList
            _tail=self.flatten_rec(child)
            # and the next pointer will point to the current next 
            _tail.next=next
            # check if the next element exist then only point it's prev to current flattened linkedList otherwise do nothing
            if next != None:next.prev=_tail
            # now the next element will be the child 
            curr.next=child
            # and prev of child will be the current
            child.prev=curr
            # set the current child to be none
            curr.child=None
            curr=tail
        else:
            curr=curr.next
        if curr != None:tail=curr
    return tail