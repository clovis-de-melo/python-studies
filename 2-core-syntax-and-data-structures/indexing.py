# Indexing

# Python indexing é o processo de acessar elementos individuais dentro de uma sequência (como listas, tuplas ou strings) usando sua posição numérica, que sempre começa em 0 (o primeiro item tem índice 0, o segundo tem índice 1, e assim por diante). Essa técnica usa colchetes [] para indicar qual item você quer, como minha_lista[0] para pegar o primeiro item, e também permite índices negativos para acessar do final da sequência para o início (ex: -1 para o último item). 

def lines():
    print("-" * 40)
    print("\n")

# Exercício 1: Acessar elementos

numeros = (10, 20, 30, 40, 50)

# 1. Mostre o primeiro número
print(numeros[0])

# 2. Mostre o terceiro número
print(numeros[2])

# 3. Mostre o último número (use índice -1)
print(numeros[-1])

# 4. Altere o segundo número para 25 e mostre a lista completa
# tuple nao pode ser alterada

lines()

# Exercício 2

frutas = ("maçã", "banana", "laranja", "uva")

# 1. Crie uma variável posicao = 2

posicao = 2 

# 2. Use essa variável para mostrar a fruta na posição 2

print(frutas[posicao])

# 3. Mude posicao para 0 e mostre novamente

posicao = 0 

print(frutas[posicao])

lines()

# Exercício 2 Indexing com string

# Dica: strings também usam indexing


palavra = "Python"

# Mostre a primeira letra

print(palavra[0])

# Mostre a letra na posição 2

print(palavra[2])

# Mostre a última letra

print(palavra[-1])

lines()

# Exercício — Indexing com string e tamanho

nome = "Programacao"

# Mostre a primeira letra da palavra

print(nome[0])

# Mostre a última letra usando o tamanho da string

print(nome[len(nome) - 1])

# Crie uma variável meio que guarde o índice do caractere do meio

meio = len(nome) // 2

# Use essa variável para mostrar a letra do meio

print(nome[meio])

""" 
Dicas:

Use len() para descobrir o tamanho da string

Lembre-se: índices começam em 0

O índice do meio pode ser calculado com divisão inteira 
"""

lines()

numeros = [10, 20, 30, 40, 50, 60]

# Mostre o primeiro número da lista.

print(numeros[0])


# Mostre o último número da lista usando índice negativo.

print(numeros[-1])

# Mostre o terceiro número da lista.

print(numeros[2])

# Altere o segundo número para 25 e mostre a lista completa.

numeros[1] = 25
print(numeros)

lines()

# Exercicio 

palavra = "Pythonista"

# 1. Mostre a primeira letra
print(palavra[0])

# 2. Mostre a quarta letra
print(palavra[3])

# 3. Mostre a última letra usando índice negativo
print(palavra[-1])

# 4. Mostre as 3 primeiras letras da palavra
print(palavra[0:3]) # slicing 

# 

lines()

numeros = [10, 20, 30, 40, 50, 60]

# 1. Mostre o primeiro número
print(numeros[0])

# 2. Mostre o último número usando índice negativo
print(numeros[-1])

# 3. Mostre os números do índice 2 ao 4 (inclusive 2, exclusivo 4)
print(numeros[2:4])

# 4. Altere o número do índice 3 para 45 e mostre a lista completa
numeros[3] = 45
print(numeros)

# 

lines()

itens = ["maçã", 10, "banana", 20, 30, "laranja"]

# 1. Mostre o item na posição 1
print(itens[1])

# 2. Mostre o último item usando índice negativo
print(itens[-1])

# 3. Mostre os itens do índice 2 ao 5
print(itens[2:5])
