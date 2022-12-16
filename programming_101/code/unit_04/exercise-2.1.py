# Unit 4 Practice
# Exercise 2.1

import random
import math

# create list
num_list = []
i = 0

# populate number list
while i < 10:
    num_list.append(random.randint(1, 10))
    i += 1

# find sum
list_sum = sum(num_list)

# display results
print(f'Numbers: {num_list}')
print(f'Sum: {list_sum}')