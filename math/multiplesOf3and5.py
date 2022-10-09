def multiplesOf3and5(num):
    sum=0
    for i in range(num):
        if(i%3==0 or i%5==0):
            sum+=i
    return sum

# print(multiplesOf3and5(10))
# print(multiplesOf3and5(49))
# print(multiplesOf3and5( 1000))
# print(multiplesOf3and5(8456))
# print(multiplesOf3and5(19564))
