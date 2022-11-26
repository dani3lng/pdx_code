# Unit 2 Lab Extra Challenge 1
# Mab Lib Program

# create MabLib text
'''
I am traveling to {place} where it is {temp} degrees.
I packed the following items for the trip:
- A {adj_1} {item_1}
- A {adj_2} {item_2}
- A {adj_3} {item_3}
'''
# get while loop requirements
play_again = "y"
while play_again == 'y':
    # ask user for inputs
    adj_1 = input("Enter a color: ")
    adj_2 = input("Enter a size: ")
    adj_3 = input("Enter an adjective: ")
    temp = input("Enter an temperature: ")
    item_1 = input("Enter an item: ")
    item_2 = input("Enter an item: ")
    item_3 = input("Enter an item: ")
    place = input("Enter in a destination: ")

    # insert user inputs into MabLib
    print(f'''
    I am traveling to {place} where it is {temp} degrees.
    I packed the following items for the trip:
    - A {adj_1} {item_1}
    - A {adj_2} {item_2}
    - A {adj_3} {item_3}
    ''')
    # get while loop requirements
    play_again = input("Would you like to play: (y/n) ")
    if play_again == 'y':
        continue
    if play_again == 'n':
        print(f'Thank you for playing Mab Libs')
        break
    else:
        print(f'You entered an invalid option')
        play_again = input("Would you like to play: (y/n) ")