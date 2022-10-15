# def moveZeroes( nums:list):
#      """
#      Do not return anything, modify nums in-place instead.
#      """
#      for i in range(len(nums)):
#         k=0
#         while k<=0:
#             k=0
#             if nums[i] == 0:
#                 x=nums.pop(i)
#                 nums.append(x)
#             else:
#                 k=1
#      return nums

def moveZeroes(arr):
    #  sol 1
    # return arr.sort(key=bool ,reverse=True)
    # sol 2

    j=0 # to track zero
    for i in range(len(arr)):
        if arr[i] != 0:
            print("Before",arr)
            arr[i],arr[j]=arr[j],arr[i]
            print("after",arr)
            j+=1
    return arr
print('moveZeroes([0,1,34,0,5]): ', moveZeroes([1,34,0,5]))