def rotateString( s: str, goal: str) -> bool:
     if len(s)==1 and s==goal:
         return True
     for i in range(len(s)-1):
        # taking the first element of the string
         shift=s[0:1]
        # redifinig s after element first
         s=s[1:]
        #  shifting element by concatinating the removed elemenent
         s=s+shift
        #  checking the condition
         if s==goal:
             return True
     return False

# writing above solution in better way 

def rotateString( s: str, goal: str) -> bool:
     for i in range(len(s)):
         if s[i:]+s[0:i]==goal:
             return True
     return False

# one liner hurrah!!!

def rotateString( s: str, goal: str) -> bool:
    return len(s)==len(goal) and s in goal+goal