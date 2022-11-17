# Unit 2 Practice
# Exercise 2

# use string methods to determine number of times a letter occurs in a word
'''
word: bookkeeper
letter: k
'''

word = 'bookkeeper'.count('k')
print(f"The letter 'k' occurs in the word 'bookkeeper' {word} times.")

# ask user for word
word = input("Enter a word: ")
letter = input("Enter a letter: ")
count = word.count(letter)

print(f"The letter {letter} occurs in the word {word} {count} times.")