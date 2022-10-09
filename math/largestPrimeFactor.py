def largestPrimeFactor(num):
    i=2
    primefactor=[]
    numq=num
    while(numq!=1):
        if(numq%i==0):
            numq /=i
            primefactor.append(i)
            i=2
        else:
            i+=1
    return primefactor[-1]
# print(largestPrimeFactor(7))
# print(largestPrimeFactor(600851475143))