# Functions Practice, Zachariah Thomas, v0.0

import random

def helloWorldMulti(): #FUNCTION SUGNATURE
    """This function will output Hello, World! in a language the user""" # DOCSTRING \
    # print a list of languages to the screen, at least three but no more than five.
    print("Hello, World! We have 3 language that you can choose.\n")
   
    print("[S]panish.\n")
   
    print("[E]nglish.\n")
   
    print("[F]rench.\n")

    # allow the user to select (input) a choice for the language.
    language = input("What language do you want?\n Please type the first letter of the language you want.\n").lower()

    # print "Hello, World!" to the sreen in that language.

    if language == "s":
        print(" In Spanish:\nHalo, Mundo!\n")
    elif language == "e":
        print("In English:\nHello, World!\n")
    else:
        print("In French:\nBon jour, Le Monde!")

helloWorldMulti() # FUNCTION CALL

#Function to Determine Even / Odd numbers
argument1 = random.randint(-1000, 1000)

def isEven( argument1: int) -> bool:
    """Determines if integer value is even or odd."""
    if argument1 % 2 == 0:
        return True
    else:
        return False
    
print(isEven(argument1))

# Function with Multiple Arguments
def canRideRollerCoaster(age: int, height: int) -> bool:
    if age >10 and height > 4:
        print("You can ride.\n")
        return True
    else:
        print("You cannot ride.\n")
        return False
    
canRideRollerCoaster(4,10) # Arguments must be passed in the same order as the fsi.