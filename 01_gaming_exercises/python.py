import random

def guessing_game():
    number = random.randint(1,100)
    tries = 0
    while True:
        tries+= 1
        guess = int(input("Guess a number between 1 and 100:"))
        if guess < number:
            print("Too low")
        elif guess > number:
            print("Too high")
        else:
            print("Congratulations! You guessed the number in {tries} tries.")
            break
guessing_game()