# Python Data Types 

# https://www.w3schools.com/python/python_datatypes.asp

""" In programming, data type is an important concept.

Variables can store data of different types, and different types can do different things.

Python has the following data types built-in by default, in these categories:

Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType 
"""

""" A palavra class aparece porque o Python está mostrando a classe (tipo) do valor.

type() retorna o molde do objeto, não apenas o nome do tipo.

Tudo em Python (números, strings, listas, etc.) é um objeto de alguma classe. 

Isso é o coração da programação orientada a objetos.

Python é uma linguagem multi-paradigma, mas o paradigma de objetos é o mais fundamental.

"""

# Getting the Data Type
# You can get the data type of any object by using the type() function:

x = 5
print(type(x)) # <class 'int'>

y = "Clovis de Melo"
print(type(y)) # <class 'str'>

z = 10.5 
print(type(z)) # <class 'float'>

a = True
print(type(a)) # <class 'bool'>

x = 1j
print(type(x)) # <class 'complex'>

x = ["apple", "banana", "cherry"]
print(type(x)) # <class 'list'>

x = ("apple", "banana", "cherry")
print(type(x)) # <class 'tuple'>

x = range(6)
print(type(x)) # <class 'range'>

x = {"name" : "John", "age" : 36}
print(type(x)) # <class 'dict'>

x = {"apple", "banana", "cherry"}
print(type(x)) # <class 'set'>

x = frozenset({"apple", "banana", "cherry"})
print(type(x)) # <class 'frozenset'>

x = b"Hello"
print(type(x)) # <class 'bytes'>

x = bytearray(5)
print(type(x)) # <class 'bytearray'>

x = memoryview(bytes(5))
print(type(x)) # <class 'memoryview'>

x = None
print(type(x)) # <class 'NoneType'>

# Setting the Specific Data Type
# If you want to specify the data type, you can use the following constructor functions:

# to do https://www.w3schools.com/python/python_datatypes.asp

# x = 5
# y = "John"
# print(int(x) + str(y)) # error 

# Fix

d = 5
e = "John"
print(str(d) + e)

""" + serve para somar números ou concatenar strings
Mas nunca misturar os dois tipos
Use str() para converter número → texto
Use int() ou float() para converter texto → número """

# Exercícios — Type Conversion em Python

# 1. Converta um número digitado para inteiro

""" Objetivo: o usuário digita um número, e você transforma em int para fazer cálculos.

Desafio:

Digite um número: 5
Digite outro número: 3
Resultado: 8

Dica: use int(input(...)) """ 

first_number = int(input("Digite um número: "))
second_number = int(input("Digite outro número "))

print((f"Resultado: {first_number + second_number}"))


# 2. Corrija o erro de tipos diferentes

""" Código com erro:

g = 5
h = "10"
print(x + y)

Tarefa: conserte o código para que o resultado seja 15. """

g = 5
h = "10"
print(g + int(h))

# 3 Transforme um número em texto

""" Objetivo: transformar 7 em "7" e concatenar com uma palavra.

Dica:

j = 7
texto = " days in a week"

Resultado esperado: 7 days in a week """

j = 7
texto = " days a week"

print(str(j) + texto)
print(f"{j} days a week")
print(f"{j}" + texto)

# 4 Some dois números decimais digitados pelo usuário

# Dica: use float() para permitir números com ponto (3.5, 2.7).

insert_number_1 = float(input("Type a decimal number: "))

insert_number_2 = float(input("Type the second decimal nummber: "))

print(f"Sum is equal to: {insert_number_1 + insert_number_2}") # f-string avalia o cálculo dentro das {} e formata tudo como texto
print(f"Sum is equal to: {insert_number_1 + insert_number_2:.2f}") # limitar as casas decimais
print(f"The sum is equal to:", insert_number_1 + insert_number_2) # Aqui você passa dois argumentos para print(): o texto e o resultado da soma. O Python automaticamente adiciona um espaço entre eles
print("The sum is equal to:", insert_number_1 + insert_number_2) # maneira mais simples e para iniciantes




