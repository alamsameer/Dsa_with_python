# _______________PYTHON SET________________

# A set is a collection which is unordered, unchangeable*, and unindexed
# Set items can appear in a different order every time you use them, 
# and cannot be referred to by index or key.

# myset = {"apple", "banana", "cherry"}
# set1 = {"abc", 34, True, 40, "34","male"}
# print(set1)

# --------add method in set to add item 

# set1.add("abcl")
# print(set1)

# ---------------add set using update()

# thisset = {"apple", "banana", "cherry"}
# tropical = {"pineapple", "mango", "papaya"}

# thisset.update(tropical)

# print(thisset)

# The object in the update() method does not have to be a set, 
# it can be any iterable object (tuples, lists, dictionaries etc.).

# ----------remove in set 
# To remove an item in a set, use the remove(), or the discard() method
# thisset = {"apple", "banana", "cherry"}

# thisset.remove("banana")
# thisset.discard("apple")
# print(thisset)

# -------- loop 
# thisset = {"apple", "banana", "cherry"}

# for x in thisset:
#   print(x)

# ----- join two set
#  1- union ,2-update

# set1 = {"a", "b" , "c"}
# set2 = {1, 2, 3}

# set3 = set1.union(set2)  or set1.update(set2)
# print(set3)

# intersection_update() will keep item present in both 

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}

# x.intersection_update(y)

# print(x,y)

# -------intersection(): The intersection() method will return a new set, that only contains the items that are present in both sets.
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}

# z=x.intersection(y)
# print(z)

# The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.

# x.symmetric_intersection_update()

# The symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets.

# z=x.symmetric_difference()

# add()	Adds an element to the set
# clear()	Removes all the elements from the set
# copy()	Returns a copy of the set
# difference()	Returns a set containing the difference between two or more sets
# difference_update()	Removes the items in this set that are also included in another, specified set
# discard()	Remove the specified item
# intersection()	Returns a set, that is the intersection of two other sets
# intersection_update()	Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	Returns whether two sets have a intersection or not
# issubset()	Returns whether another set contains this set or not
# issuperset()	Returns whether this set contains another set or not
# pop()	Removes an element from the set
# remove()	Removes the specified element
# symmetric_difference()	Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	inserts the symmetric differences from this set and another
# union()	Return a set containing the union of sets
# update()	Update the set with the union of this set and others