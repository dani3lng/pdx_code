# Unit 2 Lab
# Mab Lib Program

# create MabLib text
'''
I am traveling to {place} where it is {temp} degrees.
I packed the following items for the trip:
- A {adj_1} {item_1}
- A {adj_2} {item_2}
- A {adj_3} {item_3}
'''

# ask user for inputs
adj_1 = input("Enter a color: ")
adj_2 = input("Enter a size: ")
adj_3 = input("Enter an adjective: ")
temp = input("Enter an temperature: ")
item_1 = input("Enter an item: ")
item_2 = input("Enter an item: ")
item_3 = input("Enter an item: ")
item_4 = input("Enter an item: ")
place = input("Enter in a destination: ")

# insert user inputs into MabLib
print(f'''
I am traveling to {place} where it is {temp} degrees.
I packed the following items for the trip:
- A {adj_1} {item_1}
- A {adj_2} {item_2}
- A {adj_3} {item_3}
''')