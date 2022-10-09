# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

# sol1

# def singleNumber(nums)->int:
#     for i in nums:
#         countnum=nums.count(i)
#         print(countnum)
#     return 0
# print('singleNumber([2,2,1]): ', singleNumber([2,2,1,3,3]))

# exact solution

# def singleNumber(self, nums: List[int]) -> int:
#     return 2*sum(set(nums))-sum(nums)
    