# Unit 4 Practice
# Exercise 3

import random
import statistics

# create list
num_list = []
list_flipped = []
i = 0

# populate number list
while i < 10:
    num_list.append(random.randint(-100, 100))
    i += 1

# switch each number to its opposite sign
for x in num_list:
    x *= -1
    list_flipped.append(x)

# display results
print(f'Numbers: {num_list}')
print(f'Flipped: {list_flipped}')