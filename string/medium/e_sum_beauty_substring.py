def beautySum(s:str)->int:
    beauty=0
    for i in range(len(s)-2):
        fre={}
        for j in range(i,len(s)):
            print(s[j])
            fre.setdefault(s[j],0)
            fre[s[j]]+=1
        beauty+=max(fre.values())-min(fre.values())
    return beauty

beautySum("aabcb")
print('beautySum("aabcb"): ', beautySum("aabcb"))