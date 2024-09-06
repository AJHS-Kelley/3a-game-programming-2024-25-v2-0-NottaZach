# Loops, Zachariah Thomas, v0.0
import random # import the random module for us yo use
# generally put 

# Two type of loops
# for <-- Used when you know how many loops you'll need
# while <-- used when you do not know how many loops you'll need

# for loop is like Go fish, you search each card for what the player asked
# while loop is like musical chairs, you move around till the music stops

# each trip through the entire loop is called an interation
# "interation through the list" means use a for loop

# for list example -- interating a list
fruits=["apple", "banana", "strawberry", "blueberry"]
for eachFruit in fruits:
    print(eachFruit)

# continue Keyword -- skips the current ineration and then finishes the loop.
fruits=["apple", "banana", "strawberry", "blueberry"]
for eachFruit in fruits:
    if eachFruit== "banana":
        continue
    print(eachFruit)

# break Keyword -- Immediately exit the loop
#fruits=["apple", "banana", "strawberry", "blueberry"]
#for eachFruit in fruits:
    #if eachFruit== "banana":
       # break
    #print(eachFruit)

# for loops using range(). range (x) is EXCLUSIVE, it starts at 0 and ends at x - 1
for i in range(10): # range is 0-9
    print(i)

# Might not always wnat to start at 0
for i in range(10,100): #
    print(i)

# not want to always count by 1 -- rare
for i in range(10,100,5):
    print(i)

# sometimes you're not done writing the loop
for x in range(10):
    pass # tells PYTHON this loop isn't finished, don't freak out

# while loops -- Musical Chairs
playerScore= 0
counter= 0
while playerScore < 100: # run as long as thisis True
    print(f"Starting: {playerScore}")
    playerScore += random.randint(1,100)
    print(f"After: {playerScore}")
    counter+= 1
print(f"Counter: {counter}")












