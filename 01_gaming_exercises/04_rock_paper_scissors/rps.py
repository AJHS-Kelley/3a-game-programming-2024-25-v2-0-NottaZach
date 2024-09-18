# rock, Paper, Scissors by Zachariah Thomas, v0.1

# MODULE IMPORTS
import random

# DATA STRUCTURES -- PLAYER
playerScore = 0 
playerName = "Test Player"
playerChoice = None

# DATA STRUCTURES -- CPU
cpuScore = 0
cpuChoice = None

# PLAYER NAME INPUT
playerName = input("Type your name and press enter. \n")
print(f"Hello{playerName}!\n")
isCorrect = input("Is that correct? Type yes or no and press enter.\n").lower()
print("isCorrect")
# .lower() can turn ALL input into lowercase
# .upper() can turn ALL input into UPPERCASE

if isCorrect == "yes":
   print(f"Ok {playerName}, let's play Rock, Paper, Scissors!\n")
else:
    playerName = input("Type your name and press enter. \n")

# THE RULES using MULTI-LINE strings
print("""
Welcome to Rock, Paper, Scissors Robot!
Its to time play RPS!

You will play Against the CPU. The first to 5 points wins.
You will select from ROCK, PAPER, SCISSORS.     
The CPU will select ROCK, PAPER, SCISSORS at random.
      
 1) Rock beats Scissors     
 2) Scissors beats Paper  
 3) Paper beats Rock     
""")

# MULTI-LINE STRINGS CAN BE USED AS BIG COMMENTS






# MAIN GAME LOOP
while playerScore < 5 and cpuScore < 5:
    print(f"{playerName} you have {playerScore} points.\n The CPU has {cpuScore} points.\n")
    playerChoice = input( " Please enter rock, paper, or scissors and press enter.\n").lower()
    if playerChoice != "rock" or playerChoice != "paper" or playerChoice != "scissors":
        playerChoice = input( " Please enter rock, paper, or scissors and press enter.\n").lower() 
        if playerChoice!= "rock" or playerChoice != "paper" or playerChoice != "scissors": 
            print(" You are not following my rules. please try again. \n")
            exit()
        print(f"You have chosen{playerChoice}.\n")
    else:
        print(f"You have chosen{playerChoice}.\n")
    # let player select rock, paper, 
    # let cpu select choice at random.
    # compare player choice to cpu choice
    # print the results to the screen
    # award points to winner and output results





