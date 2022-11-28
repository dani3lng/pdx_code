# Unit 3 Practice
# Exercise 2.4

import string # string  module

#ask user for a word and letter
user_word = input("Provide a word: ")
user_word = user_word.isalpha()

# provide results
if user_word == True:
    print(f"Your input is valid.")
else:
    print(f"Your input is invalid.")