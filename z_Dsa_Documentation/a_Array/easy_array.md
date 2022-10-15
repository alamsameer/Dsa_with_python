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

#### concept:

####  python code 

```python
```


<hr>
