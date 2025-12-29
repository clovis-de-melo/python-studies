# Python Function 
# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result

# https://www.w3schools.com/python/python_functions.asp

# Creating a Function
# In Python a function is defined using the def keyword

def lines():
    print("-" * 30)

lines()

#

def my_function():
    print("Hello from a function")

# Calling a Function
# To call a function, use the function name followed by parenthesis

def my_function():
    print("Hello from function")

my_function()

# Arguments 



# Input function 

""" input("What's your name?") """

# Storing function in a Variable 

name = input("What's your name? ")

print(f"Hello, {name}. Welcome!")

# Sum function

number_1 = input("Type any number from 1 to 10. ")
number_2 = input("Type any number from 1 to 10. ")

print(f"The sum of number 1 and number 2 is equal to: {number_1 + number_2}") # Python is not really summing, is actually adding two strings together 

# Sum function solution (this is not a good practice)

number_3 = int(input("Please type any number from 1 to 10 again. ")) # int turns the string information into a number
number_4 = int(input("One more time, type any number from 1 to 10. ")) # int turns the string information into a number

print(f"The sum of number 3 and number 4 using int is equal to: {number_3 + number_4}") 

# Sum function solution (better outcome)

number_5 = input("Let's start over. Please type any number from 1 to 10. ")
number_6 = input("Type any number from 1 to 10. ")

int_number_5 = int(number_5)
int_number_6 = int(number_6)

print(f"The sum of number 5 and 6 using int variable is: {int_number_5 + int_number_6}")