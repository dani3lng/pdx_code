# Unit 3 Lab
# Unit Converter Version 3

# create dictionary
unit_converter = {
    'feet': 0.3048,
    'mile': 1609.34,
    'meter': 1,
    'kilometer': 1000,
    'yard': 0.9144,
    'inch': 0.0254,
}

# ask user for unit
urs_unit = input('''
What unit would you like to convert from? 
(feet, mile, meter, kilometer, yard, inch)
> ''')

# ask user to distance
usr_distance = input('\nWhat is the distance? ')

# create conversion calculator
meter = unit_converter[urs_unit] * int(usr_distance)

# display results
print(f"\n{usr_distance} {urs_unit} is equal to {round(meter, 2)} meters")