# Unit 2 Lab
# Sum Calculator Program

# create function 
def sum(numbers):
    #initialize variable for list sum
    total = 0
    # loop to find add all values in list
    for number in numbers:
        total += number    
    return total

# initialize number list
number_list = []
# create number list from user inputs
while True:
    user = input("Enter a number or 'done' to quit: ")
    if user == 'done':
        break
    else:
        number_list.append(int(user)) 
# display information and sum
print(f'You entered {number_list}')
print(f'The sum of the numbers is {sum(number_list)}')