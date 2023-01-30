# Unit 4 Practice
# Exercise 4.2

# ask for number from user
number_1 = int(input('Please enter an integer: '))
number_2 = int(input('Please enter an integer: '))

# calculate ranges for numbers
uprange = number_2 + 10
downrange = number_2 - 10

# determine if number is between 10 - 100
if number_1 >= downrange and number_1 <= uprange:
    print(f'{number_1} is within 10 of {number_2}')
else:
    print(f'{number_1} is not within 10 of {number_2}')