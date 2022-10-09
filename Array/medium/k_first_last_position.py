# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

def searchRange( nums, target):
    def binarySearchLeft(A, x):
        left, right = 0, len(A) - 1
        while left <= right:
            mid = int((left + right) / 2)
        #    target is always greater than the  mid value for left serch
            if x > A[mid]: left = mid + 1
            else: right = mid - 1
            # In left Search we will return left 
        return left
    def binarySearchRight(A, x):
        left, right = 0, len(A) - 1
        while left <= right:
            mid =  int((left + right) / 2)
              #    target is always greater than and equal to the  mid value for left serch
            if x >= A[mid]: left = mid + 1
            else: right = mid - 1
        print(x ,mid,left,right,A[mid])
        #  # In right Search we will return right 
        return right
    left, right = binarySearchLeft(nums, target), binarySearchRight(nums, target)
    return (left, right) if left <= right else [-1, -1]
print('searchRange( [5,7,7,8,8,10],8): ', searchRange( [5,7,7,8,8,10],8))