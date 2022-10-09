def bubbleSort(arr):
    swap=True
    # chekcing for  is their swap or not for sorted array swap will be false and it comes out of the loop  
    x=0
    while swap:
        swap=False
        x+=1
        for j in range(0,len(arr)-1):
            #  checking  next is larger  or not ,if yes then go inside if block 
            if arr[j]>arr[j+1]:
                swap=True
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
    print(x)
    return arr

print(bubbleSort([1,2,3,7]))