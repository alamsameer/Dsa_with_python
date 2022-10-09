def factorialNumbers(self, N):
    #code here 
    fact=1
    x=2
    fact_list=[]
    while fact<N:
        fact_list.append(fact)
        fact*=x
        x+=1
    return fact_list