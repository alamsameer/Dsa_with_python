def fiboEvenSum(n):
    n1=0
    n2=1
    nextnum=0
    evenfib=0
    while(n2<=n):
        if(n2%2 == 0):
            print("hlo n2")
            evenfib=evenfib+n2
        nextnum=n1+n2
        n1=n2
        n2=nextnum
    return evenfib
    
print(fiboEvenSum(8))
# print(fiboEvenSum(10))
# print(fiboEvenSum(34))
# print(fiboEvenSum(60))