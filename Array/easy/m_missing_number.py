# find the missing number from the  array of range 0 -n in which one is missing 

# sol 1
# def missingNumber( nums:list) -> int:
#     for i in range(len(nums)+1):
#         if i not in nums:
#             return i

# print('missingNumber([3,0,1]): ', missingNumber([3,0,1]))

# sol 2 
def missingNumber(nums:list):
    n=len(nums)
    print('n: ', n)
    totalSum=(n*(n+1))/2
    print('totalSum: ', totalSum)
    arrSum=sum(nums)
    print('arrSum: ', arrSum)
    return int(totalSum-arrSum)
print('missingNumber([3,0,1]): ', missingNumber([3,0,1]))