#  finding most consecutive 1 in an array of binary
def findMaxConsecutiveOnes( nums:list) -> int:
    count=0
    max=0
    for i in range(len(nums)):
        if nums[i] == 0:
            count=0
        else:
            count+=1
        if count>max:
            max+=1
    return max

print('findMaxConsecutiveOnes([1,1,0,1,1,1,0,1]): ', findMaxConsecutiveOnes([0,0,0,1,1,1,1,1,0,0,1,1,1,0]))
    
    