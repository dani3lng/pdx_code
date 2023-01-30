# Unit 4 Practice
# Exercise 4.3

# ask for info from user
number_1 = int(input('Enter the first number: '))
number_2 = int(input('Enter the second number: '))
number_limit = int(input('Enter how far apart the numbers are allowed to be: '))

# calculate ranges for numbers
uprange = number_2 + number_limit
downrange = number_2 - number_limit

# determine if number is between 10 - 100
if number_1 >= downrange and number_1 <= uprange:
    print(f'{number_1} is within {number_limit} of {number_2}')
else:
    print(f'{number_1} is not within {number_limit} of {number_2}')