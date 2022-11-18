# Unit 3 Lab
# Grade Converter Program

# 90-100: A
# 80-89: B
# 70-79: C
# 60-69: D
# 0-59: F

# ask user to input number score (0 - 100)
num_score = int(input("Enter your numerical score: "))

# create comparison 
if num_score >= 90 and num_score <= 100:
    letter_score = 'A'
elif num_score >= 80 and num_score <= 89:
    letter_score = 'B'
elif num_score >= 70 and num_score <= 79:
    letter_score = 'C'
elif num_score >= 60 and num_score <= 69:
    letter_score = 'D'
elif num_score >= 0 and num_score <= 59:
    letter_score = 'F'

# print results
print(f'Your number grade of {num_score} gives you a letter grade of {letter_score}')