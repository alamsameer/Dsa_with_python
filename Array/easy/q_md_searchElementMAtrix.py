
# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.

# sol 1 is brute force solution

# def searchMatrix(nums:list,target)-> int:
#     # define  varibles to track row and column where we will get our ans
#     # first for loop is for  row 
#     #  second for loop is to look into the current row 
#     row=0
#     col=0
#     for i in range(len(nums)):
#         row =i
#         for j in range(len(nums[i])):
#             col=j
#             if nums[row][col]==target:
#                 return True
#     return False


# print('searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],23): ', searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],23))

# optimal solution for search in matrix

# optimal solution i have thought is  to  look every element row 
# if the element is greater than the our element then  our row will be row -1
# in that row we can use binary search 

# def binarySearch(nums:list,target)->int:
#     left=0
#     right=len(nums)-1
#     while left<right:
#         mid=int((left+right)/2)
#         print(nums[mid])
#         if nums[mid]== target:
#             return True
#         if nums[mid]<target:
#             left=mid+1
#         else:
#             right=mid
    # return False
# binarySearch([0,1,2,3,4,5,6],7)
# print('binarySearch([0,1,2,3,4,5,6],5): ', binarySearch([0,1,2,3,4,5,6],input()))

# *******close to optimal ***********

# def searchMatrix(nums:list,target)-> int:
#     row =0
#     for i in range(len(nums)):
#         row=i
#         last=len(nums[row])-1
#         if nums[row][0] == target or nums[row][last]==target:
#             return True
#         if nums[row][0]> target:
#             row=row-1
#             break
#         if nums[row][last]>target:
#             row=row
#             break
#     x=binarySearch(nums[row],target)
#     return x

# print('searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],23): ', searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],10))

# solution 3 Binary Search in matrix ******************optimal************
# matrix of size of n(row)*m(column)
# a[x]=matrix[x/m][x%m]``

# def searchMatrix(matrix:list,target:int)->bool:
#     n=len(matrix)
#     m=len(matrix[0])
#     left=0
#     right=n*m-1
#     while left<right:
#         mid=(left+right)/2
#         midValue=matrix[int(mid/m)][int(mid%m)] 
#         if(midValue== target):
#             return True
#         if(midValue<target):
#             left=mid+1
#         else:
#             right=mid
#     return False

# print('searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],23): ', searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],10))
