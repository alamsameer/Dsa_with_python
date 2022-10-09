

# ____________python boolean __________
#  True ,False --- >,<,==

#  bool  function 
# print(bool("Hello"))
# print(bool(-1))

# Almost any value is evaluated to True if it has some sort of content.

# Any string is True, except empty strings.

# Any number is True, except 0.

# Any list, tuple, set, and dictionary are True, except empty ones.
# The following will return False:

# bool(False)
# bool(None)
# bool(0)
# bool("")
# bool(())
# bool([])
# bool({})


# object in this case, evaluates to False, and that is if you have an object that
#  is made from a class with a __len__ function that returns 0 or False:

# class myclass():
#   def __len__(self):
#     return 0

# myobj = myclass()
# print(bool(myobj))

# x = 200
# print(isinstance(x, int))
