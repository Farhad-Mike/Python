num = 5 ** 3    # Result is 25
helloworld = 'hello' + ' ' + 'world'    # String concatination

# List concatenation
list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]
sumList = list1 + list2
# __________________ 

# List multiplication
mulList = [1, 2, 3] * 3

# String C-style formating
"%s is %d years old." % ('Farhad', '28') # Result: Farhad is 28 years old.
# %s - String (or any object with a string representation, like numbers)
# %d - Integers
# %f - Floating point numbers
# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
# %x/%X - Integers in hex representation (lowercase/uppercase)

# Length of iterable datas
len('hello')
len([1, 2, 4])

# Index(position) of symbol in string. Count start from 0
string1 = 'hello world and all people'
string1.index('l')

# Symbol count in string
string1.count('l')

# Cut from string
string1[3:7]    # Result: 'lo w'
string1[3:11:2] # Result: 'l ol'
string1[::-1]   # Result is reverse string: 'elpoep lla dna dlrow olleh'

# String case sensivity
string1.upper()
string1.lower()
string1
# String start, stop
string1.startswith('hello')     # Result: True
string1.endswith('sometext')    # Result: False

# Split string and make it list
string1.split('splitSym')

# Conditions
5 == 5
5 > 4
5 < 6
5 != -5

# And, or, in, is, not
5 == 5 and 5 < 6
5 == 5 or 6 > 5
5 is 5                  # Compare is it the same object or no
's' in 'string'         # Return True or False
False == (not False)    # Convert the boolean value

# If, elif, else
position = 'Linux'
admins = ['Farhad', 'Yusif', 'Sarkhan', 'Anar']
if position == 'Linux' and 'Farhad' in admins:
    'Do some statement'
    pass    # Skipp another statement
elif position == 'Windows' and 'Yusif' in admins:
    'Do second statement'
    pass
else:
    'Do third statement'
    pass

# Loop For
for s in string1:
    'statement'

# Generate range of numbers
range(5)
range(3, 10)
range(3, 10, 2)     # The third value is step

# Loop WHILE
count = 0
while count < 5:
    count += 1

# Breake statement. Used for exit from loop.
while True:
    count += 1
    if count > 5:
        break

# Continue statement. Skip one step in loop
for x in range(10):
    if x % 2 == 0:
        continue

# Else in loops
for x in string1:
    'statement'
else:
    '''
    When the loop condition of "for" or "while" statement fails then code part in "else" is executed
    If a break statement is executed inside the for loop then the "else" part is skipped. 
    Note that the "else" part is executed even if there is a continue statement
    '''

# Function
def my_function_with_args(username, greeting, num1, num2):
    print("Hello, %s , From My Function!, I wish you %s"%(username, greeting))
    return num1 + num2

# Class
class MyClass:
    x = 'variable'
    def myFunction(arg):
        'statement'
objFromMyClass = MyClass()
objFromMyClass.x
objFromMyClass.myFunction()

# Class with __init__
class MyClass:
    def __init__(self, num):    # Self is like this
        self.num = num
    def showNumber(self):
        return self.num
objFromMyClass = MyClass(5)
objFromMyClass.showNumber()

# Dictionaries
phonebook = {
    'Farhad' : 123456789,
    'Yusif'  : 987654321
}
phonebook['Anar'] = 741852963
phonebook['Sarkhan'] = 963852741

# Iterate dictionaries through loop
for name, number  in phonebook.items():
    print('Name: %s, Number: %d' % (name, number))

# Dictionarie, remove item
del phonebook['Farhad']
phonebook.pop('Sarkhan')

# Import
import gzip
import gzip as tvf
from itertools import filterfalse
from os import stat
from os import *
from stringprep import in_table_c3
from Python.LibFunctools import multiply 

# Show all attributes and local methods from obj
dir(gzip)
help(gzip.open)

# Packages
'''Packages are namespaces containing multiple packages and modules. They're just directories, but with certain requirements.
Each package in Python is a directory which MUST contain a special file called __init__.py. This file, which can be empty, indicates that the directory it's in is a Python package. That way it can be imported the same way as a module.
If we create a directory called foo, which marks the package name, we can then create a module inside that package called bar. Then we add the __init__.py file inside the foo directory.'''
import foo.bar
from foo import bar
'''Файл __init__.py также может решить, какие модули пакет экспортирует как API, оставляя другие модули внутренними, переопределяя переменную __all__ следующим образом
__init__.py:
__all__ = ["bar"]
'''

# Sort iterable data and convert to list
sorted(string1)

# Get of data type
type(5)

# Tuple
tup = (1, 2, 3, 4, 5)

# Yield
import random
def lottery():
    # returns 6 numbers between 1 and 40
    for i in range(6):
        yield random.randint(1, 40)
    # returns a 7th number between 1 and 15
    yield random.randint(1, 15)
for random_number in lottery():
       print("And the next number is... %d!" %(random_number))

# List comprehension
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = [len(word) for word in words if word != "the"]
print(words)
print(word_lengths)

# Lambda function (anonymous function). Lambda functions, are inline functions defined at the same place we use it.
a = 1
b = 2
sum = lambda x,y : (x + y)
c = sum(a,b)
print(c)

# Function wth multiple arguments (list)
def foo(first, second, third, *therest):
    print("First: %s" %(first))
    print("Second: %s" %(second))
    print("Third: %s" %(third))
    print("And all the rest... %s" %(list(therest)))
foo(1, 2, 3, 4, 5)

# Get key of dictionary
phonebook.get('Farhad') # Return value for key 'Farhad'

# Function wth multiple arguments (dictionary)
def bar(first, second, third, **options):
    pass
bar(1, 2, 3, action = "sum", number = "first")

# Catch error
try:
    pass
except IndexError as errorVariable:
    pass

# Sets are lists with no duplicate entries
setVar = set([1, 2, 3, 4, 5, 5, 4, 3, 2, 1])
setVar = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}

# Set intersection. Find same values in both sets
a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])
a.intersection(b)
b.intersection(a)

# Set symmetric_difference. Find only private values in both sets
a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])
print(a.symmetric_difference(b))
print(b.symmetric_difference(a))

# Set difference. Find private value only of one set
a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])
print(a.difference(b))
print(b.difference(a))

# Set union. Compinate sets
a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])
print(a.union(b))

# Code Introspection
help()
dir() 
hasattr() 
id() 
type() 
repr() 
callable() 
issubclass() 
isinstance() 
__doc__ 
__name__

# Nonlocal
def function1(num1):
    pass
    def function2():
        nonlocal num1   # nonlocal used for access to modify the variable in enclosing function
        num1 = 'value'
    function2()

# Nested function
def transmit_to_space(message):
    "This is the enclosing function"
    def data_transmitter():
        "The nested function"
        print(message)
    return data_transmitter
returnedFunc = transmit_to_space('Hello')

# Raise error
def raisError():
    raise (ValueError, "Negative Argument")

# Decorators
def multiply(multiplier):
    def multiply_generator(old_function):
        def new_function(*args, **kwds):
            return multiplier * old_function(*args, **kwds)
        return new_function
    return multiply_generator # it returns the new generator
@multiply(3) # multiply is not a generator, but multiply(3) is
def return_num(num):
    return num
# Now return_num is decorated and reassigned into itself
return_num(5) # should return 15

# Check the same type or not
isinstance(5, int)

# Round
round(5.3456, 3)

# Map. map(func, *iterables). The func will executed for every element in list
'''In Python 3, however, the function returns a map object which is a generator object. To get the result as a list, the built-in list() function can be called on the map object.'''
'''map(func, [funcArg1], [funcArg2], ...)'''
my_pets = ['alfred', 'tabitha', 'william', 'arla']
map(str.upper, my_pets)

# Zip
'''Функция zip() принимает один или более итерируемых объектов и возвращает итератор, который в свою очередь возвращает кортежи. Первый кортеж включает в себя первые элементы всех итерируемых объектов, второй кортеж – вторые элементы и т. д., итерации прекращаются, как только содержимое любого из итерируемых объектов будет исчерпано.'''
'''Return zip object which you can convert to another iterable data type for example to list()'''
it1 = [1, 2, 3, 4, 5, 6]
it2 = ['a', 'b', 'c', 'd', 'e', 'f']
zip(it1, it2)

# Filter. Return filter object which can be converted to iterable object. Return only the elements that is return True
it3 = [1, 2, 3, 4, 5, 6, 7]
filter(lambda x : x > 2, it3)


# Reduce. Needs to be imported as it resides in the functools module.
'''Передает в функцию два аргумента. Производит работу по функции над аргументами, а результат записывает снова как первый аргумент. Начальный аргумент может быть задан, а может и не быть задан.'''
from functools import reduce
it4 = [1, 2, 3, 4, 5, 6, 7]
reduce(lambda x, y : x + y, it4, 10)
