# Tuples ()

# Uma tupla (tuple) em Python é uma coleção ordenada e imutável de itens de dados. Elas são semelhantes às listas, mas a principal diferença é que o conteúdo de uma tupla não pode ser alterado após a sua criação

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

