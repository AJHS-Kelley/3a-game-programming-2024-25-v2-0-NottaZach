# Loops, Zachariah Thomas, v0.0

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
fruits=["apple", "banana", "strawberry", "blueberry"]
for eachFruit in fruits:
    if eachFruit== "banana":
        break
    print(eachFruit)





