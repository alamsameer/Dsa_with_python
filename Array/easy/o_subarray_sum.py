# sol 1 not efficient

# def subarraySum(nums:list ,k: int) -> int:
#     result=[[]]
#     count=0
#     for i in range(len(nums)+1):
#         for j in range(i):
#             result.append(nums[j:i])
#     print(result)
#     for i in result:
#         print(sum(i))
#         if sum(i) == k:
#             count+=1
#     return count

# subarraySum([1,1,1],2)
# print('subarraySum([1,1,1],2): ', subarraySum([1,1,1],2))

# sol 2 
from collections import defaultdict
def subarraySum( nums: list, k: int) -> int:
    count=0
    totalSum=0
    sumobj=defaultdict(lambda : 0)
    for i in range(len(nums)):
        totalSum+=nums[i]
        if totalSum == k:
            count+=1
        if totalSum-k in sumobj:
            count+=sumobj[totalSum-k]
        sumobj[totalSum]+=1
    print(sumobj)
    return count

print('subarraySum([1,1,1],2): ', subarraySum([1,0, 0,1,1,1],1))
 
#  in this subarray problem hashmap is used to 
# decrease its time complexity