# Unit 3 Practice
# Exercise 1.7

import math
import random

# find perimeter of triangle
# a = side x
# b = side y
# c = side z

# assign number to each
a = random.randint(0,100)
b = random.randint(0,100)
c = random.randint(0,100)

# find perimeter
p = a + b + c

# print output
print(f'''
Exercise 1.1
A triangle with sides of {a}, {b}, and {c} has a perimeter of {p}
''')

# find area of triangle
# c = 1/2 * b * h
# h = height 
# b = base

# assign number to each
b = random.randint(0,100)
h = random.randint(0,100)

# find area
a = .5 * h * b

# print output
print(f'''
Exercise 1.2
A triangle with a base of {b} and a height of {h} has an area of {a}
''')

# find circumference and area of a circle
# C = 2 * pi * r or C = pi * d
# A = pi * r^2

# assign number to variables
r = random.randint(0,100)
pi = math.pi

# find circumference
C = 2 * pi * r

# find area
A = pi * r**2

# print output
print(f'''
Exercise 1.3
Circle
Radius: {r}
Circumference: {C}
Area: {A}
''')

# find volume of a sphere
# V = 4/3 * pi * r^3

# assign number to variables
r = random.randint(0,100)
pi = math.pi

# find volume
V = 4/3 * pi * r**3

# print output
print(f'''
Exercise 1.4
Sphere
Radius: {r}
Volume: {V}
''')

# find area of an annulus
# A = π (R2﹣r2)
# R = outer radius
# r = inner radius

# assign number to variables
R = random.randint(0,100)
r = random.randint(0,100)
pi = math.pi

# find volume
A = pi * (R**2 - r**2)

# print output
print(f'''
Exercise 1.5
Annulus
Outer Radius: {R}
Inner Radius: {r}
Area: {A}
''')

# find hypotenuse of a triangle
# c^2 = a^2 + b^2
# c = hypotenuse
# a = height
# b = base

# assign number to variables
a = random.randint(0,100)
b = random.randint(0,100)

# find volume
c = math.sqrt(a**2 + b**2)

# print output
print(f'''
Exercise 1.6
A triangle with sides of {a} and {b} has a hypotenuse of {c}
''')