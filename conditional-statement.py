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

# else

e = 10
f = 8
if f > e:
    print("f is greater than e")
elif f == e:
    print("f is equal ot e")
else:
    print("e is greater than f")


# % 

# In Python, the symbol % is called the modulus operator (or modulo operator). It gives you the remainder of a division between two numbers

""" 
Example: 3 x 4 = 9 (1 is remaining)

the % operator gives the remainder: 1 

"""

if 10 % 3 == 0:
    print("10")
else:
    print("5")

# Even vs Odd number example 

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("The number you've chosen is an even number")
else:
    print("The number you've chosen is an odd number")






