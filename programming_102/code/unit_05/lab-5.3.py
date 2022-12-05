# Unit 5 Lab
# User Login Extra Challenge

# create profile dictionary
profile = {
    'username': 'gandalfTheGrey',
    'password': 'noneShallPass!',
}

# initialize variables
login_counter = 3

# create login function
def login(username_attempt, password_attempt):
    if username_attempt == profile['username'] and password_attempt == profile['password']:
        return True
    else:
        return False
        
# get username and password from user
while True:
    usr_input = input("Enter your username: ")
    pass_input = input("Enter your password: ")
    usr_result = login(usr_input, pass_input)
    if usr_result == True:
        print('\nSuccessful login!')
        print(f'username: {usr_input}')
        print(f'password: {pass_input}')
        print(f'\nWelcome, {usr_input}')
        break
    elif usr_result == False:
        print('\nUnsuccessful login!')
        print(f'username: {usr_input}')
        print(f'password: {pass_input}')
        print(f'\nError! Your username or password was incorrect!')
        repeat = input('Would you like to try again (yes/no)? ')
        if repeat == 'yes':
            login_counter = login_counter - 1
            if login_counter > 0:
                print(f'You have {login_counter} login attempt(s) remaining...')
                print('\n')
                continue
            else:
                print("Your login has been unsuccessful three times! Try again later. Goodbye!")
                break
        if repeat == 'no':
            break