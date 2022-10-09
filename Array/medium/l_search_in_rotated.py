# There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.



# def search(nums: list, target: int) -> int:
#         def searchPivot(nums):
#             if len(nums)==1:
#                 return 0
#             for i in range(len(nums)):
#                 if nums[i-1]>nums[i]:
#                     return i
#             return 0
#         def rightSearch(nums,target,pivot):
#             left=pivot
#             right=len(nums)-1
#             print("right search",left,right)
#             while left<=right:
#                 mid=int((left+right)/2)
#                 if(nums[mid]==target):
#                     return mid
#                 if(nums[mid]<target):
#                     left=mid+1
#                 else:
#                     right=mid-1
#             return -1   
#         def leftSearch(nums,target,pivot):
#             left=0
#             right=pivot
#             while left<=right:
#                 mid=int((left+right)/2)
#                 if(nums[mid]==target):
#                     return mid
#                 if(nums[mid]<target):
#                     left=mid+1
#                 else:
#                     right=mid-1
#             return -1
#         pivot=searchPivot(nums)
#         print(' pivot: ',  pivot)
#         leftnum=leftSearch(nums,target,pivot)
#         print('leftnum: ', leftnum)
#         rightnum=rightSearch(nums,target,pivot)
#         print('rightnum: ', rightnum)
#         if(leftnum<0 and rightnum<0):
#             return -1
#         elif leftnum<0:
#             return rightnum
#         else:
#             return leftnum
# search([1,3],3)

# BIG OF O(K- PIVOT ELEMENT )

# optimized solution
def search(nums:list,target:int)->int:
    left=0
    right=len(nums)-1
    while left<=right:
        mid=int((left+right)/2)
        if (nums[mid]==target):
            return mid
        # pivot concept used -start 
        if nums[left]<nums[mid]:
            if nums[left]<=target<=nums[mid]:
                right=mid-1
            else:
                left=mid+1
        else:
            if nums[mid]<=target<=nums[right]:
                left=mid+1
            else:
                right=mid-1
        # pivot concept used -end
    return -1