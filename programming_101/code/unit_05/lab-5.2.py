# Unit 5 Lab Extra Challenge 2
# Password Generator Program

import random
import string

# list for password
password_list = []
num_letters = []
num_numbers =[]
num_symbols = []

# create lists for characters
letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation
characters = letters + numbers + symbols

# have user determine password length
in_letters = int(input("Enter the desire amount of letters: "))
in_numbers = int(input("Enter the desire amount of numbers: "))
in_symbols = int(input("Enter the desire amount of punctuation: "))

# create a while loop
while len(num_letters) < in_letters:
    letter_gen = random.choice(letters)
    num_letters.append(letter_gen)
while len(num_numbers) < in_numbers:
    number_gen = random.choice(numbers)
    num_numbers.append(number_gen)
while len(num_symbols) < in_symbols:
    symbol_gen = random.choice(symbols)
    num_symbols.append(symbol_gen)
password_list = num_letters + num_numbers + num_symbols

# display password
random.shuffle(password_list)
password = ''.join(password_list)
print(f'Your password: {password}')