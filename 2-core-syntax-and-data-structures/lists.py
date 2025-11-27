# Lists

""" A list in Python is a collection that can store multiple items (like numbers, words, or other objects) in a single variable.
Lists are ordered, changeable (you can add, remove, or modify elements), and allow duplicate values. """

# Exercicio 1: criando e acessando listas (Básico)

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

# Exercício 2: Adicionando Itens (Básico)

# Lista de compras inicial
# Adicione "leite" no final da lista
# Adicione "pão" no início da lista
# Mostre a lista completa
# Desafio: Adicione mais 2 itens que você gostaria de comprar!

compras = ["arroz", "feijão", "macarrão"]

compras.append("leite")

compras.insert(0, "pão")

print(compras)

# Exercício 3: Removendo Itens (Básico)


# lista de tarefas 
tarefas = ["estudar", "limpar casa", "fazer compras", "ler livros"]

# remova a segunda tarefa 
tarefas.remove("limpar casa")

# Ou remova pelo índice
# tarefas.pop(1) # remove pelo índice

print(tarefas)
print(tarefas[-2])

# Exercício 4: Percorrendo uma Lista (Intermediário)

# list de notas 

notas = [7.5, 8.0, 6.5, 9.0, 7.0]

# mostre cada nota

for nota_individual in notas:
    print(f"Nota individual: {nota_individual}")

# Desafio: Mostre quantas notas são maiores ou iguais a 7.0!

# soluação 1: simples

contador = 0 

for nota in notas:
    if nota >= 7.0:
        contador += 1

print(f"Notas maiores ou iguas a 7: {contador}") # 4

# solução 2: com lista

notas_aprovadas = []

for nota in notas:
    if nota >= 7.0:
        notas_aprovadas.append(nota)

print(f"Quantidade de alunos aprovados: {len(notas_aprovadas)}")
print(f"Notas aprovadas: {notas_aprovadas}")

# Prática

# Você tem uma lista de preços de produtos:
precos = [15.50, 23.00, 8.75, 42.00, 12.30]

# Desafios:

# 1. Mostre todos os preços na tela (use for)

for preco_individual in precos:
    print(f"Todos os preços: {preco_individual}")

# 2. Mostre quantos produtos custam menos de 20 reais

contador_precos = 0

for preco_individual in precos:
    if preco_individual < 20:
        contador_precos += 1


# Loop terminou, agora mostra o resultado:        
print(f"A quantidade de números menor que 20 é: {contador_precos}")

# 2.1 Mostre quantos produtos custam menos que 10 reais 

contador_precos = 0

for preco_produto in precos:
    if preco_produto < 10:
        contador_precos += 1

print(f"A quantidade de produtos menor que 10 reais é: {contador_precos}")



# 3. Mostre os produtos que custam menos de 20 reais

for preco_individual in precos:
    if preco_individual < 20:
        print(f"Número(s) menor que 20: {preco_individual}")

# add to a list 

preco_individual_menor_20 = []

for preco_individual in precos:
    if preco_individual < 20:
        preco_individual_menor_20.append(preco_individual)

print(preco_individual_menor_20)


# 4. Crie uma lista chamada "precos_baratos" com apenas os produtos abaixo de 20 reais

# 5. Calcule o total de quanto você gastaria comprando todos os produtos

# 6. Mostre o produto mais caro e o mais barato

