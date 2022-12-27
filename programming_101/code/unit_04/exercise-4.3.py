# Unit 4 Practice
# Exercise 4.2

# create lists
input_list = []
char_list = []

# create for loop to get user inputs
for x in range(3):
    user_input = input('Provide the name of three items: ')
    input_list.append(user_input)

# create loop to get letters
for word in input_list:
    print(word)
    for x in word:
        print(x)
        if x not in char_list:
            char_list.append(x)
        else:
            continue
        
# display character list
print(char_list)