# Unit 4 Lab
# Anagram Checker

# ask user for two words
print("This is an Anagram Checker")
word_1 = input("Enter your first word: ")
word_2 = input("Enter your second word: ")

# sort the strings into lists
list_1 =list(word_1)
list_2 = list(word_2)

# sort each list
list_1.sort(reverse=True)
list_2.sort(reverse=True)

# display results
if list_1 == list_2:
    print(f"'{word_1}' and '{word_2}' are anagrams")
else:
    print(f"'{word_1}' and '{word_2}' are not anagrams")