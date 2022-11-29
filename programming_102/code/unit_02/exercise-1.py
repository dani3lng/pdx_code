# Unit 2 Practice
# Exercise 1

# initialize variables
loops = 0
user = ''

#create loop
while True:
    user = input("Again? yes/no: ")
    # set loop condition
    if user == 'yes':
        loops += 1
        continue
    # end loop condition
    elif user == 'no':
        print(f'The loop ran {loops} times.')
        break
    else:
        print("You entered an invalid option.")