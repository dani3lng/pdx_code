# Unit 3 Practice
# Exercise 2.2

#ask user for a word and letter
user_word = input("Provide a word: ")
user_letter = input("Provide a letter: ")

if user_letter in user_word:
    user_letter = user_letter.upper()
    print(f'The word "{user_word}" contains the letter "{user_letter}".')
else:
    print(f'"{user_letter}" is not found in the word "{user_word}".')