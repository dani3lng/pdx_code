'''
Programming 101
Unit 3
'''

# Datatype: boolean (bool)

# True / False

a = True
b = False

# print(a, type(a)) # True <class 'bool'>
# print(b, type(b)) # False <class 'bool'>

# in Python, booleans are capitalized
# b = true # NameError: name 'true' is not defined
# --------------------------------------------------------------------------------------------------- #


# Comparison Operators - compare two pieces of data and result in a boolean


x = 5
y = 5

# = is the assignment operator

# print(x == y) # == check equality - True
# print(x != y) # != check inequality - False


# print(x < y) # < 'strictly' less than - False
# print(x <= y) # <= less than or equal to - True


# print(x > y) # > 'strictly' greater than - False
# print(x >= y)  # >= greater than or equal to - True


# check the result of some math
# print (x / 2 == 2.5) # True

# check for a particular value in a variable

# print(x == 5) # True

# print(x == 99) # False
# ----------------------------------------------------------------------- #

# other datatypes can be compared as well
# can't compare unlike datatypes

word_1 = 'catt'
word_2 = 'catt'

# print(word_1 == word_2) # True
# print(word_1 == 'cat') # False

# ----------------------------------------------------------------------- #

# logical Operators - combine the results of two comparisons into a single boolean 
# and, or, not


x = 5 
y = 3

# and = True only if BOTH comparisons result in True

# print(x == 5 and y == 3) # True - both comparisons result in True

# print(x == 5 and x == y) # False - right comparison (x == y) results in False

# or - True if at least ONE comparison is True
# print(x == 5 or x == y) # True - left comparison (x == 5) results in True
# print(x == 1 or x == y) # False - both comparisons result in False


# not - flip a boolean
# print(x < 0)
# print(not x < 0) # True

# ------------------------------------------------------------------------------------ #

# 'not' is often used with the keyword 'in' to determine if an item is 'in' a sequence (list, string, etc..)

word = 'book'

# print('k' in word) # True
# print('z' not in word) # True

# ------------------------------------------------------------------------------------ #

'''
Conditional statements - if / elif / else


Run different code blocks based on the outcome of comparisons.

Code Block
----------

A section of code that executes together.
In Python, code blocks are defined using horizontal indentation

- must start with if
- every single if statement will be checked
- elif will only be checked if the preceding if and other elifs were False
- if/elif will only be checked until a True condition is found
- else will be run if all other conditions were False

'''

# ------------------------------------------------------------------------------------- #


light_switch = 'ON'

if light_switch == 'ON': # colon signifies the beginning of a code block
    # first line in a code block determines the indentation for the block
    message = 'I can see!'
    
elif light_switch == 'OFF':
    
    message = "It's dark in here!"
elif light_switch == 'DIM':
    
    message = 'The light is dim...'
else:
    
    message = 'The light is broken...'
    
# print(message)

# -------------------------------------------------------------------------------------- # 

x = 10
y = 10

if x < y:
    output = f'{x} is less than {y}'
    
elif x == 14:
    output = 'x is 14'
    
elif x > y:
    output = f'{x} is greater than {y}'
    
else:
    output = f'x and y are both {x}'
    
# print(output)
# ---------------------------------------------------------------------------------- #
# pretend this is line 1 of the file (imports are always at the top)
import random

# set the secret 1-10
# secret = 5

secret = random.randint(1, 100000)

# ask the user to guess a number
guess = input('Guess a number between 1 and 10: ')

# convert the guess to an integer
guess = int(guess)


if guess == secret:
    print(f'Congratulations! you guess the secret number: {secret}')
    
elif guess < secret:
    print(f'Oops! Your guess of {guess} was too low! The secret number was {secret}...')
    
elif guess > secret:
    print(f'Oops! Your guess of {guess} was too high! The secret number was {secret}...')