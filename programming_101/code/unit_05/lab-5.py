# Unit 5 Lab
# Password Generator Program

import random
import string

# list for password
password_list = []

# create lists for characters
letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation
characters = letters + numbers + symbols

# create while loop
while len(password_list) < 10:
    generator = random.choice(characters)
    password_list.append(generator)

# display password
password = ''.join(password_list)
print(f'Your password: {password}')