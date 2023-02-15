# stack and queue

## concept

### stack and queue

**queue**: First-In-First-Out 
**stack**:Last-In-First-Out 

In Python, a queue is a collection of elements that supports adding elements to the back of the queue (enqueue) and removing elements from the front of the queue (dequeue). It follows the First-In-First-Out (FIFO) principle, which means that the element that was added to the queue first will be removed first.

Python provides a built-in module called queue that implements different types of queues, including:

- Queue: This is a basic queue implementation that provides all the necessary methods for adding and removing elements from the queue.

- LifoQueue: This is a variant of a queue called a "stack", which follows the Last-In-First-Out (LIFO) principle. It provides methods for adding and removing elements from the top of the stack.

- PriorityQueue: This is a variant of a queue where elements are dequeued based on their priority. Each element in the queue has an associated priority, and the element with the highest priority is dequeued first.

### classes
- Classes provide a means of bundling data and functionality together
- Creating a new class creates a new type of object, allowing new instances of that type to be made.
-  Each class instance can have attributes attached to it for maintaining its state
- Class instances can also have methods (defined by its class) for modifying its state.
- classes partake of the dynamic nature of Python: they are created at runtime, and can be modified further after creation.
 ```py

   class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

my_car = Car('Toyota', 'Corolla')
print(my_car.make)  # Output: Toyota

# Adding a new method to the class at runtime
def get_info(self):
    return f'{self.make} {self.model}'

Car.get_info = get_info
print(my_car.get_info())  # Output: Toyota Corolla

# Modifying an existing method of the class at runtime
def get_make_and_model(self):
    return f'{self.make} - {self.model}'

Car.get_info = get_make_and_model
print(my_car.get_info())  # Output: Toyota - Corolla

```
> what is this syntax for f'{self.make} {self.model}'

The syntax f'{self.make} {self.model}' is an example of an f-string in Python. An f-string is a formatted string literal that allows you to embed expressions inside string literals using curly braces {}.

In the example f'{self.make} {self.model}', the curly braces {} are used to embed the expressions self.make and self.model inside the string literal. When the f-string is evaluated, the expressions are replaced with their corresponding values, resulting in a string that combines the values of the make and model attributes of the object.

> Difference betwen global and nonlocal in python

**global keyword**
 the global keyword is used to access and modify global variables from within a function or a nested function,
```
count = 0  # global variable

def increment():
    global count  # accessing global variable
    count += 1

increment()
print(count)  # Output: 1

```
**nonlocal**
the nonlocal keyword is used to access and modify variables from an outer, enclosing function within a nested function.
```
def outer():
    x = 1  # enclosing function variable

    def inner():
        nonlocal x  # accessing variable from enclosing function
        x += 1

    inner()
    print(x)  # Output: 2

```
### Look at Classes

####  Class Definition Syntax
```py
class ClassName:
    <statement-1>
    .
    .
    .
    <statement-N>
```
####  Class objects

Class objects support two kinds of operations: attribute references and instantiation.

Attribute references use the standard syntax used for all attribute references in Python: obj.name

example :
```py
class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'
```
then MyClass.i and MyClass.f are valid attribute references, returning an integer and a function object, respectively

### Method Objects
Usually, a method is called right after it is bound:

```
x.f()
```
In the MyClass example, this will return the string 'hello world'. However, it is not necessary to call a method right away: x.f is a method object, and can be stored away and called at a later time. For example:

```xf = x.f
while True:
    print(xf())
    
```
will continue to print hello world until the end of time.

 ### Class and Instance Variables¶
Generally speaking, instance variables are for data unique to each instance and class variables are for attributes and methods shared by all instances of the class:

```py
class Dog:

    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.kind                  # shared by all dogs
'canine'
>>> e.kind                  # shared by all dogs
'canine'
>>> d.name                  # unique to d
'Fido'
>>> e.name                  # unique to e
'Buddy'
```
As discussed in A Word About Names and Objects, shared data can have possibly surprising effects with involving mutable objects such as lists and dictionaries. For example, the tricks list in the following code should not be used as a class variable because just a single list would be shared by all Dog instances:

```py
class Dog:

    tricks = []             # mistaken use of a class variable

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.add_trick('roll over')
>>> e.add_trick('play dead')
>>> d.tricks                # unexpectedly shared by all dogs
['roll over', 'play dead']
```
Correct design of the class should use an instance variable instead:

```py
class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.add_trick('roll over')
>>> e.add_trick('play dead')
>>> d.tricks
['roll over']
>>> e.tricks
['play dead']

```

### Inheritance

```py
class DerivedClassName(BaseClassName):
    <statement-1>
    .
    .
    .
    <statement-N>
```

The name BaseClassName must be defined in a scope containing the derived class definition. In place of a base class name, other arbitrary expressions are also allowed. This can be useful, for example, when the base class is defined in another module:
```py
class DerivedClassName(modname.BaseClassName):
```

Execution of a derived class definition proceeds the same as for a base class. When the class object is constructed, the base class is remembered. ```This is used for resolving attribute references: if a requested attribute is not found in the class, the search proceeds to look in the base class. This rule is applied recursively if the base class itself is derived from some other class.```

Python has two built-in functions that work with inheritance:

Use isinstance() to check an instance’s type: isinstance(obj, int) will be True only if obj.__class__ is int or some class derived from int.

Use issubclass() to check class inheritance: issubclass(bool, int) is True since bool is a subclass of int. However, issubclass(float, int) is False since float is not a subclass of int.

## topics to understand: [python class](https://docs.python.org/3/tutorial/classes.html)

- Private Variables
- Odds and Ends¶
-  Iterators¶
-  Generators¶
- Generator Expressions¶
