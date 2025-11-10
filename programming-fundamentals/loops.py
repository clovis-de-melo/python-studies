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

# Exercise

# 1- Write a Python program that prints all even numbers from 1 to 20

for even_number in range(1, 21):
    if even_number % 2 == 0:
        print(even_number)

# 2- Write a Python program that prints all odd numbers from 1 to 20

for odd_number in range(1,21):
    if odd_number % 2 != 0:
        print(f"The odd numbers on a list from 1 to 20 are: {odd_number}")


# 3- Write a Python program that displays the multiplication table of the number 5 (from 1 to 10) using a for loop

for multiplication in range(1, 11):
    print(multiplication * 5)

# another option

for multiplication in range(1, 11):
    print(f"5 x {multiplication} = {multiplication * 5}")


for multiplation in range(1, 11):
    print(f"4 x {multiplation} = {multiplation * 4}")



# += Exercise 

# Write a Python program that adds the numbers from 1 to 5 using a for loop and the += operator.

total = 0 

for number in range(1, 6):
    total += number # total = total + number

print("A soma total é:", total)

# += 1 Exercise
# to do 

sum_total = 0

for numbers in range(1,5):
    sum_total += numbers # total = total + number 

print("The total sum is:", sum_total)






# While Loop 

count = 1

while count <= 10:
    print(f"Count is: {count}")
    count += 1

#

count = 1

while count <= 5:
    print(f"Count: {count}")
    count += 1

# 

# While Loop - Password Exercise

correct_password = "python123"
attempt = input("Type your password: ")

while attempt != correct_password:
    print("Wrong password. Please try again.")
    attempt = input("Type your password: ")

print("Access granted")

# For Loop - Password Exercise 

correct_password = "python123"

for attempt in range(3):
    password = input("Digite a senha: ")
    if password == correct_password:
        print("Acesso permitido")
        break
    else:
        print("Senha incorreta. Tentativas restantes:", 2 - attempt)
else:
    print("Acesso bloqueado")

# Break (examples)

# Exemplo 1 — Usando break com for

""" Você quer procurar um número específico em uma sequência.
Assim que encontrar, o loop deve parar. """

# exemplo: de 1 a 10, o loop deve parar quando chegar no numero 5

print("\nFor Loop: Must stop when reaching number 5")

for number in range(1, 11):
    print(f"Checking number {number}")
    if number == 5:
        print("Number 5 found! Loop stopped")
        break 

# \n (newline character)


""" Você quer pedir um número até o usuário acertar o número secreto (por exemplo, 7)
Quando chegar no numero 7, o loop deve encerrar  """

print("\nWhile loop: Must stop when user types number 7")

secret_number = 7 # número secreto fixo

number = 0 # inicializa a variável

while number != secret_number:
    number = int(input("Type a number from 1 to 50: "))

    if number == secret_number:
        print("Congratulations! The secret number is 7!")
        break
    else:
        print("Wrong number, keep trying")









