# Unit 4 Lab
# Rock Paper Scissors Program

import random

# paper > rock
# rock > scissors
# scissors > paper

# establish moves
moves = ['Rock', 'Paper', 'Scissors']

# welcome user to game
print(f'''Welcome to Rock, Paper, Scissors!
      
Your options are:''')

# use for loop to display possible choices
for move in moves:
    print(f'- {move}')
print(" ")

# ask player for move
player = input("Enter your move: ")
player = player.title()
print(f'''
You chose {player}''')

# have computer choose move
computer = random.choice(moves)
computer = computer.title()
print(f'''Computer chose {computer}
''')

# compare results
if player == computer:
    print("You tied")
    
if player == 'Rock' and computer == 'Paper':
    print("You lost")
if player == 'Rock' and computer == 'Scissors':
    print("You won")
    
if player == 'Paper' and computer == 'Rock':
    print("You won")
if player == 'Paper' and computer == 'Scissors':
    print("You lost")
    
if player == 'Scissors' and computer == 'Rock':
    print("You lost")
if player == 'Scissors' and computer == 'Paper':
    print("You won")