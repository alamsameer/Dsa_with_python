# loop for k time 
# remove from the last 
# insert at starting
# def rotate_right(arr:list,k):
#     for i in range(k):
#         x=arr.pop()
#         arr.insert(0,x)
#     return arr




# print('rotate_right([1,2,3,4],2): ', rotate_right([1,2,3,4],2))

# another direct solution

def rotate_extraspace(nums:list,  k:int):
    if (k==0): 
        return
    if (nums == None):
         return
    
    res= [None]*len(nums)
    for i in range(len(nums)):
            newIndex = (i + k) % len(nums)
            print('newIndex: ', newIndex,i + k,len(nums))
            res[newIndex] = nums[i]
    
    
    for i in range(len(nums)):
        nums[i] = res[i]
    print(nums)
    
print('rotate_right([1,2,3,4],2): ', rotate_extraspace([1,2,3,4],3))
