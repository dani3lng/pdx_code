# Unit 5 Lab
# User Login

# create profile dictionary
profile = {
    'username': 'gandalfTheGrey',
    'password': 'noneShallPass!',
}

# create login function
def login(username_attempt, password_attempt):
    if username_attempt == profile['username'] and password_attempt == profile['password']:
        return True
    else:
        return False
        
# get username and password from user
usr_input = input("Enter your username: ")
pass_input = input("Enter your password: ")
usr_result = login(usr_input, pass_input)
if usr_result == True:
    print('\nSuccessful login!')
    print(f'username: {usr_input}')
    print(f'password: {pass_input}')
    print(f'\nWelcome, {usr_input}')
elif usr_result == False:
    print('\nUnsuccessful login!')
    print(f'username: {usr_input}')
    print(f'password: {pass_input}')
    print(f'\nError! Your username or password was incorrect!')