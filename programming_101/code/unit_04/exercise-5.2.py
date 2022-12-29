# Unit 4 Practice
# Exercise 5.2

import random

# create lists
number_list = []
even_list = []

# create for loop to populate list
for x in range(1, 10):
    number_list.append(random.randint(1,100))
    
# create loop to find even numbers
even_count = 0
for number in number_list:
    x = number % 2
    if x == 0:
        even_list.append(number)
        even_count += 1
    else:
        continue
        
# display lists
print(f"Numbers: {number_list}")
print(f"There are {even_count} evens: {even_list} ")