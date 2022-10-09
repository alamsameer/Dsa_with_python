# _________dictionary____________
# Dictionaries are used to store data values in key:value pairs.

# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict)

# print(thisdict["brand"])

# -------accessing values

# x = thisdict["model"]
# print(x)
# x = thisdict.get("model")

# print(x)

# ------ keys() :will return a list of all the keys in the dictionary.
# x = thisdict.keys()
# print(x)

# --------The values() method will return a list of all the values in the dictionary.
# x=thisdict.values()

# The items() method will return each item in a dictionary, as --tuples--in a list.
# x = thisdict.items()
# print(x)

# -------Check if "model" is present in the dictionary:

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# if "model" in thisdict:
#   print("Yes, 'model' is one of the keys in the thisdict dictionary")

#  changing value in dictionary

# thisdict["year"] = 2018

# ---update()
# thisdict.update({"year": 2020}) update if exist otherwise add to the dictionary

# -- dlete item using pop()
# thisdict.pop("model")
# ---------------popitem() method removes the last inserted item
# -- del keyword
# del thisdict["model"]
# The clear() method empties the dictionary:

# ---- copy dictionary

# 1-dict1.copy()
# 2-dic(dict1)


# ______methods in dictionary 

# clear()	Removes all the elements from the dictionary
# copy()	Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and value
# get()	Returns the value of the specified key
# items()	Returns a list containing a tuple for each key value pair
# keys()	Returns a list containing the dictionary's keys
# pop()	Removes the element with the specified key
# popitem()	Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	Updates the dictionary with the specified key-value pairs
# values()	Returns a list of all the values in the dictionary