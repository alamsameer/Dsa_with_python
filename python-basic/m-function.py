def my_function():
  print("Hello from a function")

my_function()

# If you try to call the function with less or more argument you will get an error 

# -- default argument 

def my_function(country = "Norway"):
  print("I am from " + country)
my_function("india")
