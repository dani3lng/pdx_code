'''
Programming 101
Unit 4
'''

import random

'''
Datatype: list (list)

'Ordered' and 'changeable' sequences of items.

Items are separated with commas ,
Lists are defined using square brackets []

Since lists are 'ordered', their items can be retrieved using their positions in the list.
An item's position in the list is called its 'index' ('indices' plural)
'''

# define an empty list
empty_list = []

# print(empty_list, type(empty_list)) # [] <class 'list'>
# --------------------------------------------------------------------------------------------- #

# numbers = [11, -22, 33, -44] # list of integers
# colors = ['red', 'green', 'blue'] # list of strings

# list items can be ANY dataype, including other lists
jumble = ['cat', 99, None, 3.14, False, 'elephant', [1, 2, 3]]
# print(jumble) # ['cat', 99, None, 3.14, False, 'elephant', [1, 2, 3]]

# --------------------------------------------------------------------------------------------- #

# list items can be organized vertically

colors = [
    'red',
    'green',
    'blue'
]

# print(colors) # ['red', 'green', 'blue']

# --------------------------------------------------------------------------------------------- #

# retrieve an item from the list using its index
# place the index in square brackets after the list's variable name

# list indices always start at 0
# print(colors[0]) # red
# print(colors[1]) # green
# print(colors[2]) # blue

# can't use indices that don't exist
# print(colors[3]) # IndexError: list index out of range
# --------------------------------------------------------------------------------------------- #

# in Python, negative indices are allowed
# print(colors[-1]) # blue
# print(colors[-2]) # green
# print(colors[-3]) # red

# can't use indices that don't exist
# print(colors[-4]) # IndexError: list index out of range

# --------------------------------------------------------------------------------------------- #

# often, a variable will be used to represent an index
index = 2

# print(colors[index]) # blue


# --------------------------------------------------------------------------------------------- #

# strings are also 'ordered' sequences, which means
# indices can be used to retrieve each character in a string

letters = 'ABCDEFG'
# print(letters[0]) # A

# strings are NOT changeable
# letters[0] = 'Z' # TypeError: 'str' object does not support item assignment

# option 1: return a new string with the desired changes
# letters = letters.replace('A', 'Z')
# print(letters) # ZBCDEFG

# option 2: convert the string to a list
# list() - return the sequence as a list, if possible
letters = list(letters)
# print(letters) # ['A', 'B', 'C', 'D', 'E', 'F', 'G']

letters[0] = 'Z'
# print(letters) # ['Z', 'B', 'C', 'D', 'E', 'F', 'G']

# --------------------------------------------------------------------------------------------- #

# change the color at index 1 to 'yellow'
colors[1] = 'yellow'
# print(colors) # ['red', 'yellow', 'blue']

# cannot add values this way
# colors[3] = 'purple' # IndexError: list assignment index out of range

# --------------------------------------------------------------------------------------------- #

# add items using list methods

# .append(item) - add a single item to the END of the list and return None
colors.append('purple')
# print(colors) # ['red', 'yellow', 'blue', 'purple']

# .insert(index, item) - add the item at the index and return None
colors.insert(1, 'cyan')
# print(colors) # ['red', 'cyan', 'yellow', 'blue', 'purple']

# .extend(sequence) - add the items from the sequence to the end of the list
colors.extend(['magenta', 'yellow', 'pink'])
# print(colors) # ['red', 'cyan', 'yellow', 'blue', 'purple', 'magenta', 'yellow', 'pink']
# --------------------------------------------------------------------------------------------- #

# delete items using list methods

# .remove(item) - remove the first occurrence of the item from the list
colors.remove('yellow') 
# print(colors) # ['red', 'cyan', 'blue', 'purple', 'magenta', 'yellow', 'pink']

# .pop(index) - remove the items at the index and return it. Index defaults to -1 if not provided
# colors.pop() # remove the last item
# print(colors) # ['red', 'cyan', 'blue', 'purple', 'magenta', 'yellow']

# color = colors.pop(1)
# print(color, colors) # cyan ['red', 'blue', 'purple', 'magenta', 'yellow']


# --------------------------------------------------------------------------------------------- #

# random.choice() - return a random selection from a sequence (list,string)

# choose a random color from the list of colors
random_color = random.choice(colors)
# print(random_color)

ABCs = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
random_letters = random.choice(ABCs)
# print(random_letters)
# --------------------------------------------------------------------------------------------- #

'''
loop - a code block that repeats until a certain condition is met

'for' loop
-----------

for item in sequence - visit each item in a sequence (list, string, etc.)
for x in range() - loop a certain number of times

for/in - Python operators
item/x - arbitrary variable name to store each item from the sequence as it's visited
sequence/range() - iterable (loopable) object (list, string, range, etc...) through which to loop
'''

colors = ['red', 'cyan', 'blue', 'purple', 'magenta', 'yellow', 'pink']
'''
for color in colors:
    # loop this code block
    # for each item in the colors list
    print(color)
'''
# --------------------------------------------------------------------------------------------- #

counter = 1 # to label each color


for color in colors:
    output = f'{counter}. {color}'

    # print(output)
    
    # increase the counter to change the number label
    counter += 1
    
# --------------------------------------------------------------------------------------------- #

ABCs = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

vowels = ['A', 'E', 'I', 'O', 'U']

# loop through the string and print only the vowels
for letter in ABCs:
    # check if the current letter is a vowel
    if letter in vowels:
        output = letter
    
    else:
        output = '...'
        
    # print(output)


# --------------------------------------------------------------------------------------------- #

# for x in range() - loop a certain number of times

# range(stop_value) - return a range of number from 0 to stop_value -1

# print(range(10)) # range(0, 10)

# convert the range object to a list
# print(list(range(10))) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

'''
for number in range(10):
    print(number)

'''

# --------------------------------------------------------------------------------------------- #

# generate a list of the powers of 2 from 0 to 10


# blank list of numbers
powers_of_2 = []

# loop 11 times

for exponent in range(11):
    powers_of_2.append(2 ** exponent)
    
# print(powers_of_2) # [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]

# --------------------------------------------------------------------------------------------- #

# generate a list of 10 random numbers between 0 and 100

# blank list of numbers
numbers = []

# loop 10 times
for x in range(10):
    # generate a random number
    random_number = random.randint(0, 100)
    
    numbers.append(random_number)
    
    
#print(numbers)