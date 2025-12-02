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

# Use range() e um loop for para mostrar os números de 0 a 9

# Resultado esperado:
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

for i in range(10):
    print(i)

# Use range() para mostrar seu nome 5 vezes

# Exemplo de resultado:
# João
# João
# João
# João
# João

for i in range(5):
    print("Clovis")

# Use range() para mostrar os números de 1 a 5 (não de 0 a 4)
# Dica: range(1, 6) começa em 1 e para antes do 6

for i in range(1, 6):
    print(i)

# Use range() para mostrar qual é a linha (número da volta)

# Resultado esperado:
# Linha 0
# Linha 1
# Linha 2
# Linha 3
# Linha 4
# Linha 5
# Linha 6

# Dica: Você vai precisar usar f-string para juntar "Linha" com o número!

for i in range(7):
    print(f"Linha {i}")

# Use range() para mostrar apenas números pares de 0 a 10
# Dica: range(0, 11, 2) - o terceiro número é o "passo"

# Resultado esperado:
# 0
# 2
# 4
# 6
# 8
# 10

for i in range(0, 11, 2):
    print(i)



