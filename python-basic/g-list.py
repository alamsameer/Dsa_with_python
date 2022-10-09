# ___________ Python List __________List items are ordered, changeable, and allow duplicate values.

#  _--------List methods---------start 
#  insert(position,item)
# ----------------end-------------
# A list can contain different data types:
# list=["a",1,True,[],{}]
# print(list)

#  list ---- constructor-> list((items))

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:5])


# thislist = ["apple", "banana", "cherry"]
# thislist[1:3] = ["watermelon"]
# print(thislist)

# Insert ____ list using insert() method it will not replace the item of specified position
# thislist = ["apple", "banana", "cherry"]
# thislist.insert(2, "watermelon")
# print(thislist)

# append 
# thislist = ["apple", "banana", "cherry"]
# thislist.append("orange")
# print(thislist)

# extend method ----is used extend current list with another existing list 
# l1=[1,2,3,4]
# l2=[5,6,7,89]

# l1.extend(l2)
# print(l1)

# The extend() method does not have to append lists,
#  you can add any iterable object (tuples, sets, dictionaries etc.).

# l1=[1,2,3,4]
# t1=(1,2,3)
# t1.extend(l1)
# print(t1,type(t1))   will show error bcz tuple does not supoprt extend method 

#  ----- remove() will remove specified item 

# l1=[1,2,3,4]
# l1.remove(3)
# print(l1)

#  ---------pop() will remove specified index ,if index else revome from last 

# l1=[1,2,5,4]
# l1.pop(2)
# l1.pop()
# print(l1)

# --------del ----The del keyword also removes the specified index:

# l1=[1,2,5,4]
# del l1[2]
# print(l1)
# del l1
# print(l1)

# -------clear() will remove all element but list will empty

# l1=[1,2,5,4]
# l1.clear()
# print(l1)

# -------loop in list throught element 
# for x in l1:
#     print(x)
# ------- shorthand form of above print(x) for x in l1
# -------loop in list throught index
# for i in range(len(l1)):
#     print(i)
#     print(l1[i])

# __________list compression ----- it like doing operation shorthand type
#  offers a shorter syntax when you want to create a new list based on the values of an existing list. 
# OLD LIST IN NOT CHNAGED 
# fruits 
# = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []

# for x in fruits:
#   if "a" in x:
#     newlist.append(x)

# print(newlist)

# ------shorthand of above 
# shortList=[y for y in fruits if "a" in y] # variable y like should be same
# print(shortList)

#  SYNTAX : newlist = [expression for item in iterable if condition == True]
# newlist = [x for x in range(10)]
# print(newlist)
# newlist = ['hello'+x for x in fruits]
# print(newlist)
#  condition in expression 
# newlist = [x if x != "banana" else "orange" for x in fruits] #"Return the item if it is not banana, if it is banana return orange".
# print(newlist)

# ----------sort in list ---that will sort the list alphanumerically
# list.sort()  in ascending order
# list.sort(reverse=True) in decending order 

#  ---------- sort can be customized 
# def myfunc(n):
#     return n-70
# list=[100,40,64,89,60]
# x=list.sort(key=myfunc)
# print(list)
#  -----sort is case sensitive capital >lower letter
# print(list.sort(key=str.lower))

# --------reverse() will show  item in reverse order 

# --------copy method()

# You cannot copy a list simply by typing list2 = list1,
#  because: list2 will only be a reference to list1, 
# and changes made in list1 will automatically also be made in list2.

# thislist = ["apple", "banana", "cherry"]
# mylist = thislist.copy()
# print(mylist)

# ----------methods to join two or more list
# 1- +,2-a using for loop ,3-extend() 

# _______________METHODS IN LIST _____________

# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list

