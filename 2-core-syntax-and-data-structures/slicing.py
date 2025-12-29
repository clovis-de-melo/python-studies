# Slicing 

# Slicing in Python is a technique used to extract a portion (subset) of a sequence, such as a string, list, tuple, or range, by specifying a start index, an end index, and an optional step

# sequence[start:end:step]

# start → index where the slice begins (inclusive)

# end → index where the slice ends (exclusive)

# step → how many elements to skip (optional)

# Slicing em Python é uma técnica usada para extrair uma parte de uma sequência, como strings, listas, tuplas ou ranges, especificando um índice inicial, um índice final e, opcionalmente, um passo.

# sequencia[inicio:fim:passo]

""" inicio → índice inicial (incluído)

fim → índice final (excluído)

passo → intervalo entre os elementos (opcional) """

""" Regras importantes de Slicing

O índice final nunca é incluído

Pode usar índices negativos

Funciona em strings, lists e tuples

Não altera a sequência original """

""" Dica final (muito importante)

Se você vê [:], [:3], [2:], [::2] → isso é slicing
Se você vê [3], [-1] → isso é indexing """

def lines():
    print("-" * 50)
    print("\n")

# Exercicio 1 - String básica 
print("\nString exercise")

palavra = "Python"

# 1. Mostre as 3 primeiras letras
print(palavra[:3]) # print(palavra[0:3]) menos pythonic

# 2. Mostre as 2 últimas letras
print(palavra[-2:])

# 3. Mostre a palavra inteira usando slicing
print(palavra[:])

lines()

# Exercicio 2 - Lista de números 
print("\nNumbers exercise")

numeros = [10, 20, 30, 40, 50, 60]

# 1. Mostre do segundo ao quinto número
print(numeros[1:5])

# 2. Mostre os 3 últimos números
print(numeros[-3:])

# 3. Mostre a lista pulando de 2 em 2
print(numeros[::2])

lines()

# Exercício 3 - Índices negativos
print("\nNegative index")

frutas = ["maçã", "banana", "laranja", "uva", "pera"]

# 1. Mostre as duas últimas frutas
print(frutas[-2:])

# 2. Mostre todas as frutas exceto a última
print(frutas[:-1])

lines()

# Exercício 4 - Tuples
print("\nTuples exercise")

cores = ("vermelho", "azul", "verde", "amarelo")

# 1. Mostre as três primeiras cores
print(cores[:3])

# 2. Mostre as cores do meio (sem a primeira e a última)
print(cores[1:-1])

""" 
| Objetivo                    | Slicing  |
| --------------------------- | -------- |
| Pular o primeiro            | [1:]   |
| Pular o último              | [:-1]  |
| Pular primeiro **e** último | [1:-1] | 
"""

lines()

# Exercicio 5 - Step
print("\nStep exercise")

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 1. Mostre apenas os números pares usando slicing
numeros_pares = numeros[1::2]
print(numeros_pares)

# 2. Inverta a lista usando slicing
inverted_list = numeros[::-1]
print(inverted_list)

lines()

# Exercicio 6 - Slicing + Loop 
print("\nSlicing + Loop")

numeros = [10, 20, 30, 40, 50, 60, 70, 80]

# Use slicing para pegar apenas os números que estão nas posições pares (índices 0, 2, 4, 6).


# Depois, use um loop para imprimir cada um desses números multiplicado por 2.



