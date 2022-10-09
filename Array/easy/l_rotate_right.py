# loop for k time 
# remove from the last 
# insert at starting
def rotate_right(arr:list,k):
    for i in range(k):
        x=arr.pop()
        arr.insert(0,x)
    return arr

print('rotate_right([1,2,3,4],2): ', rotate_right([1,2,3,4],2))

# another direct solution

# def rotate_extraspace(nums:list,  k:int) {
#    if (k==0) return
#    if (nums == null or nums.length == 0) return
   
#    res = [None]*nums.length
#    for i in range(len(nums)):
#         newIndex = (i + k) % nums.length
#         res[newIndex] = nums[i]
   
#     print(res)
#     for i in range(len(nums)):
#         nums[i] = res[i];
#     print(res)
   
