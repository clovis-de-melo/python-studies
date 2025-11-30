# The range() function in Python generates a sequence of immutable numbers, commonly used for iterating a specific number of times in for loops. It returns a range object, which is an iterable but not a list itself, making it memory-efficient for large sequences.

# range() é uma função em Python que gera uma sequência de números inteiros, usada principalmente para controlar iterações em for loops. A sequência é imutável e pode ser definida por até três argumentos: start (início), stop (fim) e step (pulo ou incremento

for i in range(3):
    print("Hello")

""" 
Hello
Hello
Hello 
"""

for i in range(5):
    print(i)

""" 
0
1
2
3
4
"""

for _ in range(3):
    print("Underscore test")

""" 
Underscore test
Underscore test
Underscore test 
"""

