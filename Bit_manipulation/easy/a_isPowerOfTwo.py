def isPowerOfTwo( n: int) -> bool:
    # n will check if n is greater than 0 and  not(n&(n-1)) will check if n is the power of 2 or not
    return (n and not(n & (n-1)))
print(isPowerOfTwo(255))