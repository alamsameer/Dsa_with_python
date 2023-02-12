def subsets(nums:list[int])->list[list[int]]:
    count=0
    def backtrack(start,path):
        nonlocal count
        res.append(path)
        count+=1
        print(count)
        # print('parent ',path)
        for i in range(start,len(nums)):
            # print('for',i,path)
            backtrack(i+1,path+[nums[i]])
    res=[]
    backtrack(0,[])
    return res

print(subsets([1,2,3]))



