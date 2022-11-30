# Unit 2 Practice
# Exercise 2

# create list 
colors = []

# create loop
while True:
    user = input("Enter a color or 'done' to quit: ")
    # set break condition
    if user == 'done':
        print(f"The colors you entered were: {colors}")
        break
    # add user's color to list
    if user not in colors:
        colors.append(user)
        print(f"'{user}' added to the colors list!")
    # prevent adding similar colors
    elif user in colors:
        print(f"Oops! '{user}' is already in the colors list! ")