# Python Operators

# Operators are used to perform operations on variables and values.

# In the example below, we use the "+" operator to add together two values: 

# Example: print(10 + 5)

# Python divides the operators in the following groups: 

# Arithmetic operators
# Assignment operators
# Comparison operators
# Logical operators
# Identity operators
# Membership operators
# Bitwise operators


# Python Arithmetic Operators

# Arithmetic operators are used with numeric values to perform common mathematical operations:

print("Python Arithmetic Operators")

# + addition x + y 
# - subtraction x - y 
# * multiplication x * y 
# / division  x / y 
# % Modulus x % y
# ** exponentiation x ** y x = 2, y= 5 same as 2*2*2*2*2
# // Floor division x // y  the floor division // rounds the result down to the nearest whole number

print(100 + 20) # 120
print(100 - 20) # 80
print(100 * 20) # 2000
print(100 / 20) # 5
print(100 % 20) # 0
print(10 ** 20) # 100000000000000000000
print(11 // 2) # 5 

# Python Assignment Operators

# Assignment operators are used to assign values to variables:

print("Python Assignment Operators")

# = , x = 5, same as x =5 
# += , x += 3, same as x = x + 3
# -= , x -= 3, same as x = x + 3
# -= , x -= 3, same as x = x -3 
# *= , x *= 3, same as x = x * 3
# /= , x /= 3, same as x = x / 3
# %= , x %= 3, same as x = x % 3
# //= , x //= 3, same as x = // 3
# **= , x **= 3, same as x = x ** 3   
# &= , x &=3 , same as x = x & 3
# |= , x |= 3 , same as x = x | 3
# ^= , x ^= 3, same as x = x ^ 3
# >>= , x >>= 3, same as x = x >> 3
# <<= , x <<= 3, same as x = x << 3
# := , print(x:=3), same as x = 3(printx)


# Practice

# =  

x = 5
print(x) # 5

# +=

x = 5 
x += 3
print(x) # 8

# -=

x = 5 
x -= 3
print(x)

# *=

x = 5
x *= 3
print(x)


# Python Comparison Operators

print("Python Comparison Operators")

# Comparison operators are used to compare two values:

# == , Equal, x == y
# != , Not equal, x != y
# > , Greater than, x > y 
# < , Less than , x < y
#  >= , Greater than or equal to, x >= y
# <= , Less than or equal to, x <= y

# Practice

# == 

x = 5
y = 3
print(x == y) # false

x = 5
y = 5
print(x == y) # true

# != 

x = 5
y = 3
print(x != y) # true

x = 5
y = 5
print(x != y) # false

# >

x = 5
y = 3
print(x > y) # true

x = 5
y = 5
print(x > y) # false

# < 

x = 5
y = 3
print(x < y) # false

x = 8
y = 7
print(x > y) # true


# >= 

x = 5
y = 5
print(x >= y) # true

x = 2 
y = 6
print(x >= y) # false


# <= 

x = 5
y = 5
print(x <= y) # true

x = 6
y = 11
print(x >= y) # false

# Python Logical Operators

print("Python Logical Operators")

# Logical operators are used to combine conditional statements

# and

# or 

# not


# Python Operators Precedence Rule
print("Python's Operator Precedence Rule")

# 1st (n + n) Parentheses
# 2nd ** Exponents
# 3rd * / // % Multiplication and Division
# 4th + - Addition and Subtraction

total_1 = 1 + 1 ** 5 + 5 # 7 
print("total 1:", total_1) 

total_2 = (1 + 1) * 5 # 10
print("total 2:", total_2)

total_3 = 1 + (20 + 50) # 71
print("total_3", total_3)