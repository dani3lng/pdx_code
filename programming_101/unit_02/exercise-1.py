# Unit 2 Practice
# Exercise 1

# ask user to enter mailing address
street = input("Enter your street: ")
city = input("Enter the city you reside in: ")
state = input("What state do you reside in: ")
zip_code = input("Enter your zip code: ")

print(f'''
Your address is:
----------------
{street.title()}
{city.title()}, {state.title()}
{zip_code}
''')