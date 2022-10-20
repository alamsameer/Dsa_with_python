### [Go to easy](#easy-level-problem)
### [Go to medium](#medium-level)

# Easy level problem

### Check_if_Array_Is_Sorted_and_Rotated

#### concept:
 
 In this solution ,The approach is to compare every current element to it's last element so that every current element is larger than pervious one but at one place the current element is smaller than pervious element where the roation has happened ,and the last element is always less than first element

####  python code 
```python
from typing import List 
import sys
def check( nums: List[int]) -> bool:
    count = 0
    length = len(nums) - 1
    for i in range(length):
        if nums[i] > nums[i + 1]:
            print(nums[i] , nums[i + 1])
            count+=1
            print(' count: ',  count)

    print(count)
    if count > 1 or (count == 1 and nums[0] < nums[length]):
        return False
    
    return True

y=check([4,5,6,1,2,3])
print(y)
```

<hr>

### Reverse Integers 

#### concept:
- first step is to check whether element is positive or negative 

- mathematical concept is  used to get last digit of the number  which is to get remainder by dividing by 10 and that digit can be stored in list 

- The loop is used for them element of the list ,which is multiplied by their power of 10 to its position
- added all the number to form the number 
- in last is returned
####  python code 

```python
def reverse(x:int)->int:
    sys=0
    if(x>0):
        sys=1
    else:
        sys=-1
    newX=abs(x)
    digitList=[]
    while newX:
        digitList.append(newX%10)
        newX=newX//10
    reversedNum=0
    digitLen=len(digitList)
    for i in range(digitLen):
        reversedNum+=digitList[digitLen-1-i]* pow(10,i)
    res=sys*reversedNum
    if res > (pow(2, 31) - 1) or res < -(pow(2,31)): # here number is checked that it should not cross the limit 
        return 0
    return res

```

<hr>


### find the lcm 

#### concept:
- mathematical concept is  used to get lcm (a*b=lcm *hcf)
####  python code 

```python
from d_hcf import find_gcd
def lcmAndGcd( A , B):
     # code here 
    gcd=find_gcd(A,B)
    lcm=int(A*B/gcd)
    sol=[lcm,gcd]
    return sol
print(lcmAndGcd(5,6))
```


<hr>

### check armstrongNumber 

#### concept:
armstrong number are thos number which is when sum of  the cube of its digit is equal to the number 

####  python code 

```python
def armstrongNumber (ob, n):
     # code here 
     string_num=str(n)
     sum=pow(int(string_num[0]),3)+pow(int(string_num[1]),3)+pow(int(string_num[2]),3)
     if(sum!=n):
         return "No"
     return "Yes"
```


<hr>

### find the cubic sum of n number 

#### concept:
- Mathematical formula is used 
####  python code 

```python
def sumOfSeries(n):
    x = (n * (n + 1)  / 2)
    return (int)(x * x)

print(sumOfSeries(5))
```


<hr>

### find nth fibonacci number  

#### concept:
- Recursion is used -Add the fib(num-2)+fib(n-1)
####  python code 

```python
def fib(n: int) -> int:
    if n ==0 or n==1:
        return n
    return fib(n-1)+fib(n-2)
```


<hr>

### left Rotate the number 

#### concept:
- If the arrray is sorted and to rotate left from tth postion
- array sice method is used to add before nth and after n th  nnum
####  python code 

```python
def leftRotate( arr, k):
     # Your code goes here
     return arr[k:] + arr[:k]
print('leftRotate([1,2,3,4,5,6],3): ', leftRotate([1,2,3,4,5,6],3))

```


<hr>

### Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

#### concept:
In this problem there can be  multiple solution
####  python code 

```python
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
            j+=1 # it will not increase until there is non zero number
    return arr
```


<hr>

### Given an array, rotate the array to the right by k steps, where k is non-negative

#### concept:
In the first solution ,for loop is used to remove from the last and add to front as the value of K

In solution two ,a new array is declared with the length of given list,and a for loop is used to decide the position of the element after k right rotation
####  python code 

```python
# solution 1 
def rotate_right(arr:list,k):
    for i in range(k):
        x=arr.pop()
        arr.insert(0,x)
    return arr
# solution  2
def rotate_extraspace(nums:list,  k:int) {
    # intializing the base case 
   if (k==0) return
   if (nums == null or nums.length == 0) return
#    creating the new array list 
   res = [None]*nums.length
   for i in range(len(nums)):
        newIndex = (i + k) % nums.length
        res[newIndex] = nums[i]
   
    print(res)
    for i in range(len(nums)):
        nums[i] = res[i]
    print(res)
```


<hr>

### find the missing number from the  array of range 0 -n in which one is missing 


#### concept:
Mathematical concept is used

####  python code 

```python
def missingNumber(nums:list):
    n=len(nums)
    totalSum=(n*(n+1))/2
    arrSum=sum(nums)
    return int(totalSum-arrSum)
```


<hr>

###  finding most consecutive 1 in an array of binary

#### concept:

####  python code 

```python
def findMaxConsecutiveOnes( nums:list) -> int:
    count=0 #track the current count of consecutive one 
    max=0 # track the maximum number of 1 has been occured
    for i in range(len(nums)):
        if nums[i] == 0:
            count=0
        else:
            count+=1
        if count>max:
            max+=1
    return max
```


<hr>

### Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.


#### concept:

####  python code 

```python
def subarraySum( nums: list, k: int) -> int:
    count=0 # track the number of subarray found
    totalSum=0 # track the  sum to the ith value of array
    sumobj=defaultdict(lambda : 0) # hashmap to store the sum so far acheived 
    for i in range(len(nums)):
        totalSum+=nums[i]
        if totalSum == k:
            count+=1
        if totalSum-k in sumobj: # checking the  if total sum - k(required sum ) is there in the object ,if it is then add its value to get the subarray so far occured
            count+=sumobj[totalSum-k]
        sumobj[totalSum]+=1
    print(sumobj)
    return count
```


<hr>

###  Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.You must implement a solution with a linear runtime complexity and use only constant extra space.


#### concept:

####  python code 

```python
def singleNumber(self, nums: List[int]) -> int:
    return 2*sum(set(nums))-sum(nums)
```


<hr>

###  Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:Integers in each row are sorted from left to right.The first integer of each row is greater than the last integer of the previous row.


#### concept: matrix of size of n(row)*m(column), a[x]=matrix[x/m][x%m]``

####  python code 

```python
def searchMatrix(matrix:list,target:int)->bool:
    n=len(matrix)
    m=len(matrix[0])
    left=0
    right=n*m-1
    while left<right:
        mid=(left+right)/2
        midValue=matrix[int(mid/m)][int(mid%m)] 
        if(midValue== target):
            return True
        if(midValue<target):
            left=mid+1
        else:
            right=mid
    return False
```


<hr>

### searchInsert

#### concept: binary Search is used and condition is changed inside the while loop

####  python code 

```python
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
```


<hr>

### 

# Medium Level





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


