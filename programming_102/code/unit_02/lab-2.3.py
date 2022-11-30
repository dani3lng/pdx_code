# Unit 2 Lab
# List Removal Program

# create remove_all function
def remove_all(numbers, target):
    if target in numbers:
       numbers.remove(target)
       return numbers
    else: 
        print(f'{target} is not in the list')

# initialize number list
number_list = [4, 5, 4, 2, 7, 4, 4, 5, 8, 10]
print(number_list)
# determine target parameter
user = int(input('What number would you like to remove from the list?: '))
print(f'Old Numbers: {number_list}')
print(f'New Numbers: {remove_all(number_list, user)}')