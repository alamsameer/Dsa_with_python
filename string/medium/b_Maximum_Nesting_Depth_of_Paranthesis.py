def maxDepth( s: str) -> int:
        if len(s) == 0 or ("(" not in s and ")" not in s):
            return 0
        stack=[]
        count=0
        res=0
        for i in s:
            if i == "(":
                stack.append(i)
                count+=1
                if count>res:
                    res+=1
            elif i == ")":
                count-=1
                stack.pop()
        print(res)
        return res
maxDepth("")
print('maxDepth(""): ', maxDepth(""))