import math
def merge(left:list,right:list):
    l=0
    r=0
    result=[]
    while l<len(left) and r<len(right):
        if left[l]<right[r]:
            result.append(left[l])
            l+=1
        else:
            result.append(right[r])
            r+=1
    print(result)
    return result+left+right

def mergeSort(arr:list):
    if len(arr)== 1:
        return arr
    mid=math.floor(len(arr)/2)
    left=arr[0:mid]
    right=arr[mid:]
    return merge(mergeSort(left),mergeSort(right))

print('mergeSort([2,7,3,7,4,18,9]): ', mergeSort([2,7,3,8,7,4,18,9]))