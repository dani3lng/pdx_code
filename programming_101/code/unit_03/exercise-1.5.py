# Unit 3 Practice
# Exercise 1.5

import math

# find area of an annulus
# A = π (R2﹣r2)
# R = outer radius
# r = inner radius

# assign number to variables
R = 5
r = 3 
pi = math.pi

# find volume
A = pi * (R**2 - r**2)

# print output
print(f'''
Annulus

Outer Radius: {R}
Inner Radius: {r}
Area: {A}
''')