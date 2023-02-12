def combinationSum( candidates: list[int], target: int) -> list[list[int]]:
    def backtrack(currsum,currcomb,ans,currindex):
        if currsum >target: # backtrack from here
            return
        if currsum==target: # when our condition satisfy backtrack
            ans.append(currcomb[:])
            return 
        for i in range(currindex,len(candidates)): # trying all possible combination
            currcomb.append(candidates[i])
            currsum+=candidates[i]
            backtrack(currsum,currcomb,ans,i)
            currcomb.pop()
            currsum-=candidates[i]
    ans=[]
    currindex=0
    backtrack(0,[],ans,currindex)
    return ans
print('ans',combinationSum([2,3,5],8))

# -------- second way

def combinationSum(candidates: list[int], target: int) -> list[list[int]]:
    def backtrack(start, currsum, path):
        if currsum == target:
            ans.append(path)
            return
        for i in range(start, len(candidates)):
            if currsum + candidates[i] > target:
                continue
            backtrack(i, currsum + candidates[i], path + [candidates[i]])
    ans = []
    backtrack(0, 0, [])
    return ans

print(combinationSum([2,3,5], 8))

