# Dragon Realm, Zachariah Thomas, v0.0
# Based on https://inventwithpython.com/chapter6.html by Al Sweigart
# 

import random
import time
import datetime

# SAVING DATA TO A FILE
# STEP 1-- Create the file name to use.
logFileName = "dragonRealmLog" + str(time.time()) + ".txt"
# Example : dragonRealmLog1132AM.txt

#STEP 2 -- Create / open the file to save the data.
saveData = open(logFileName,"x")
# file modes
# "x" CREATES FILE, IF FILE EXISTS, EXIT WITH ERROR MESSAGE
# "W" REATES FILE, IF FILE EXITS, ERASE AND OVERWRITE FILE CONTENTS
# "A" CREATES FILE, IF FILE EXISTS, APPEND DATA TO THE FILE

saveData.write("GAME STARTED" + " "+ str(datetime.datetime.now()) + "\n")
def displayIntro():

    print('You are in a land full of dragons. In front of you,')
    print('you see two caves. In one cave, the dragon is friendly')
    print('and will share his treasure with you. The other dragon')
    print('is greedy and hungry, and will eat you on sight.')
    print()

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('Which cave will you go into? (1 or 2)')
        cave = input()
    return cave

def checkCave(chosenCave):
    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
        print('Gives you his treasure!')

    else:
        print('Gobbles you down in one bite!')



playAgain = 'yes'

while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)
    print('Do you want to play again? (yes or no)')
    playAgain = input()



    hasCannonLauncher = False
    damage = random.randint (1,8)
    pickUpItem = input("You see a beautiful CannonLauncher right next to some to a broken sword. Do you have the guts to pick it up? Type yes or no, then press enter.\n ").lower()
    if pickUpItem == "yes":
        hasCannonLauncher = True

    # Remove this code, we are not doing to track amounts of damage for this project.  It will make it too complicated.  
    if hasCannonLauncher:
        damage += 35









































































































































# Close the file
saveData.write("END OF GAME \n\n")
saveData.close()