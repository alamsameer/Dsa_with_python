
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


# def count_good_numbers(n):
#     def is_good_number(num):
#         for i in range(n):
#             if i % 2 == 0:
#                 if (num[i] % 2) != 0:
#                     return False
#             elif num[i] not in (2, 3, 5, 7):
#                 return False
#         return True

#     def helper(n, num):
#         if n == 0:
#             return 1 if is_good_number(num) else 0
#         count = 0
#         for i in range(10):
#             count += helper(n-1, num + [i])
#         return count

#     return helper(n, [])

def count_good_numbers(n):
    def is_good_digit(d, idx):
        if (idx % 2 == 0 and d % 2 == 0) or (idx % 2 != 0 and d in (2, 3, 5, 7)):
            return True
        return False

    def helper(n, idx):
        if idx == n:
            return 1
        count = 0
        for d in range(10):
            if is_good_digit(d, idx):
                print("before",count)
                count += helper(n, idx + 1)
                print("after",count)

        print("inside helper",n,idx,count)
        return count
    return helper(n, 0)


print(count_good_numbers(int(input())))
