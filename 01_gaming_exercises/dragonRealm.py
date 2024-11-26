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

items = 0
alive = True
waitTime = 4

def displayIntro():
    print("You are lost in the mountains and need somewhere to stay.\n")
    time.sleep(waitTime)
    print("There is shelter in the mountains you can try to stay at for the night since it's cold.\n ")
    time.sleep(waitTime)
    print("However, there is something in there that doesn't seem to like new visitors.\n")
    
def chooseCave():
    shelter = ''
    while shelter != '1' and shelter != '2':
        print('Which shelter will you go into? (1 for endo shelter or 2 for buddha shelter)')
        shelter = input()
    return shelter

def checkCave(shelter):
    if shelter == 1 and hasArrow:
        print("You wander into the endo shelter, it doesn't look dark as it sounds... and barely any people.\n")
        time.sleep(waitTime)
        print("It's an elderly person walking up to you with a smirk.\n")
        time.sleep(waitTime)
        print("He draws his dual katana looking for a fight!\n")
        time.sleep(waitTime)
        print("You defend yourself very well but starts to lose ground until the elderly man stops.\n") 

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














































































































































# Close the file
saveData.write("END OF GAME \n\n")
saveData.close()