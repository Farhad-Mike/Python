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
from os import stat
from os import * 

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