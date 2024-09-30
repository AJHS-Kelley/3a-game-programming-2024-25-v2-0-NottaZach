# rock, Paper, Scissors by Zachariah Thomas, v0.1

# MODULE IMPORTS
import random, time

# DATA STRUCTURES -- PLAYER
playerScore = 0 
playerChoice = None
numDraws = 0 
# DATA STRUCTURES -- CPU
cpuScore = 0
cpuChoice = None


# MAIN GAME LOOP
while playerScore < 5 and cpuScore < 5:
   
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
    print(f"CPU choice:{cpuChoice}")
    # let PLAYER select choice at random.
    playerChoice = random.randint(0, 2) # randomly select 0, 1, or 2.  
    if playerChoice == 0:
        playerChoice = "rock"
    elif playerChoice == 1:
        playerChoice = "paper"
    elif playerChoice == 2:
        playerChoice = "scissors"
    else:
        print("Unable to dtermined CPU choice.\n Please restart.\n")
        exit()
    # compare player choice to cpu choice
    if playerChoice == "rock" and cpuChoice == "paper":
        print(f" The cpu chose {cpuChoice} and you chose {playerChoice}. \n")
        print("The CPU wins a point.\n")
        cpuScore += 1
        # CPU wins
    elif playerChoice == "rock" and cpuChoice == "scissors":
        print(f" The cpu chose {cpuChoice} and you chose {playerChoice}. \n")
        print("You win a point.\n")
        playerScore += 1
        #Player wins
    elif playerChoice == "rock" and cpuChoice == "rock":
        print(f" The cpu chose {cpuChoice} and you chose {playerChoice}. \n")
        print(" It's a draw!\n")
        #Draw
    elif playerChoice == "scissors" and cpuChoice == "paper":
        #Player wins
        print(f" The cpu chose {cpuChoice} and you chose {playerChoice}. \n")
        print("You win a point.\n")
        playerScore += 1
    elif playerChoice == "scissors" and cpuChoice == "rock":
        # Cpu wins
        print(f" The cpu chose {cpuChoice} and you chose {playerChoice}. \n")
        print("The CPU wins a point.\n")
        cpuScore += 1
    elif playerChoice == "scissors" and cpuChoice == "scissors":
        #Draw
        print(f" The cpu chose {cpuChoice} and you chose {playerChoice}. \n")
        print(" It's a draw!\n")
    elif playerChoice == "paper" and cpuChoice == "rock" : 
        #Player wins
        print(f" The cpu chose {cpuChoice} and you chose {playerChoice}. \n")
        print("You win a point.\n")
        playerScore += 1
    elif playerChoice == "paper" and cpuChoice == "scissor" :
        # Cpu wins
        print(f" The cpu chose {cpuChoice} and you chose {playerChoice}. \n")
        print("The CPU wins a point.\n")
        cpuScore += 1
    elif playerChoice == "paper" and cpuChoice == "paper" :
        #Draw
        print(f" The cpu chose {cpuChoice} and you chose {playerChoice}. \n")
        print(" It's a draw!\n")

    else:
        print("Unable to determine a winner. Please restart .\n")
        exit()
    # print the results to the screen
    # award points to winner and output results





