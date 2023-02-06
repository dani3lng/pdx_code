# Unit 5 Practice
# Exercise 2.1

# initialize list
number_list = []

# set variables
x = 0
y = 0

# populate list
list_length = len(number_list)
for x in range(1, 101):
    number_list.append(x)

# create while loop
for x in number_list:
    y += 1
    if y % 15 == 0:
        print(f"{x}: FizzBuzz")
    elif y % 3 == 0:
        print(f"{x}: Fizz")
    elif y % 5 == 0:
        print(f"{x}: Buzz")
    else:
        print(f"{x}: {y}")