def selectionSort(arr):
    for i in range(len(arr)):
        min=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[i]:
                min=j
        arr[i],arr[min]=arr[min],arr[i]
    return arr
print('selectionSort([23,5,7,1]): ', selectionSort([23,5,7,1]))