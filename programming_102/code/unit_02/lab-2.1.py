# Unit 2 Lab
# Building sum() function

# create function 
def sum(numbers):
    #initialize variable for list sum
    total = 0
    # display list
    print(f'Numbers: {numbers}')
    # loop to find add all values in list
    for number in numbers:
        total += number    
    # display the sum
    print(f'Sum: {total}')

# create number list 
num_input = [4, 5, 4, 2, 7, 4, 4, 5, 8, 10]
# call sum function
sum(num_input)