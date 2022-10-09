# _________While loop 
i=10
while i<20:
    i+=1

    if i==16:
        break
    elif i==13:
        continue
    print(i)

# ____else with while 

while i<16:

    i+=1
    print(i)
else:
    print("i is no more")
print("global")

# ___________for loop 
# ---loop with list 
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)

#   loop with string 
# for x in "string":
#     print(x)


# _____ range 

# The range() function returns a sequence of
#  numbers, starting from 0 by default, 
# and increments by 1 (by default), and ends at a specified number.

# range(4) 0 to 3
# range(2,8) 2 to 7
# range(2,19,2) 2 to 18 with  gap of 2 like 2,4,6,8...


# _________ else in for  loop 

# for x in range(2,6,2):
#   print(x)
# else:
#   print("Finally finished!")

# The else block will NOT be executed if the loop is stopped by a break statement
