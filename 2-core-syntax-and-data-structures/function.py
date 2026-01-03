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


# return é a palavra que devolve um valor de dentro de uma função para quem chamou essa função.

""" A função é uma máquina
Você coloca dados (parâmetros)
A máquina processa
O return é o resultado que sai da máquina """

h2("Function - Without Return")

def soma(a, b):
    print(a + b)

soma(10, 30)

""" O que acontece?

Mostra o resultado na tela

Mas o valor não pode ser reutilizado """

resultado_soma = soma(20, 40)
print(resultado_soma) # none

""" Isso NÃO funciona

Porque:
A função não devolveu nada
resultado_soma vira None """

h2("Function - With Return")

def subtracao(a, b):
    return a - b

resultado_subtracao = subtracao(100, 80)
print(resultado_subtracao)

""" Agora sim:

A função devolve o valor correto

Você pode guardar, usar, comparar, subtrair, etc """


""" Diferença entre print e return (muito importante)


| `print()`                | `return`             |
| ------------------------ | -------------------- |
| Mostra algo na tela      | Devolve um valor     |
| Serve para visualizar    | Serve para lógica    |
| Não pode ser reutilizado | Pode ser reutilizado |

print nao substitui return """ 

h2("Keep in mind: return ends the function")

""" The return statement ends the function execution.

When Python reaches return, the function stops running.

return immediately exits the function. """

# Tudo que vem depois do return não executa 

def test():
    print("Antes")
    return 
    print("Depois")

test() # Antes

h2("return types example")

# return pode devolver qualquer coisa

# Number 

def dobro(n):
    return n * 2 

# Text 

def saudacao():
    return "Olá!"

# Boolean 

def eh_maio(n):
    return n > 10

# List 

def criar_lista():
    return[1, 2, 3]

# Lógica (if / else)

def verificar_idade(idade):
    if idade >= 18:
        return "Maior de idade"
    else:
        return "Menor de idade"
    
# Função para ter vários return 

def classification(numero):
    if numero > 0:
        return "Positivo"
    if numero < 0:
        return "Negativo"
    return "Zero"

# Python executa o primeiro return que encontrar 

""" Quando usar return?

Use return quando você:

Precisa guardar um valor

Vai usar o resultado depois

Quer testar a função

Está criando lógica reutilizável

Use print quando:

Só quer mostrar algo para o usuário
"""

# Regra mental simples 

""" Funções retornam valores
Prints mostram valores """

h2("Exercise 1")

# Retornando um número

# Crie uma função chamada retorna_numero que retorne o número 10.

""" Dica:

Use return 10

Depois, use print() para mostrar o valor retornado """

def retorna_numero():
    return 10 

print(retorna_numero) # <function retorna_numero at 0x000002D ...>

print(retorna_numero()) # 10 

# Forma alternativa (também correta)

def retorna_numero():
    return 10

resultado = retorna_numero()
print(resultado)

h2("Exercise 2")

# Retornando uma string 

# Crie uma função chamada mensagem que retorne a string "Hello, Python!"

""" Dica:

return "Hello, Python!" """

def mensagem():
    return "Hello, Python!"

print(mensagem())

h2("Exercise 3")

# Soma simples 

""" Crie uma função soma que:

Receba dois números

Retorne a soma deles

Dica:

Não use print dentro da função

Use return """

def soma(d=30, e=50):
    return d + e 

print(soma()) # 80
print(soma(10, 20)) # 30

h2("Exercise 4")

# Multiplicação

""" Crie uma função multiplica que:

Receba dois números

Retorne o resultado da multiplicação """

def multiplica(a=3, b=5):
    return a * b

print(multiplica())
print(multiplica(4, 5))

# segunda opção 

def multiplica(a, b):
    return a * b

print(multiplica(1, 70))

h2("Exercise 5")

# Retornando um valor fixo 

# Crie uma função status que sempre retorne a palavra "OK"

def status():
    return "OK"

print(status())

h2("Exercise 6")

# Retornando o mesmo valo recebido 

""" Crie uma função eco que:

Receba um valor

Retorne exatamente esse valor

Dica:
Isso ajuda a entender que return devolve dados """

# Palavra

def eco():
    return input(f"Digite uma palavra: ")

palavra = eco()

print(palavra)
print(f"A palavra digitada foi: {palavra}")

# Número

def eco_number():
    return int(input("Digite um numero de 1 a 10: "))

numero = eco_number()

print(numero)
print(f"O número digitado foi: {numero}")


h2("Exercise 7")

# Retornando um cálculo simples 

""" Crie uma função quadrado que:

Receba um número

Retorne esse número elevado ao quadrado

Dica:
Use ** 2 
"""

def quadrado(a):
    return a ** 2

numero = int(input("Type any number from 1 to 10: "))

print(quadrado(numero))

h2("Exercise 8")

# Retornando uma frase montada

""" Crie uma função saudacao que:

Receba um nome

Retorne a frase:
"Hello, <nome>!"

Dica:
Use f-string dentro do return """

""" def saudacao():
    nome = input("Digite o seu nome: ")
    return nome 

print(f"Olá, {saudacao(nome)}") """





