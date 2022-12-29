# Unit 4 Practice
# Exercise 5.2

import random

# create lists
number_list = []
reverse_list = []

# create for loop to populate list
for x in range(1, 10):
    number_list.append(random.randint(1,100))
    
# create loop to reverse numbers
list_length = len(number_list)
for index in range(list_length -1, -1, -1):
    number = number_list[index]
    reverse_list.append(number)
    
# display lists
print(f"Numbers: {number_list}")
print(f"Reversed: {reverse_list}")