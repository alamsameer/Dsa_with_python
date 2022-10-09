# sol 1 brute force solution 

# def twoSum(self, nums: List[int], target: int) -> List[int]:
#         totalSum=0
#         start=0
#         last=0
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 if nums[i]+nums[j]==target:
#                     return [i,j]

# sol 2 optimal solution using hashmap *********** OPTIMAL *********

# from collections import defaultdict

# def twoSum( nums: list, target: int) -> list:
#         hash=defaultdict(lambda:0)
#         for i in range(len(nums)):
#             sub=target-nums[i]
#             if( sub in hash):
#                 return [hash[sub],i]
#             else:
#                 hash[nums[i]]=i