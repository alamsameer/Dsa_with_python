# Python is an object oriented programming language.

# Almost everything in Python is an object, with its properties and methods.

# syntax 

# class Myclass:
#     x="sam"

# a=Myclass()
# print(a.x)


# ________The __init__() Function_____

# All classes have a function called __init__(), which is always executed when the class is being initiated.

# class college:
#     def __init__(self,name,age):
#         self.n=name
#         self.a=age
# student= college("sameer",34)

# print(student.n)

# print(student.a)

# _____ object method ______

# class college:
#     def __init__(self,name,age):
#         self.n=name
#         self.a=age
#     def showDetail(self):
#         print("Detail of the student"+self.n)
# student= college("sameer",34)

# student.showDetail()


# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

# It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:
