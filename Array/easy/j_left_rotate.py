# def leftRotate(arr,k):
#     i=0
#     for i in range(0, k):    
#         #Stores the first element of the array    
#         first = arr[0];    
            
#         for j in range(1, len(arr)-1):    
#             #Shift element of array by one    
#             arr[j] = arr[j+1];          
#         #First element of array will be added to the end    
#         arr[len(arr)-1] = first; 
#         # print(arr)  
#     return arr 

def leftRotate( arr, k):
     # Your code goes here
     return arr[k:] + arr[:k]
print('leftRotate([1,2,3,4,5,6],3): ', leftRotate([1,2,3,4,5,6],3))