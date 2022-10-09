# Sort Characters By Frequency
from collections import defaultdict

def sortdictvalue(d):
    res=sorted(d.items(),key=lambda x:x[1],reverse=True)
    return res


def frequencySort( s: str) -> str:
    result=defaultdict(lambda:"not present")
    freres=''
    for i in s:
        if i in result:
            count=result[i]
            result[i]=count+1
        else:
            result[i]=1
    sortedDict=sortdictvalue(result)
    for i in sortedDict:
        freres+=i[0]*i[1]
    return freres
    


print('frequencySort("eertttgg"): ', frequencySort("eertttgg"))

