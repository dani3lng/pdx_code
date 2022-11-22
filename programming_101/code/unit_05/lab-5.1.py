# Unit 5 Lab Extra Challenge 1
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

# have user determine password length
user = int(input("Enter the desire password length: "))

# create while loop
while len(password_list) < user:
    generator = random.choice(characters)
    password_list.append(generator)

# display password
password = ''.join(password_list)
print(f'Your password: {password}')