def searchInsert(self, nums: list, target: int) -> int:
        left=0
        right=len(nums)-1
        # condition to check that left should not be grater than right if it is so 
        # it means the element does not exist 
        while left<=right:
            # every time  resetting mid where we can look that if element exist or not 
            mid=int((left+right)/2)
            # if element found then return the element
            if nums[mid]==target:
                return mid
            if nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return left
            