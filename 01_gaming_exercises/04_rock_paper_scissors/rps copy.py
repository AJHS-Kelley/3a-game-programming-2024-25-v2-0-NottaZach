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
def playerName(): # Function signature -- name of function, (arguments if any)
    """ Gets the name from the player and returns it."""
    # The line above is a DOCSRTING,  it gives a brief example of what the function does.
    playerName = input("Type your name and press enter. \n")
    print(f"Hello{playerName}!\n")
    isCorrect = input("Is that correct? Type yes or no and press enter.\n").lower()
    if isCorrect == "yes":
        print(f"Ok {playerName}, let's play Rock, Paper, Scissors!\n")
    else:
        playerName = input("Type your name and press enter. \n")
    return playerName 
    

# CALLING THE FUNCTIONS
playerName = playerName()

# THE RULES using MULTI-LINE strings
def rules() -> None:
    """This function prints the rules for rock, paper, scissors."""
    print(f"""
    Welcome, {playerName} to Rock, Paper, Scissors Robot!
    Its to time play RPS!

    You will play Against the CPU. The first to 5 points wins.
    You will select from ROCK, PAPER, SCISSORS.     
    The CPU will select ROCK, PAPER, SCISSORS at random.
      
    1) Rock beats Scissors     
    2) Scissors beats Paper  
    3) Paper beats Rock     
    """)
    #Does another part of this program need to access this information?


def playerChoice() -> str:
    """Allows the plaeyer to chose rock, paper, scissors."""
    playerChoice = input( " Please enter rock, paper, or scissors and press enter.\n").lower()
    if playerChoice != "rock" and playerChoice != "paper" and playerChoice != "scissors":
        playerChoice = input( " Please enter rock, paper, or scissors and press enter.\n").lower() 
        if playerChoice != "rock" and playerChoice != "paper" and playerChoice != "scissors": 
            print(" You are not following my rules. please try again. \n")
            exit()
        print(f"You have chosen{playerChoice}.\n")
    else:
        print(f"You have chosen{playerChoice}.\n")
    return playerChoice
    
def cpuChoice() -> str:
    """Allows the cpu to choose rock, paper, scissors."""
    cpuChoice = random.randint(0, 2) # randomly select 0, 1, or 2.  
    if cpuChoice == 0:
        cpuChoice = "rock"
    elif cpuChoice == 1:
        cpuChoice = "paper"
    elif cpuChoice == 2:
        cpuChoice = "scissors"
    else:
        print("Unable to dtermined CPU choice.\n Please restart.\n")
        exit()
    return cpuChoice

def picWinner(playerChoice: str, cpuChoice: str) -> str: # playerChoice and cpuChoice are both arguments,  tjey will be string values.
    """this function uses the player choice and CPU choice to determine a winner."""
    if playerChoice == "rock" and cpuChoice == "paper":
        print(f" The cpu chose {cpuChoice} and you chose {playerChoice}. \n")
        print("The CPU wins a point.\n")
        cpuScore += 1
        return "CPU Wins"
        # CPU wins
    elif playerChoice == "rock" and cpuChoice == "scissors":
        print(f" The cpu chose {cpuChoice} and you chose {playerChoice}. \n")
        print("You win a point.\n")
        playerScore += 1
        return " Player wins"
        #Player wins
    elif playerChoice == "rock" and cpuChoice == "rock":
        print(f" The cpu chose {cpuChoice} and you chose {playerChoice}. \n")
        print(" It's a draw!\n")
        return "Draw"
        #Draw
    elif playerChoice == "scissors" and cpuChoice == "paper":
        #Player wins
        print(f" The cpu chose {cpuChoice} and you chose {playerChoice}. \n")
        print("You win a point.\n")
        playerScore += 1
        return " Player wins"
    elif playerChoice == "scissors" and cpuChoice == "rock":
        # Cpu wins
        print(f" The cpu chose {cpuChoice} and you chose {playerChoice}. \n")
        print("The CPU wins a point.\n")
        cpuScore += 1
        return "CPU Wins"
    elif playerChoice == "scissors" and cpuChoice == "scissors":
        #Draw
        print(f" The cpu chose {cpuChoice} and you chose {playerChoice}. \n")
        print(" It's a draw!\n")
        return "Draw"
    elif playerChoice == "paper" and cpuChoice == "rock" : 
        #Player wins
        print(f" The cpu chose {cpuChoice} and you chose {playerChoice}. \n")
        print("You win a point.\n")
        playerScore += 1
        return " Player wins"
    elif playerChoice == "paper" and cpuChoice == "scissor" :
        # Cpu wins
        print(f" The cpu chose {cpuChoice} and you chose {playerChoice}. \n")
        print("The CPU wins a point.\n")
        cpuScore += 1
        return "CPU Wins"
    elif playerChoice == "paper" and cpuChoice == "paper" :
        #Draw
        print(f" The cpu chose {cpuChoice} and you chose {playerChoice}. \n")
        print(" It's a draw!\n")
        return "Draw"

    else:
        print("Unable to determine a winner. Please restart .\n")
        exit()
        # return statements IMMEDIATELY exit a function.

# Main game loop
while playerScore< 5 and cpuScore < 5:
    print(f"{playerName} you have {playerScore} points.\nThe CPU has {cpuScore} pints.\n")


    #let cpu select choice at random

    # print(f"CPU Choice: {cpuChoice}")

    # compare player choice to cpu choice
   




