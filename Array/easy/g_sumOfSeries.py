# __1___-solution one _______

# def sumOfSeries(N):
#       #code here
#       print(N)
#       if(N <1):
#           return 0 
#       return pow(N,3)+sumOfSeries(N-1)

# 

# ____2______
    # def sumOfSeries(N):
    #     #code here
    #     sum=0
    #     for i in range(1,N+1):
    #         sum+=pow(i,3)
    #     return sum

# efficient solution using formiula

def sumOfSeries(n):
    x = (n * (n + 1)  / 2)
    return (int)(x * x)

print(sumOfSeries(5))
