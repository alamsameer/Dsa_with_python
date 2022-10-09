def solve(A:str)->str:
    hashmap={}
    result=""
    for i in A:
        if i not in hashmap.keys():
            hashmap[i]=A.count(i)
    for i in hashmap.keys():
        result+=i+str(hashmap[i])
    print(result)
    return result
    
solve("abbhuabcfghh")