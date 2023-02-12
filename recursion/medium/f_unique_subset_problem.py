def subspunique(nums: list) -> list[list]:
    # The backtrack function takes two arguments: start ,path:
    # The start argument represents the starting index in the nums list
    # path path is a list that keeps track of the current subset.
    def backtrack(start, path):
        # The function first adds the current path to the result list res.
        res.append(path)
        # The function then loops through the nums list, starting from the start index.
        for i in range(start, len(nums)):
            # If the current index is greater than start and the current element is equal to the previous element, the function continues to the next iteration to avoid duplicate subsets.
            if i > start and nums[i] == nums[i-1]:
                continue
            # Finally, the function adds the current element to the path,
            path.append(nums[i])
            # makes a recursive call to backtrack with the updated path
            backtrack(i+1, path)
            path.pop()  # removes the last element from path to backtrack.
    # This function sorts the input nums list in increasing order, then uses a backtracking approach to generate all the unique subsets.
    nums.sort()
    res = []
    backtrack(0, [])
    return res
