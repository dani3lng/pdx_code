# Unit 4 Practice
# Exercise 5.3

import random

# create lists
number_list = []

# create for loop to populate list
for x in range(1, 10):
    number_list.append(random.randint(1,100))

# display number list
print(f"Numbers: {number_list}")
    
# create loop to sort numbers
# loop: i = 0 -> (length of list - 1)
for i in range(len(number_list) - 1):
    # set 'swap' variable to False
    swap = False
    # loop: j = 0 -> (length of list - 1)
    for j in range(len(number_list) - 1):
        #if list[j] is less than list[j+1]
        if number_list[j] > number_list[j+1]:
            #place list[j] in a 'bubble' variable
            bubble = number_list[j]
            # put list[j+1] at list[j]
            number_list[j] = number_list[j+1]
            # put bubble at list[j+1]
            number_list[j+1] = bubble
            # since a swap occurred this loop,
            # set swap to True
            swap = True
    # if no swap occurred, break the outer loop
    if not swap:
        break

# display sorted number list
print(f"Sorted: {number_list}")