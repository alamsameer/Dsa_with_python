def searchMatrix(nums:list,target)-> int:
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