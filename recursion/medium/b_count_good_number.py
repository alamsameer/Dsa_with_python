
# not optimal Solution
# import math
# def countGoodNumbers( n: int) -> int:
#         count=0
#         largest=0
#         smallest=0
#         if n ==1:
#             largest=9
#             smallest=0
#         else:
#             smallest=10**(n-1)
#             largest='9'*n
#             largest=int(largest)
#         print(smallest,largest)
#         for i in range(smallest,largest):
#             # print( isGood(str(i)),i)
#             if  isGood(str(i)):
#                 count+=1
#         return count
                
                
            
# def isGood(strg):
#     i=0
#     check=True
#     while i<len(strg) and check:
#         check=False
#         if i%2==0:
#             if  isEven(strg[i]):
#                 check=True
#                 i+=1
#             else:
#                 check=False
#                 break
#         else:
#             if  isPrime(strg[i]):
#                 check=True
#             else:
#                 check=False
#                 break
#     return check
            
# def isEven( x):
#     return int(x)%2==0
# def isPrime( x):
#     lst=math.sqrt(int(x))
#     i=0
#     while i<lst:
#         if int(x)%i ==0:
#             return False
#     return True


# print('countGoodNumbers(4): ', countGoodNumbers(4))

