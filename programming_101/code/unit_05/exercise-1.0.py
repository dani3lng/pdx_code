# Unit 5 Practice
# Exercise 1.1

import random

# set variables 
awake = True
count = 0

# create random variable number
number = random.randint(1,10)

# create while loop
while awake == True:
    count += 1
    print(f'{count} sheep - baa!')
    if count == number:
        print("...zZzZzZzZ...")
        awake = False
    else:
        continue