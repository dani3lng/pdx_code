# Unit 3 Lab
# Unit Converter Version 1

# create dictionary
converto_meter = {
    'feet': 0.3048
}

# ask user to distance
user = input('What is the distance in feet? ')

# create conversion calculator
meter = converto_meter['feet'] * int(user)

# display results
print(f"{user} ft is equal to {round(meter, 4)} m")