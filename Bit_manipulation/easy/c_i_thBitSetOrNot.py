#. When we talk about the "i-th bit" of a number,
#  we mean the binary digit located at the i-th position from the right.

#To check if the i-th bit of a number is set (i.e., equal to 1), 
# we can use a bitwise operator in conjunction with a bit mask. 
# A bit mask is a number whose binary representation consists of all 0's except for a single 1 at the i-th position from the right.

x = 5  # binary representation: 0101
i = 2  # the i-th bit we want to check
mask = 1 << (i - 1)  # binary representation: 0010
if x & mask:
    print("The {}-th bit of {} is set.".format(i, x))
else:
    print("The {}-th bit of {} is not set.".format(i, x))
