"""
Programming 102
101 Review
"""

"""
Units 1 & 2 - variables, strings & string operations, f-strings, input(), int/float
"""

import string

# = is the assignment operator. Assigns the value on the right to the variable on the left.
# define a variable 'animal' and assign the string 'dog' to it using =
animal = 'dog'
# print(animal) # dog

# ------------------------------------------------------------------------------------- #

# a "function" is a named code block that performs a specific task
# functions are executed by placing parentheses () after their name
# data can be passed into the function by placing it within the parentheses
# functions will always return a value as well

# type(object) - return the datatype of the object
animal_datatype = type(animal)
# print(animal_datatype) # <class 'str'>

# string (str) - sequence of textual characters surrounded by quotes
# --------------------------------------------------------------------------------------- #

# change the value within the variable 'animal' to 'cat'
animal = 'cat'
# print(animal) # cat

# --------------------------------------------------------------------------------------- #

# concatenation - adding strings together to form a single string

# add the string 'fish' to the value within the variable 'animal'
# redefined 'animal' with the result
animal = animal + 'fish'
# print(animal) # catfish

# --------------------------------------------------------------------------------------- #

# a 'method' is a function that manipulates only the object to which it belongs
# an object's methods are accessed using a dot after the object's name

# .upper() - return an uppercase version of the string
# print(animal.upper()) # CATFISH

# .replace(old, new) - return a copy of the string with the old replaced with the new within it
# print(animal.replace('c', 'b')) # batfish

# methods can be chained. Each one operates on the return value of the previous
# print(animal.replace('c', 'b').upper()) # BATFISH

# ---------------------------------------------------------------------------------------------- #

"""
Escape Characters
- Denoted with a backslash \ before the character 
- "Escape" the normal rules of strings to allow the characters to behave differently than normal
"""

# print("hello "world"") # Error! Quotes cancel each other

# Solution 1 - printing quotes with mismatched sets:
# print('hello "world"') # hello "world"

# Solution 2 - printing quotes with escape characters
# print("hello \"world\"") # hello "world"

# formatting string with escape characters
# print("A\nB\nC") # \n - new line character
# print("A\tB\tC") # \t - horizontal tab

# ------------------------------------------------------------------------------------------- #

'''
Python Variable Names
- must start with a letter or underscore
- cannot start with a number
- can only contain alphanumeric characters and underscores (A-z, 0-9 and _)
- are case sensitive (age, Age, AGE are 3 different variables)
'''

# python_variable_and_function_names_use_snake_case
# all lowercase words, separated with underscores

# ThisIsPascalOrTitleCase - used for defining classes in Python
# ALLCAPS - generally used for constant variables

# for Python styling conventions check out PEP8 (Python Style Guide)

# ----------------------------------------------------------------------------------------- #

# f-strings
# 'f' stands for 'formatted'. f-strings allow Python expressions to be formatted into strings

# note: concatenation only works with strings
# other datatypes will need to be "typecast" using str() before concatenation

number = 99.5
# output = 'The number is ' + str(number) + '!'

# f-strings don't care about datatype
output = f"The number is {number}!"
# print(output) # The number is 99.5!

# ----------------------------------------------------------------------------------------- #
'''
user_string = input(prompt_message)

Print the prompt message and wait for the user to hit enter.
Once the user hits enter, anything they typed in the terminal will be returned.
Return value can be saved in a variable such as 'user_string'

name = input('Enter your name: ')
print(f"Welcome, {name}!")
'''


# ------------------------------------------------------------------------------------------ #
'''
# input() always returns a string

# typecast to a number
# int(object) - return the object as an integer, if possible
# float(object) - return the object as a float, if possible

'''

'''
number = input("Enter a number: ")

print(number, type(number)) # 9 <class 'str'>
print(number * 10) # 9999999999

# convert the number string to float
number = float(number)

print(number, type(number)) # 9.0 <class 'float'>
print(number * 10) # 90.0
'''

# ----------------------------------------------------------------------------------------- #

# integer (int) - whole numbers
# float (float) - decimal numbers

# arithmetic operators

x = 5
y = 3

# print(x + y)  # addition +
# print(x - y)  # subtraction -

# print(x * y)  # multiplication *
# print(x ** y) # exponentiation ** (x^y)

# print(x / y)  # 'regular' division / (results in a float)
# print(x // y) # 'floor' division // (rounds down to the nearest integer)

# print(x % y)  # modulus % (remainder after division)

# ----------------------------------------------------------------------------------- #

# ReAssignment Operators

x = 4

# ReAssignment Operators - combine the arithmetic and assignment operators
x += 2 # x = x + 2
x -= 2 # x = x - 2
x *= 2 # x = x * 2
x **= 2 # x = x ** 2
x /= 2 # x = x / 2
x //= 2 # x = x // 2
x %= 2 # x = x % 2

# ----------------------------------------------------------------------------------------- #

'''
Unit 3 - booleans, comparisons, logical statements, conditionals
'''

# datatype - boolean
# True / False

a = True
b = False

# print(a, type(a)) # True <class 'bool'>
# print(b, type(b)) # False <class 'bool'>

# booleans in Python are Capitalized
# b = false # NameError: name 'false' is not defined

# -------------------------------------------------------------------------------------- #

# typecast to boolean
# bool(object) - return a boolean representation of the object

# Truthy/Falsey
# if an object has value, it will convert to True
# if an object has no value, it will convert to False
'''
# Falsey values
''    # blank string has no value
[]    # blank list has no value
0     # number 0 has no value
None  # None has no value
etc...
'''

# -------------------------------------------------------------------------------------- #

# Comparison Operators - compare two pieces of data and result in a boolean

# All comparisons need two sides

x = 5
y = 5

# print(x == y)  # == check equality - True
# print(x != y)  # != check inequality - False

# print(x < y) # < 'strictly' less than - False
# print(x <= y) # <= less than or equal to - True

# print(x > y) # > 'strictly' greater than - False
# print(x >= y) # >= greater than or equal to - True

# ---------------------------------------------------------------------------------------- #

# Logical Operators - combine comparisons and result in a single boolean
# and, or, not

# logical statements need two comparisons

x = 5
y = 5

# and - True only if BOTH comparisons are True
# print(x == 5 and y == 5) # True - both comparisons are True
# print(x == 5 and y == 2) # False - left comparison (y == 2) is False

# or - True if at least ONE comparison is True
# print(x == 5 or y == 2)  # True - left comparison (x == 5) is True
# print(x == 2 or y == 2)  # False - both comparisons are False

# not - flip a boolean
# print(x < 0) # False
# print(not x < 0) # True

# 'not' is often used with the keyword 'in' to check if an item is in a sequence
# print(33 in [22, 33, 44]) # True
# print(44 not in [11, 22, 33]) # False

# ---------------------------------------------------------------------------------------- #

'''
Conditional Statements
----------------------
Run different code blocks based on the outcome of comparisons
Keywords: if, elif, else

Code Block:
A section of code that executes together.
In Python, code blocks are defined using horizontal indentation
---------------------------------------------------------------------------------------

Conditional Rules:
------------------
- must start with if
- all ifs will be checked
- elif are only checked if the preceding if and other elifs were False
- else is triggered if all other conditions were False
- if/elif will only be checked until a True condition is found

---------------------------------------------------------------------------------------
Conditional Combinations:
-------------------------
if
if / elif
if / else
if / elif / else
if / elif / elif / ... / elif
if / elif / elif / ... / else
'''

'''
x = 5

if x > 5:
    print(f"{x} is greater than 5")

elif x < 5:
    print(f"{x} is less than 5")

else:
    print('x is 5')

'''
# ------------------------------------------------------------------------------------------- #

'''
Unit 4 - lists / for loops
------
Datatype: list

Lists are 'ordered' and 'changeable' sequences of items.
Lists are created using square brackets []
List items are separated with commas ,
'''

# define a list of colors
colors = ['red', 'green', 'blue']

# organized vertically
colors = [
    'red',
    'green',
    'blue'
]

# print(colors) # ['red', 'green', 'blue']

# ------------------------------------------------------------------------------------------- #

# list items can be retrieved using their positions in the list
# an item's position in the list is called its 'index'

# place the index of the item in square brackets
# after the list's variable name to retrieve the item
# list indices always start at 0
# print(colors[0]) # red
# print(colors[1]) # green
# print(colors[2]) # blue

# can't use non-existent indices
# print(colors[3]) # IndexError: list index out of range

# In Python, negative indices are allowed
# -1 will always be the last index
# print(colors[-1]) # blue
# print(colors[-2]) # green
# print(colors[-3]) # red

# can't use non-existent indices
# print(colors[-4]) # IndexError: list index out of range

# ------------------------------------------------------------------------------------ #

# strings are ordered sequences as well
ABCs = string.ascii_uppercase
# print(ABCs[10]) # K

# strings are NOT 'changeable'
# ABCs[0] = 'Z' # TypeError: 'str' object does not support item assignment

# lists ARE changable
colors[1] = 'yellow'
# print(colors) # ['red', 'yellow', 'blue']

# ------------------------------------------------------------------------------------- #

# cannot add values this way
# colors[3] = 'purple' # IndexError: list assignment index out of range

# items can be added using list methods

# .append(item) - add a single item to the end of the list
colors.append('purple')
# print(colors) # ['red', 'yellow', 'blue', 'purple']

# .insert(index, item) - add the item at the index
colors.insert(0, 'magenta')
# print(colors) # ['magenta', 'red', 'yellow', 'blue', 'purple']

# .extend(sequence) - add the items from the sequence to the end of the list
colors.extend(['orange', 'yellow', 'cyan'])
# print(colors) # ['magenta', 'red', 'yellow', 'blue', 'purple', 'orange', 'yellow', 'cyan']

# -------------------------------------------------------------------------------------- #

# items can be removed with list methods as well

# .remove(item) - remove the first occurrence of the item from the list
colors.remove('yellow')
# print(colors) # ['magenta', 'red', 'blue', 'purple', 'orange', 'yellow', 'cyan']

# .pop(index) - remove the item at the index and return it. index defaults to -1 if not provided
# colors.pop()
# print(colors) # ['magenta', 'red', 'blue', 'purple', 'orange', 'yellow']

# colors.pop(1)
# print(colors)  # ['magenta', 'blue', 'purple', 'orange', 'yellow']

# ------------------------------------------------------------------------------------------- #

# .sort() - sort a list in ascending order (returns None)
# colors.sort()
# print(colors) # ['blue', 'cyan', 'magenta', 'orange', 'purple', 'red', 'yellow']

# .sort() returns None
# colors = colors.sort()
# print(colors[0]) # TypeError: 'NoneType' object is not subscriptable
# print(colors) # None

# ---------------------------------------------------------------------------------------------- #


# loop - a code block that repeats until a certain condition is met

# for item in sequence - loop through each item in the sequence

# for/in - Python operators
# item - arbitrary variable name to store each item as the loop visits it
# sequence - string, list or other 'iterable' (loopable) object
'''
for color in colors:
    print(color)
'''
# -------------------------------------------------------------------------------------------- #

numbers = [2, 4, 6]

numbers_squared = []

for number in numbers:
    # square the number and add it to the list
    numbers_squared.append(number ** 2)

# print(numbers_squared)

# ---------------------------------------------------------------------------------------------- # 
# for x in range() - loop a certiain number of times

# range(stop) - return a range of numbers from 0 to stop-1
# print(list(range(10))) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


powers_of_2 = []
for number in range(11):
    powers_of_2.append(2 ** number)

# print(powers_of_2) # [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]

# range(start, stop, step)
'''
for x in range(0, 101, 10):
    print(x)
'''
# -------------------------------------------------------------------------------------- #

# while loop

'''
while some_condition == True:
    # loop this
    # code block
'''

# "for x in range(10)" with a while loop

x = 0

while x < 10:
    # print(x)

    x += 1

# -------------------------------------------------------------------------------------- #

# loop controls
# continue, break, else

for x in range(10):

    if x == 8:
        print('goodbye')
        break # end the loop immediately

    elif x == 3:
        print('...')
        continue # skip the rest of this iteration and begin the next

    print(x)

else:
    # else will be run if the loop makes it all the way through =
    # i.e. if its condition becomes False
    print("The loop ran all the way through")