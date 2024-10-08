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
loopCount = 0
loopsReq = int(input(" How many loops do you want?\nEnter an integer, no commas, and press ENTER.\n"))
# req is the universal abbreviation in computer programming for REQUEST. reqs =  REQUESTS
rpsTimeStart = time.time() # returns the number of seconds since Jan. 01, 1970 @ 12:00AM
while loopCount < loopsReq:
   
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
    print(f"player choice:{playerChoice}")
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
        numDraws += 1
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
        numDraws += 1
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
        numDraws += 1

    loopCount += 1

print(f" Your final score: {playerScore}\nCPU Final Score: {cpuScore}\nDraws: {numDraws}\n")
if playerScore> cpuScore:
    print(f" Congratulations. You are the winner!\n")
elif cpuScore> playerScore:
    print(f"Womp Womp, the cpu wins.\n")
else:
    print("Unable to determine a winner.\nPlease restart.\n")
    exit()




rpsTimeStop = time.time()
rpsTime = rpsTimeStop - rpsTimeStart
print(f" Number of Loops: {loopCount}\n")
print(f"Execution Time {rpsTime: .2F} seconds.\n")






