# Unit 4 Lab
# Anagram Checker Extra Challenge 1

# ask user for two words
print("This is an Anagram Checker")
word_1 = input("Enter your first word: ").lower()
word_2 = input("Enter your second word: ").lower()

# sort the strings into lists
list_1 = list(word_1)
list_2 = list(word_2)

# sort each list
list_1.sort()
list_2.sort()

# create while loop to remove spaces
space = ' '
for letter in list_1:
    if space == letter:
        list_1.remove(letter)
for letter in list_2:
    if space == letter:
        list_2.remove(letter)

# display results
if list_1 == list_2:
    print(f"'{word_1}' and '{word_2}' are anagrams")
else:
    print(f"'{word_1}' and '{word_2}' are not anagrams")