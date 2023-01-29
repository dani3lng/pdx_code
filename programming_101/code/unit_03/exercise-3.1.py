# Unit 3 Practice
# Exercise 3.1

import math

# constants
max_length = 1000


# ask user for number of characters in tweet
character_count = int(input('How many characters are in your Tweet? '))
if character_count <= max_length:
    print('You will only need to create one Twitter post.')
else:
    tweet_number = math.ceil(character_count / max_length)
    print(f'You will need to create {tweet_number} Twitter posts.')