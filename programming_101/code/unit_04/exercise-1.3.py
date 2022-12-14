# Unit 4 Practice
# Exercise 1.3

# create list
old_list = [3, 3, 10, 5, 4, 5, 6, 5, 7, 2]
new_list = []

# change value of each number to square of itself
for x in old_list:
    x **= 2
    new_list.append(x)
    
# display new list
print(new_list)