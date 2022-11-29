# Unit 1 Practice
# Exercise 2

# find error
# if num < 3                                  ############## "num" is not defined                                       
                                                ############## Expected ":"
#     print('The number is ' + num)             ############## TypeError: can only concatenate str (not "int") to str   
#     print(f'{num is less than three')        ############## Unterminated expression in f-string; missing close brace
#         prin('thanks for playing!")        ############## SyntaxError: unterminated string literal                    
#                                             ############## "prin" is not defined
#                                             ############## Unexpected indentation
             
# corrected
num = 1
if num < 3:
    print('The number is ' + str(num))
    print(f'{num} is less than three')
    print("Thanks for playing!")        