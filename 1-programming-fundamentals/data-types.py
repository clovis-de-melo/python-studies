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



