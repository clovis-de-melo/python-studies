# In Python, the if statement is a conditional statement that executes a block of code only if a specified condition is true. 
# It is a fundamental part of decision-making in programming.

# https://www.w3schools.com/python/python_conditions.asp

# Python supports the usual logical conditions from mathematics

""" 
Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
"""

# These conditions can be used in several ways, most commonly in "if statements" and loops.
#An "if statement" is written by using the if keyword

# Example

# if statement 

a = 33
b = 200
if b > a:
    print("b is greater than a") # print: b is greater than a

# elif
# The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".

c = 33
d = 33
if d > c:
    print("d is greater than c")
elif c == d:
    print("c and d are equal") # print: c and are equal 