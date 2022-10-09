
# _____TLE ERROR___________
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