# Rock Paper Scissors

Let's play rock-paper-scissors with the computer.

1. Greet the user and use a `for` loop to display their possible choices.   

```
Welcome to Rock, Paper, Scissors!

Your options are:

- Rock
- Paper
- Scissors

Enter your selection:  
```

2. The computer will ask the user for their choice (rock, paper, scissors). 
3. The computer will randomly choose rock, paper or scissors.
4. Compare the players' choices and determine who won and tell the user.

NOTE: Do not use index positions during the lab to target any values

## Possible Combinations
| Human | Computer | Winner
|-|-|-|
|rock |rock | Tie
|rock |paper|Computer|
|rock |scissors|Human|
|paper |paper|Tie|
|paper |rock|Human|
|paper |scissors|Computer|
|scissors |scissors|Tie|
|scissors |rock|Computer|
|scissors |paper|Human|

### Lab [Code](/programming_101/code/unit_04/lab-4.py)

## Extra Challenge 1

Catch all tie conditions using a single if conditional.
### Challenge 1 [Code](/programming_101/code/unit_04/lab-4.1.py)
## Extra Challenge 2

Ask the user if they want to play again, using a while loop.
### Challenge 2 [Code](/programming_101/code/unit_05/lab-5.1.py)
## Extra Challenge 3

Use a dictionary where each key is one of the choices, and the value is what the key loses to.
### Challenge 3 [Code](/programming_101/code/unit_05/lab-5.1.py)
[//]: # (instructor note: write the tie case, the first case, have them write the others using elif)