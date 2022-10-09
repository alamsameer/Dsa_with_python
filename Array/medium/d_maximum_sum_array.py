

def maxSubArray(self, nums) -> int:
    lmax=0
    gmax=float("-inf")
    for i in nums:
        lmax=max(i,lmax+i)
        if(lmax>gmax):
            gmax=lmax
    return gmax