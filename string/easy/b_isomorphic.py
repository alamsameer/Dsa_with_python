def isIsomorphic(strg1:str,strg2:str)->bool:
    map1=[]
    map2=[]
    for i in strg1:
        map1.append(strg1.index(i))
    for j in strg2:
        map2.append(strg2.index(j))
    # print(map1,map2)
    if map1 ==map2:
        return True
    
    return False
isIsomorphic("kegg","ladd")
print('isIsomorphic("kegg","ladd"): ', isIsomorphic("kegg","ladd"))
isIsomorphic("foo","bar")
print('isIsomorphic("foo","bar"): ', isIsomorphic("foo","bar"))