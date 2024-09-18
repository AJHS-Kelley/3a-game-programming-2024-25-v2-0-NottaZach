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
if isCorrect == "yes":
   print(f"Ok {playerName}, let's play Rock, Paper, Scissors!\n")
else:
    playerName = input("Type your name and press enter. \n")























