# Unit 4 Practice
# Exercise 2.2

import random
import statistics

# create list
num_list = []
i = 0

# populate number list
while i < 20:
    num_list.append(random.randint(1, 10))
    i += 1

# find mode
list_mode = statistics.mode(num_list)
mode_count = num_list.count(list_mode)

# display results
print(f'Numbers: {num_list}')
print(f'Mode: {list_mode}')
print(f'The number {list_mode} appears {mode_count} times')