# Data Types and Operators, Zachariah Thomas, v0.0

# Fundamental Data Types
# String - str - Sequence of letters, numbers, spaces, or other characters
# Strings in Python are inside ' ' or " "
# idc if you use ' ' or " " just be consistent.

# Boolean - bool - True or False values.

# Float - float - any munber value with a decimal, +/-, including 0.0

# Integers - int - any whole numbers, +/-, including 0.

# Data types are stored in VARIABLES.
# A variable is basically a bucket with a name to put data into.
# VARIABLES NAMES SHOULD TELL YOU WHAT DATA IS BEING STORED IN IT.
# VARIABLES CANNOT START WITH A NUMBER
# camelCaseVariableNames
# snakes_case_variable_names

# DECLARING VARIABLES AND ASSIGNING VALUES

high_score = 565090 # int data type 
highScore = 450875 # int data types

carSpeed = 17.89 # float data type, miles per hour
car_speed = -2.97655 # float data type, miles per hour

hasAxe = True # boolean data type
isPurple = False # boolean data type

playerName = "Zachariah Thomas" # string data type
enemyType = "nature" # string data type

# ASSIGN NEW VALUES 
playerNames = "Rocky Will"
carspeed = -2.72

# DATA TYPES CAN CHANGE, BE CAREFUL
hasAxe = 3.0

# Printing Data Types
newInt= 3
newFloat= 4.0
newString= "W Sigma"
newBool= False 

print(type(newInt))
print(type(newFloat))
print(type(newString))
print(type(newBool))

# printing Variables to Console/Screen
print(playerName)
print(isPurple)
print(high_score)
print(car_speed)

# printing variabls and expressions to console / screen
print(high_score + 4700)
print(8 * 9)
print(high_score)


# PRINTING VARIABLES INSIDE OF STRINGS
print(f"Hello{playerName}. Your best rep was {high_score}. \n")

# ARITHMETIC OPRERATORS
myInt = 4
myFloat = 2.48
myNum = 0

# addition
myInt = 6 + 19
myFloat = 3.0 + 4.87

myInt = myInt + 7

myNum = myInt + myFloat
# When you add int and a float together, the answer becomes a float

# subtraction
myNum = myInt - myFloat
myInt = myFloat -1.85

# Multiplication
myNum = myInt * myFloat

# Division
myNumber = myInt / myFloat # first is numerator, second num is denominator

# MODULUS (MODULO) % --Returns REMAINDER after dividing.
 #MOST COMMON USE FOR MODULUS IS DETERMINING EVEN / ODD NUMBERS.
numStudents = 6
numSlicesPizza = 42

leftOvers = numSlicesPizza % numStudents
print(leftOvers)

# EXPONETS**
numSquared = 5 ** 3 # 5 is the base, 3 is the exponent.

# FLOOR-DIVISION // -- Divides, throws out any decimal
myNum = myInt // myFloat

# Addiction-Assignment Operator - Mostly used for counters.
myNum = 4
myNum = myNum + 2 # Old-School Method
myNum += 2 # New Hotness 
myNum *= 2
myNum /= 2


# CPMPARSION OPERATORS

# IS-EQUAL-TO== Are the two values equal to each other?
# Returns True or False based on evaluation.
x= 12.0
print(x==5)

# NOT-EQUAL-TO != Are the two values NOT equal?
# Returns True or False based on evaluation
print(x != 12)

# GREATER THAN / GREATER-THAN-OR-EQUAL TO
print(5 > 3) # Greater Than
print( 12 >= 2) # Greater Than or Equal to

# LESS THAN / LESS-THAN-OR-EQUAL TO
print(5 < 3) # LESS Than
print(12 <= 2) # Less Than or Equal To

# LOGICAL OPERATORS
# and -- ALL CONDITIONS MUST BE TRUE FOR ENTIRE STATEMENT TO BE TRUE
age = 27
height = 68.7
eyeColor = "blue"
# In order to ride the Teacups, you must be at least 18 years old and at least 60" tall
print( age >= 18 and height >= 60)
print( age >= 18 and height >= 60 and eyeColor == "Red")
# ALWAYS CHECK FOR THE LEAST-LIKELY TO BE FALSE CONDITION FIRST!!!!!
#print(defeatedBoss == True and level > 5 and hasBluekey == True)


# or -- AT LEAST ONE CONDITION MUST BE FOR ENTIRE STATEMENT TO BE TRUE
print( age >= 18 or height >= 60)
print( age >= 18 or height >= 60 and eyeColor == "Red")
#ALWAYS CHECK FOR THE MOST-LIKELY TO BE TRUE CONDITION FIRST!!!!!
#print(defeatedBoss == True or level > 5 or hasBluekey == True)

# not -- RETURNS THE OPPOSITE VALUE OF THE STATEMENT.
a = 8
#print(a == 8)
#print (not (not (a == 8)))

#COMBINING LOGICAL OPERATORS
#print(a == 8 and hasKey == True or isCloud == True)
#TRUE and 

# IDENTITY OPERATORS
g = 1.0
h = 1.0
i = g
print(g is h)
print(i is h)
print(i is not 1.0)
print(i is not g)

# MEMBERSHIP OPERATORS
fruits = ["apple", "banana", "tomato"]
print("banana" in fruits)
print("potato" in fruits)