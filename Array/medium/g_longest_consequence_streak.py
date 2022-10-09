
# brute force Solution

def longestSequence(nums:list)->list:
    longestStreak=0
    for i in nums:
        currnum=i
        currstreak=1
        while currnum+1 in nums:
            currstreak+=1
            currnum+=1
        longestStreak=max(currstreak,longestStreak)
    return longestStreak
print('longestSequence([100,4,200,1,3,2]): ', longestSequence([100,4,200,1,3,2]))


# optimal solution 

def longestConsecutive(self, nums: list ) -> int:
    #  checking if nums list is empty or not 
        if not nums:
            print(not nums)
            return 0
        # intializing the variable to store the longest and current streak 
        longestStreak=1
        currstreak=1
        sortnums=sorted(nums)
        for i in range(len(sortnums)):
            if sortnums[i] !=sortnums[i-1]:
                if sortnums[i]==sortnums[i-1]+1:
                    currstreak+=1
                else:
                    longestStreak=max(currstreak,longestStreak)
                    currstreak=1

        print((currstreak,longestStreak))
        # returing the maximum value of current and longest streak 
        return max(currstreak,longestStreak)