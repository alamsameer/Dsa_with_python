# def reverseWord(s):
#     # your code here
#     s = [*s]
#     s.reverse()
#     reversedStr="".join(s)
#     print(reversedStr)
#     return reversedStr

# _____correct ans________

def reverseWord(s):
    return s[::-1]

print(reverseWord("ZRNKJZFPZWSOQCPKEKXJNL"))

# a[-1]    # last item in the array
# a[-2:]   # last two items in the array
# a[:-2]   # everything except the last two items
# # Similarly, step may be a negative number:

# a[::-1]    # all items in the array, reversed
# a[1::-1]   # the first two items, reversed
# a[:-3:-1]  # the last two items, reversed
# a[-3::-1]  # everything except the last two items, reversed