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
     
