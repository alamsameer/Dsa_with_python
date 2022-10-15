



### Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.You may assume that each input would have exactly one solution, and you may not use the same element twice.You can return the answer in any order.

#### concept
In this question ,we can use hashmap concept to store the current value as key and its position as value,

then the main logic is to subtract the target to current value
and check if that as key in hash then we found the two sum otherwise not 

#### code 
```python
def twoSum( nums: list, target: int) -> list:
        hash=defaultdict(lambda:0)
        for i in range(len(nums)):
            sub=target-nums[i]
            if( sub in hash):
                return [hash[sub],i]
            else:
                hash[nums[i]]=i
```
<hr>


### # Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue. We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively. You must solve this problem without using the library's sort function.


#### concept
 sol  1  -  we can  sort the  value = 0,1,2 using  inbuilt method  sol 2 - or use any sorting algorithm
#### code 
```python
```
<hr>


### 

#### concept

#### code 
```python
# It can have multiple solution,some of which I have tried 

# solution 1  Brute force  O(n2)
def majorityElement(self, nums: List[int]) -> int:
        majority_count = len(nums)//2 # storing the majority element 
        for num in nums:
            count = sum(1 for elem in nums if elem == num)# counting the different number occurence of number 
            if count > majority_count:# compareing  every time coutn and majority_count and if it  is true then return true
                return num
# solution 2  using Hashmap
def majorityElement( nums:list) -> int:
    hashmap=defaultdict(lambda:0)
    uni=set(nums) # getting unique value 
    for i in uni:  # storing  number and its no.of occurence in dictionary
        tnum=nums.count(i)
        hashmap[i]=tnum
    for j in hashmap:
        if hashmap[j]>len(nums)/2:
            return j
# 3 solution 
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]
# optimal solution
   def majorityElement(self, nums: List[int]) -> int:
        curr, count = nums[0], 1                   # curr will store the current majority element, count will store the count of the majority
        for i in nums[1:]:
            count += (1 if curr == i else -1)      # if i is equal to current majority, they're in same team, hence added, else one current majority and i both will be dead
            if not count:                          # if count of current majority is zero, then change the majority element, and start its count from 1
                curr = i
                count = 1
        return curr


```
<hr>


### Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

#### concept
Kadane’s Algorithm — (Dynamic Programming)

 #### solution  1
 Brute Force Approach
One very obvious but not so good solution is to calculate the sum of every possible subarray and the maximum of those would be the solution. We can start from index 0 and calculate the sum of every possible subarray starting with the element A[0], as shown in the figure below. Then, we would calculate the sum of every possible subarray starting with A[1], A[2] and so on up to A[n-1], where n denotes the size of the array (n = 9 in our case). Note that every single element is a subarray itself.
#### code 
```python
#kadane algorithm 
def maxSubArray(self, nums: List[int]) -> int:
        lmax=0
        gmax=float("-inf")
        for i in range(len(nums)):
            lmax=max(nums[i],nums[i]+lmax)
            if gmax<lmax:
                gmax=lmax
        return gmax
```
<hr>


### You are given an array prices where prices[i] is the price of a given stock on the ith day.You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

#### concept
 Normal comaprision
#### code 
```python
def maxProfit(prices:list)->int:
    buy=prices[0] # assumed that buy price is first elemnet
    profit=0 # profit will be Zero
    for i in range(prices):
        if buy>prices[i]: # comparing current price and  what was buy price  if earlier was larger than we will change our buy price to current ,so that profit can be maximized 
            buy=prices[i]
        elif prices[i]-buy>profit: # comparing earlier profit ot current profit 
            profit=prices[i]-buy
    return profit
```
<hr>


### 	Rearrange the array in alternating positive and negative items

#### concept

#### code 
```python
 
 # a kind of brute  force approach with non constant space complexity 

 def rearrangeArray(self, nums:list) -> list:
        positiveNum=[]
        negativeNum=[]
        result =[]
        for i in nums:
            if i<0:
                negativeNum.append(i)
            else:
                positiveNum.append(i)
        for i in range(len(nums)):
            x=i%2
            if( x !=0):
                n=negativeNum.pop(0)
                result.append(n)
            else:
                p=positiveNum.pop(0)
                result.append(p)
        return result
# _____OPTIMAL SOLUTION 

def rearrangeArray(self, nums:list) -> list:
    # POINTER FOR  positive value 
     a=0
    #  pointer for negative Value 
     b=1
    #  intializing new array where the desired result can be stored
     arranged=[0]*len(nums)
     for i in nums:
         if(i>0):# checking for value is positve 
            # storing value at a position which is always even
             arranged[a]=i
            #  incrementing the value  by 2 for next positvevalue to be stored 
             a+=2
         else:
            # storing value at a position which is always odd
             arranged[b]=i
              #  incrementing the value  by 2 for next negative value to be stored
             b+=2
     return arranged

```
<hr>


###  longest consecutive sequence 

#### concept
- sort the number 
- then loop through the list 
- and increase only when consecutive nuber are not same 
- Increase curr streak if it is equal  to prev +1
- when it is not then set the value of longest streak
- Return the longest Streak
#### code 
```python
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
```
<hr>


### 

#### concept

#### code 
```python
```
<hr>


### 

#### concept

#### code 
```python
```
<hr>


### 

#### concept

#### code 
```python
```
<hr>


### 

#### concept

#### code 
```python
```
<hr>


### 

#### concept

#### code 
```python
```
<hr>


### 

#### concept

#### code 
```python
```
<hr>