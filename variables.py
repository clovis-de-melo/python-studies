# Python Variables 
print("Python Variables")

# Creating Variables

# Variables are containers for storing data values 
# Python has no command for declaring a variable
# A variable is created the moment you first assign a value to it

# Example 

x = 5 
y = "John"
print(x)
print(y)

# Variables do not need to be declared with any particular type, and can even change type after they have been set.

x = 4 # x is of type int
x = "Sally" # x is not of type string
print(x)

# Casting 

# If you want to specify the data type of a variable, this can be done with casting.

# Example:

x = str(3) # x will be '3'
y = int(3) # y will be 3
z = float(3) # z will be 3.0


# Get the type 

# You can get the data type of a variable with the type() function

x = 5 
y = "John"
print(type(x)) # will print <class 'int'>
print(type(y)) # will print <class 'str'>


# Single or Double Quotes? 

# String variables can be declared either by using single or double quotes

# Example

x = "John"
# is the same as 
x = 'John'

# Case-Sensitive 

# Variable names are case-sensitive 

# Example

a = 4 
A = "Sally"
# this will create two variables 
# A will not overwrite a

print(a) # a
print(A) # Sally


# f String

name = "Daron"
age = 30
print(f"My name is {name} and I am {age} years old.")