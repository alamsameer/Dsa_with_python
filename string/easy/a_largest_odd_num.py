# find the largest odd from a string number 

# solution approach 
#  start from back 
# check if it even or odd ,if even then change num digit less than 1 
# if odd return it 

def largestOddNumber(num):
    while len(num)>0 and (int(num[-1])%2 ==0):
        num=num[:-1]
    return num
print('largestOddNumber("212426"): ', largestOddNumber("212426"))