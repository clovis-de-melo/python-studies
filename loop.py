# loop 

# A loop is a programming structure that allows you to repeat a block of code multiple times, automatically.

# The two main types of loops in Python are:

""" 
for loop (Counting, iterating through lists)
Repeats a fixed number of times or over a collection

while loop (Repeating until something changes, like guessing a number)
Repeats while a condition is true 
"""

print("Hello")
print("Hello")
print("Hello")

""" 
That works — but it’s repetitive and not efficient.

With a loop, you can do the same in one line:
"""

for i in range(3):
    print("Hello World")

# For

for i in range(5):
    print(i)


for i in range(5):
    print(f"This is loop number {i}")


# List of fruits 

fruits = ["apple", "banana", "orange", "grape", "mango"]

# How I'd print without using the loop feature 

print(f"I like{fruits[0]}")
print(f"I like {fruits[1]}")
print(f"I like {fruits[3]}")
print(f"I like {fruits[4]}")

# Loop through the list 

for fruit in fruits:
    print(f"I like {fruit}")

# Cars

cars = ["car1", "car2", "car3", "car4", "car5", "car6"]

for car in cars:
    print(f"I like {car}")

# Letters

for number in range(1, 10):
    print(number)


name = "Clovis de Melo"

for letter in name:
    print(letter)

# Numbers

numbers = [5, 8, 2, 9, 0, 1, 3, 4]

for n in numbers:
    if n % 2 != 0:
        print(f"The number {n} is even")
    else:
        print(f"The number {n} is odd")




# While Loop 

""" count = 1

while count <= 10:
    print(f"Count is: {count}")
    count += 1 """
