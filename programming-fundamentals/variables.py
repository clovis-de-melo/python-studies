# Python Variables 
print("# Python Variables")

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

# Age Calculator 

""" 
Step1: Ask birthday year
Step2: Define current year
Step3: Calculate user's age
Step4: Print user's age 
"""

birthday_year = int(input("What's your birthday year? "))

current_year = 2025

user_age = current_year - birthday_year

print(f"You are approximately {user_age} years old.")


# Age Conditional 

# Add a conditional statement which will confirm if user is underage or not

if user_age >= 10:
    print("You're an adult.")
else:
    print("You're a minor.")


# Currency Converter: Dollar to Real 

""" 
Step1: ask for the amount in dollars
Step2: define the exchange rate (you can change this value)
Step3: convert the value (define brazilian real)
Step4: print the result 
"""

dollar_amount = float(input("Enter the amount in US dollars (USD): "))

exchange_rate = 5.38

real_amount = dollar_amount * exchange_rate 

print(f"R${dollar_amount:.2f} USD is equivalent to ${real_amount:.2f} BRL")

# Details 

""" 
float() → converts input to a decimal number.

Mathematical operations (*) for conversions.

Formatting numbers with two decimal places using :.2f.

String interpolation using f"...". 
"""

""" 
int integer(inteiro) 10, -3, 2025 números sem parte decimal
float floating point (ponto flutuante) 10.5, -3.14, 0.001 números com parte decimal 
"""
