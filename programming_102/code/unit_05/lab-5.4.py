# Unit 5 Lab
# User Login Extra Challenge

# create list for profiles and profile dictionaries
list_profile = []
dict_profile = {
    'name': '',
    'username': '',
    'password': '',
}

# initialize variables
login_counter = 3

# create function for creating profiles
def user_data(name, usr_input, pass_input):
    dict_profile.update({'name': name})
    dict_profile.update({'username': usr_input})
    dict_profile.update({'password': pass_input})
    list_profile.append(dict_profile)
    
# create function for login
def login(name, username_attempt, password_attempt):
    if username_attempt == dict_profile['username'] and password_attempt == dict_profile['password'] and name == dict_profile['name']:
        return True
    else:
        return False
        
# get username and password from user
new_profiles = int(input('How many profiles would you like to create? '))
for x in range(new_profiles):
    print('''
Account Details
---------------''')
    name = input("Name: ")
    usr_input = input("Username: ")
    pass_input = input("Password: ")
    user_data(name, usr_input, pass_input)
while True:
    print('''
Login Screen
------------''')
    name = input("Name: ")
    if name in dict_profile['name']:
        print(f'Hello {name}!')
        usr_input = input("Username: ")
        pass_input = input("Password: ")
        usr_result =login(name, usr_input, pass_input)
        if usr_result == True:
            print('\nSuccessful login!')
            print(f'username: {usr_input}')
            print(f'password: {pass_input}')
            print(f'\nWelcome back, {name}')
            break    
        else:
            print('\nUnsuccessful login!')
            print(f'username: {usr_input}')
            print(f'password: {pass_input}')
            print(f'\nError! Your username or password was incorrect!')
            repeat = input('Would you like to try again (y/n)? ')
            if repeat == 'y':
                login_counter = login_counter - 1
                if login_counter > 0:
                    print(f'You have {login_counter} login attempt(s) remaining...')
                    print('\n')
                    continue
                else:
                    print("Your login has been unsuccessful three times! Try again later. Goodbye!")
                    break
            else:
                break
    else:
        print("You do not have an account with us. Please create an account first.")
        break