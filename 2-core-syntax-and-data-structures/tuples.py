# Tuples ()

# Uma tupla (tuple) em Python é uma coleção ordenada e imutável de itens de dados. Elas são semelhantes às listas, mas a principal diferença é que o conteúdo de uma tupla não pode ser alterado após a sua criação

# Diferença entre list, tuple e set
#
# Tipo    | Sintaxe | Ordenado | Aceita duplicados | Mutável
# --------|---------|----------|-------------------|---------
# list    | []      | Sim      | Sim               | Sim
# tuple   | ()      | Sim      | Sim               | Não
# set     | {}      | Não      | Não               | Sim
#
# Observações:
# - list: usada quando você precisa alterar dados com frequência
# - tuple: usada para dados fixos (constantes)
# - set: usada para remover duplicados e fazer comparações


# Lista "mutável"

""" 
frutas = ["maçã", "banana", "laranja"]
frutas[0] = "uva"  # Funciona
print(frutas)  # ["uva", "banana", "laranja"] 
"""

# Tuple "imutável"

""" 
frutas = ("maçã", "banana", "laranja")
frutas[0] = "uva"  # ERRO! Não pode modificar 
"""

# Exercício 1: Criando e Acessando Tuples

# Você tem uma tuple com coordenadas (x, y)
coordenadas = (10, 20)

# Desafios:
# 1. Mostre o valor de x (primeiro elemento)
print(coordenadas[0])

# 2. Mostre o valor de y (segundo elemento)
print(coordenadas[1])

# 3. Mostre quantos elementos tem na tuple
print(len(coordenadas))

# Exercício 2: Tuple de Cores

# Você tem uma tuple com cores RGB
cor_vermelha = (255, 0, 0)
cor_verde = (0, 255, 0)
cor_azul = (0, 0, 255)

# Desafios:
# 1. Mostre todas as cores
print(f"vermelho: {cor_vermelha}, verde: {cor_verde}, azul: {cor_azul}")

# 2. Mostre apenas o componente vermelho de cor_vermelha
print(cor_vermelha[0])

# 3. Use um loop para mostrar cada valor de cor_azul

for cada_valor_azul in range(len(cor_azul)):
    print(cor_azul[cada_valor_azul])

# Com range (usa índice):
for i in range(len(cor_azul)):
    print(cor_azul[i])

# Sem range (direto):
for valor in cor_azul:
    print(valor)

# Exercício: Tupla de animais
animais = ("cachorro", "gato", "coelho", "papagaio", "peixe")

# 1. Mostre os dois primeiros animais usando slicing
print(animais[0:2])

# 2. Mostre os dois últimos animais usando slicing com índice negativo
print(animais[-2:])

# 3. Use um loop para imprimir cada animal em letras maiúsculas
for cada_animal in animais:
    print(cada_animal.upper())

# Exercício: Tupla de números pares
pares = (2, 4, 6, 8, 10, 12)

# 1. Mostre os números do índice 1 ao 4
print(pares[1:4])

# 2. Use um loop para imprimir apenas os números maiores que 5

for i in pares:
    if i > 5:
        print(f"Números pares maior que 5 são: {i}")

# 3. Mostre a quantidade de números na tupla
print(len(pares))

# Exercício: Tupla mista de dados
dados = ("João", 25, "São Paulo", True)

# 1. Mostre o nome e a cidade usando indexing
print(dados[0])
print(dados[2])

# 2. Use slicing para mostrar idade e cidade
print(dados[1:3])

# 3. Use um loop para imprimir todos os elementos

for data in dados:
    print(data)

# Exercício: Tupla com números repetidos
numeros = (5, 10, 5, 20, 10, 5)

# 1. Mostre quantas vezes o número 5 aparece
print(numeros.count(5))

# 2. Mostre o índice da primeira ocorrência do número 10
print(numeros.index(10))

# 3. Use um loop para imprimir cada número multiplicado por 3
for i in numeros:
    print(i * 3)

# Exercício: Tupla aninhada (tuplas dentro de tuplas)
print("\n Tuplas dentro de tuplas")

pessoas = (("Alice", 25), ("Bob", 30), ("Carol", 22))

# 1. Mostre o nome da primeira pessoa
print(str(pessoas[0][0]))

# 2. Mostre a idade da segunda pessoa
print(pessoas[1][1])

# 3. Use um loop para imprimir "Nome: X, Idade: Y" para cada pessoa
for nome, idade in pessoas:
    print(f"Nome: {nome}, Idade: {idade}")