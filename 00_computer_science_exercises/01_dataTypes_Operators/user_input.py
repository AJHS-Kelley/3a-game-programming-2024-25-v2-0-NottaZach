# User Input Practice, Zachariah Thomas, v0.0

# input() is the built-inb function to get information from the KEYBOARD
# BASIC EXAMPLE
variableName = input("Please type a variable name press enter.\n")
print(variableName)

# input() saves ALL INPUT TO STRING DATA TYPES BY DEFAULT!!!
# input() saves ALL INPUT TO STRING DATA TYPES BY DEFAULT!!!
# input() saves ALL INPUT TO STRING DATA TYPES BY DEFAULT!!!
# input() saves ALL INPUT TO STRING DATA TYPES BY DEFAULT!!!

myNumber= input(" Please type an INTEGER number and press enter.\n")
# print(myNumber + 5) 



myNumber= int(input(" Please type an INTEGER number and press enter.\n"))
print(myNumber + 5)

#Wrapper Functions
# int() will convert the data to an INTEGER if possible
newNumber = input("Please type a value and press enter.\n")
print(int(newNumber)) # can convert STRING to INTEGER.
print(float(newNumber)) # can convert STRING to FLOAT.
print(str(newNumber)) # can convert FLOAT to STRING.

# float() will convert the data to an FLOAT if possible
newNumber = input("Please type a value and press enter.\n")
# print (int(newNumber))<-- cannot convert FLOAT to INTEGER.
print(float(newNumber)) # can convert STRING to FLOAT.
print(str(newNumber)) # can convert FLOAT to STRING.

# str() will convert the data to an STRING if possible
newNumber = 5
print( newNumber + newNumber) # Should print 10.
print(str(newNumber+ newNumber)) # Should print 55.








