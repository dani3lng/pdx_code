# Unit 4 Practice
# Exercise 2.2

import random
import math

# create list
num_list = []
i = 0

# populate number list
while i < 10:
    num_list.append(random.randint(1, 10))
    i += 1

# find mean
list_mean = sum(num_list) / 10

# display results
print(f'Numbers: {num_list}')
print(f'Mean: {list_mean}')