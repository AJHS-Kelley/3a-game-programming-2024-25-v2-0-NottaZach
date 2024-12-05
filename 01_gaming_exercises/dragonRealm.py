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
    if shelter == 1 and hasSword:
        print("You wander into the endo shelter, it doesn't look dark as it sounds... and barely any people.\n")
        time.sleep(waitTime)
        print("It's an elderly person walking up to you with a smirk.\n")
        time.sleep(waitTime)
        print("He draws his dual katana looking for a fight!\n")
        time.sleep(waitTime)
        print("You defend yourself very well but starts to lose ground until the elderly man stops.\n")
        time.sleep(waitTime)
        print("As the elderly man stops, he starts fading away.\n")
    elif shelter == 1 and hasShield:
        print(" You wander more in the endo shelter, and still little to no people.\n")
        time.sleep(waitTime)
        print("Some strange noise got your attention, as if it was another person with a weapon.\n")
        time.sleep(waitTime)
        print("You see another person charge at you with a weapon but you blocked the attack.\n")
        time.sleep(waitTime)
        print("Another person come charging at you while you was blocking the first attack and you are getting stab.\n")
        time.sleep(waitTime)
        print("You passes out and died from all the blood loss.\n")
        alive = False
        return alive
    elif shelter ==2 and hasShield:
        print("You wander into the buddha shelter, it is very charming and bright.\n")
        time.sleep(waitTime)
        print("The owner of the shelter looks at you with a estactic face.\n")
        time.sleep(waitTime)
        print("He greets you and says if you want to stay you have beat one of my greatest disciple.\n")
        time.sleep(waitTime)
        print("The owner disciple spiritual pressure shocks you leaving you stunned but your shield resist the pressure.\n")
        time.sleep(waitTime)
        print("You blocked the disciiple finger which no one has ever done.\n")
        time.sleep(waitTime)
        print("The owner tell you that you earn his respect.\n")
        time.sleep(waitTime)
        print("Time to get some rest now.\n")
    elif shelter == '2' and hasSword:
        print("You wander into the buddha shelter, it is very charming and bright.\n")
        time.sleep(waitTime)
        print("The owner of the shelter looks at you with a estactic face.\n")
        time.sleep(waitTime)
        print("He greets you and says if you want to stay you have beat one of my greatest disciple.\n")
        time.sleep(waitTime)
        print(" The owner disciple spiritual pressure shocks you leaving you stunned.\n")
        time.sleep(waitTime)
        print("The disciple touches you with a single finger and erase you from existence.\n")
        alive = False
        return alive
    





    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
        print('Gives you his treasure!')

    else:
        print('Gobbles you down in one bite!')



playAgain = 'yes'

while playAgain == 'yes' or playAgain == 'y':
    waitTime = int(input("Please input how many seconds would you like for the text to to wait. Enter 1-4.\n"))
    print("Please select your weapon, 1 for sword or 2 for shield.\n")
    weapon = input().lower
    if weapon == 1:
        hasSword = True
    elif weapon == 2:
        hasShield = True
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)
    print('Do you want to play again? (yes or no)')
    playAgain = input()














































































































































# Close the file
saveData.write("END OF GAME \n\n")
saveData.close()