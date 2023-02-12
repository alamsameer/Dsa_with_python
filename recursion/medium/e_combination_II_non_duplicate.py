
def combinationSum2( candidates: list[int], target: int) -> list[list[int]]:
    def backtrack(target,currcomb,ans,currindex):
        if target<0:
            return
        if target==0:
            ans.append(currcomb[:])
            return
        for i in range(currindex,len(candidates)):
            if i > currindex and candidates[i] == candidates[i-1]:
                continue
            currcomb.append(candidates[i])
            backtrack(target-candidates[i],currcomb,ans,i+1)
            currcomb.pop()
    candidates.sort()
    ans=[]
    currindex=0
    backtrack(target,[],ans,currindex)
    return ans

# ____explaiantion

# This function sorts the input candidates list in increasing order, then uses a backtracking approach to find all the unique combinations that sum up to the target.

# The backtrack function takes four arguments: start, target, path, and res. The start argument represents the starting index in the candidates list, target is the target sum, path is a list that keeps track of the current combination, and res is a list that stores the final result.

# The function first checks if the target is negative, and if it is, the function returns. If the target is equal to 0, it means that the current combination sums up to the target, so it adds the current path to the result list.

# The function then loops through the candidates list, starting from the start index. If the current index is greater than start and the current element is equal to the previous element, the function continues to the next iteration to avoid duplicate combinations.

# Finally, the function adds the current element to the path, makes a recursive call to backtrack with the updated target and path, then removes the last element from path to backtrack.