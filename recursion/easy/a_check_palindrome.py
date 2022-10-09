class Solution:
    def isPalindrome(self, s: str) -> bool:
             
        s="".join(filter(str.isalnum,s)).lower()
        if len(s)<2:
            return True 
        if s[0]!=s[-1]:
            return False
        return self.isPalindrome(s[1:-1])

x=Solution()

print('x.isPalindrome( "A man, a plan, a canal: Panama"): ', x.isPalindrome( "A man, a plan, a canal: Panama"))
print('x.isPalindrome( "race a car"): ', x.isPalindrome( "race e car"))