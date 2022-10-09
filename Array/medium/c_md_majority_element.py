
# sol 1 it's BigO  is  O(M+N)

# from collections import defaultdict
# def majorityElement( nums:list) -> int:
#     hashmap=defaultdict(lambda:0)
#     uni=set(nums)
#     for i in uni:
#         tnum=nums.count(i)
#         hashmap[i]=tnum
#     max=0
#     print(hashmap)
#     for j in hashmap:
#         print(hashmap[j])
#         if hashmap[j]>len(nums)/2:
#             return j

# print('majorityElement([3,2,3]): ', majorityElement([3,2,3]))

# optimal solution is using binary Search tree 

# https://www.geeksforgeeks.org/majority-element/#:~:text=The%20basic%20solution%20is%20to,majority%20element%20doesn't%20exist.


# need to think how this will work 

#    def majorityElement(self, nums: List[int]) -> int:
#         curr, count = nums[0], 1                   # curr will store the current majority element, count will store the count of the majority
#         for i in nums[1:]:
#             count += (1 if curr == i else -1)      # if i is equal to current majority, they're in same team, hence added, else one current majority and i both will be dead
#             if not count:                          # if count of current majority is zero, then change the majority element, and start its count from 1
#                 curr = i
#                 count = 1
#         return curr