def isPalindrome(self, head) -> bool:
        curList=[]
        while head is not None:
            curList.append(head.val)
            head=head.next
        if curList == curList[::-1]:
            return True
        return False