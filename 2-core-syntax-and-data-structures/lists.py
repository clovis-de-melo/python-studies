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

print("-" * 60)
print("\nNotas")

notas = [7.5, 8.0, 6.5, 9.0, 7.0]

# mostre cada nota

print(notas) # Se o exercício pedisse "mostre todas as notas" ou "mostre a lista de notas", aí sim

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
print("-" * 60)
print("\nPrática")

# Você tem uma lista de preços de produtos:
precos = [15.50, 23.00, 8.75, 42.00, 12.30]

# Desafios:

# 1. Mostre todos os preços na tela (use for)

for preco_individual in precos:
    print(f"\nTodos os preços: {preco_individual}")

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

precos = [15.50, 23.00, 8.75, 42.00, 12.30]

precos_baratos = []

for preco in precos:
    if preco < 20:
        precos_baratos.append(preco)
        
print(f"Os produtos abaixo de 20 reais sâo: {precos_baratos}")

# 4.1 Exercicio 

# Crie uma lista chamada "valores_baratos" com apenas os produtos igual ou menor que 10 reais

valores = [13.50, 50, 60, 120, 10, 4, 5, 40, 2, 9, 25]

valores_baratos = []

for valor in valores:
    if valor <= 10:
        valores_baratos.append(valor)

print(valores_baratos)




# 5. Calcule o total de quanto você gastaria comprando todos os produtos

# option 1

total = sum(valores)

print(f"Total option 1 is: {total}")

# option 2

total_option_2 = 0 

for valor in valores:
    total_option_2 += valor 

print(f"Total option 2 is: {total_option_2}")


# 6. Mostre o produto mais caro e o mais barato

mais_barato = min(valores)
mais_caro = max(valores)

print(f"O mais barato é {mais_barato} e o mais caro é {mais_caro}")
print(len(valores))


