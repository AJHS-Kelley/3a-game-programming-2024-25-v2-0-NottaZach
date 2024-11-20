# Flow Control Structures, Zachariah Thomas, v0.0
# Making Computer Programs Make Decisions

temperature = 144.76
color = "yellow"
height = 2
likePineappleOnPizza = True

# SINGLE DECISIONS POINT- if statement
# if CONDITIONAL_EXPRESSION: <-- This will use a COMPARISON OPERATOR 99% of the time
    # runThisCode IF the CONDITIONAL_EXPRESSION is True

if temperature > 100:
    print("It is hot as the sun outside. \n")

if height >=5:
    print("They are above the height requirement. \n")

# CHEAT FOR IF STATEMENTS THAT USE BOOLEANS.
if likePineappleOnPizza:
    print("Tasty")

# What if we want something different to happen?
if color == "yellow": # COMMON ERROR FOR STUDENTS IS USING = instead of ==
    print("Your shirt is the correct uniform color. \n")
else:
    print("Your shirt is not the correct uniform color. \n")
weather = "Sunny"
if weather == "Sunny":
    print("It is sunny so you are good. \n")
else:
    print("If it's not sunny this it is out of commesion. \n")

# AMUSEMENT PARK HEIGHT CHECKER EXAMPLE
# Must be > min. height and < max. height to ride

if height >= 3: 
    print("You're too tall to ride the diddy slide! \n")
elif height >= 6:
    print("You're too tall to ride the diddy slide! \n")
else: # "oh, no, something's wrong!"
    print("Error, height not detected. Do not ride. \n")

# When writing if-elif-else blocks check for the HIGHEST VALUE first when using > or >=
    
# When writing if-elif-else blocks check for the LOWEST VALUE first when using < or <=
if height <= 3: 
    print("You're not too tall to ride the diddy slide! \n")
elif height < 6:
    print("You're tall enough to ride the diddy slide! \n")
else: # "oh, no, something's wrong!"
    print("Error, height not detected. Do not ride. \n")

if temperature >= 100:
    print("It is too hot for yall to be outside. \n")
elif temperature >= 50:
    print("You are allow to go out today. \n")
else:
    print("Error detecting temperature. \n")




