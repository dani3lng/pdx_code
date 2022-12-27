# Unit 4 Practice
# Exercise 4.2

# create list for user inputs
input_list = []

# create for loop to get user inputs
for x in range(3):
    user_input = input('Provide the name of three items: ')
    input_list.append(user_input)

# create loop to display word and letters
for word in input_list:
    print(word)
    for x in word:
        print(x)