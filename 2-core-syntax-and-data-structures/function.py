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

""" def my_function():
    print("Hello from a function")

# Calling a Function
# To call a function, use the function name followed by parenthesis

def my_function():
    print("Hello from function")

my_function() """

# Arguments 



# Input function 

""" input("What's your name?") """

# Storing function in a Variable 

# name = input("What's your name? ")

""" print(f"Hello, {name}. Welcome!")

# Sum function

# number_1 = input("Type any number from 1 to 10. ")
# number_2 = input("Type any number from 1 to 10. ")

print(f"The sum of number 1 and number 2 is equal to: {number_1 + number_2} (no 'int' used)") # Python is not really summing, is actually adding two strings together 

# Sum function solution (this is not a good practice)

# number_3 = int(input("Please type any number from 1 to 10 again. ")) # int turns the string information into a number
# number_4 = int(input("One more time, type any number from 1 to 10. ")) # int turns the string information into a number

print(f"The sum of number 3 and number 4 using int is equal to: {number_3 + number_4}") 

# Sum function solution (better outcome)

# number_5 = input("Let's start over. Please type any number from 1 to 10. ")
# number_6 = input("Type any number from 1 to 10. ")

# int_number_5 = int(number_5)
# int_number_6 = int(number_6)

print(f"The sum of number 5 and 6 using int variable is: {int_number_5 + int_number_6}") """

# lines()

# Function using parameters

def h2(txt):
    print("-" * 30)
    print(txt)

h2("Function exercise")

# Exercise 1 - Função simples (sem parâmetros)

""" Crie uma função chamada mostrar_mensagem que:

Não recebe parâmetros

Imprime a mensagem: "Hello, welcome to Python!"

Chame a função para testar

Dica: use def e print() """

def show_message():
    print("Hello, welcome to Python!")

show_message()

h2("Function exercise - Parameters")

# Exercise 2 - Função com um parâmetro

""" Crie uma função chamada mostrar_nome que:

Recebe um nome como parâmetro

Imprime: "Hello, <nome>!"

Teste a função passando seu nome

Dica: parâmetros funcionam como variáveis dentro da função """

def show_name(name):
    print(f"Hello, {name}!")

show_name("Clovis")

# Parameters examples

def sum(a, b):
    s = a + b
    print(s)

sum(2, 4)

# Python "help" options
# help()
# help(input) 
# print(input.__doc__)  # docstring





# Docstrings

""" (documentation string) is a special string literal that appears as the first statement in a module, function, class, or method definition to document the code. Unlike comments, docstrings are retained at runtime and can be accessed programmatically using tools like the built-in help() function or the .__doc__ attribute """

def somar(a, b, c=0):     # the same as somar(a=0, b=0, c=0)
    s = a + b + c
    print(f"A soma vale: {s}")

somar(3, 2, 5)
somar(8, 4)
somar(b=10, a=15, c=5)
somar(b=10, a=10)


# Return

h2("Return")

# Em Python (e em programação no geral), return serve para devolver um valor para quem chamou a função. O return é a saída da máquina
# entrada → processamento → saída

# Exemplo simples 

def soma(a, b):
    return a + b 

resultado = soma(2, 3)
print(resultado)

