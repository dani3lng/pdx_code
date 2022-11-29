# Unit 2 Practice
# Exercise 1

# create counter variable
loops = 0

# input user answer
user = ''
while True:
    user = input("Again? yes/no: ")
    if user == 'yes':
        loops += 1
        continue
    elif user == 'no':
        print(f'The loop ran {loops} times.')
        break
    else:
        print("You entered an invalid option.")