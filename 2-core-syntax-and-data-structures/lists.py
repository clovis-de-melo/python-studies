# Lists

""" A list in Python is a collection that can store multiple items (like numbers, words, or other objects) in a single variable.
Lists are ordered, changeable (you can add, remove, or modify elements), and allow duplicate values. """

# Exercicio 1: criando e acessando listas 

# Crie uma lista com 5 frutas de sua preferência
# Mostre a primeira fruta
# Mostre a última fruta
# Mostre todas as frutas
# Desafio: Tente imprimir a terceira fruta da lista

frutas = ["maçã", "banana", "laranja", "uva", "morango"]

print(frutas[0])
print(frutas[-1])
print(frutas)
print(frutas[2])

# Exercício 2: Adicionando Itens

# Lista de compras inicial
# Adicione "leite" no final da lista
# Adicione "pão" no início da lista
# Mostre a lista completa
# Desafio: Adicione mais 2 itens que você gostaria de comprar!

compras = ["arroz", "feijão", "macarrão"]

compras.append("leite")

compras.insert(0, "pão")

print(compras)


