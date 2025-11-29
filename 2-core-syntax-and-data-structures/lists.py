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


# Você tem uma lista de idades
idades = [12, 18, 25, 16, 30, 14, 22, 19, 15, 21]

# Desafios:
# 1. Mostre quantas pessoas são menores de idade (menos de 18 anos)

menores_de_idade = 0 

for idade in idades:
    if idade < 18:
        menores_de_idade += 1 # é o mesmo que menores_de_idade = menores_de_idade + 1 (Isso é um operador de atribuição composto)

print(f"O total de pessoas menores de idade é: {menores_de_idade}")

""" for inicia um loop (repetição)
idade é a variável temporária que recebe cada valor
in idades significa "para cada item na lista idades"
O loop vai executar 10 vezes (porque a lista tem 10 idades) """

""" menores_de_idade += 1 é o mesmo que menores_de_idade = menores_de_idade + 1
Aumenta o contador em 1
Só executa quando o if é verdadeiro (idade < 18) """

""" menores_de_idade = menores_de_idade + 1

Como funciona:
Passo a passo:

Pega o valor atual de menores_de_idade
Soma 1 a esse valor
Guarda o resultado de volta na variável menores_de_idade """

menores_de_idade = 0    # Valor inicial

menores_de_idade += 1   # 0 + 1 = 1
print(menores_de_idade) # 1

menores_de_idade += 1   # 1 + 1 = 2
print(menores_de_idade) # 2

menores_de_idade += 1   # 2 + 1 = 3
print(menores_de_idade) # 3

# 2. Crie uma lista "adultos" apenas com as idades de 18 anos ou mais

""" Regra simples para lembrar:
Pergunta do exercícioO que usarCódigo

"QUANTOS..."Contador (+= 1) contador += 1

"CRIE UMA LISTA..."Lista (append)lista.append(item) """

# Você tem uma lista de idades
idades = [12, 18, 25, 16, 30, 14, 22, 19, 15, 21]

adultos = []

for idade in idades:
    if idade >= 18:
        adultos.append(idade) # Adiciona a idade na lista

print(adultos)

# 2.1 Mostre quantas pessoas são maiores de idade (mais ou igual a 18 anos)

idades = [12, 18, 25, 16, 30, 14, 22, 19, 15, 21]

quantos_adultos = 0 

for idade in idades:
    if idade >= 18:
        quantos_adultos += 1

print(quantos_adultos)

# 3. Calcule a média das idades

idades = [12, 18, 25, 16, 30, 14, 22, 19, 15, 21]

""" Para calcular média:

Some todos os valores
Divida pela quantidade de valores

Operador usado: / (divisão) """

""" Outro exemplo com notas:
Um aluno tirou estas notas:
Prova 1: 7.0
Prova 2: 8.0
Prova 3: 9.0
Calcular média:
Soma: 7.0 + 8.0 + 9.0 = 24.0
Quantidade: 3 provas
Média: 24.0 ÷ 3 = 8.0 """

soma_idades = sum(idades)
print(soma_idades)

quantidade_idades = len(idades)
print(quantidade_idades)

media_idade = soma_idades / quantidade_idades 

print(media_idade)

# 4. Mostre a pessoa mais velha e a mais nova

idades = [12, 18, 25, 16, 30, 14, 22, 19, 15, 21]

mais_nova = min(idades)

mais_velha = max(idades)

print(f"A pessoa mais nova tem {mais_nova} anos e a mais velha tem {mais_velha} anos")

# Exercício 2: Notas de Alunos

# Você tem uma lista de notas
notas_alunos = [8.5, 6.0, 7.5, 9.0, 5.5, 7.0, 8.0, 4.5, 9.5, 6.5]

# Desafios:
# 1. Mostre quantos alunos foram aprovados (nota >= 7.0)

alunos_aprovados = 0 

for nota in notas_alunos:
    if nota >= 7.0:
        alunos_aprovados += 1

print(alunos_aprovados)


# 2. Mostre quantos alunos foram reprovados (nota < 7.0)

alunos_reprovados = 0 

for nota in notas_alunos:
    if nota < 7.0:
        alunos_reprovados += 1 

print(alunos_reprovados)

# 3. Crie uma lista "aprovados" com apenas as notas dos aprovados

notas_alunos = [8.5, 6.0, 7.5, 9.0, 5.5, 7.0, 8.0, 4.5, 9.5, 6.5]

aprovados = []

for nota in notas_alunos:
    if nota >= 7:
        aprovados.append(nota)

print(aprovados)        


# 4. Calcule a média geral da turma

notas_alunos = [8.5, 6.0, 7.5, 9.0, 5.5, 7.0, 8.0, 4.5, 9.5, 6.5]

somatorio = sum(notas_alunos)

quantidade_alunos = len(notas_alunos)

media = somatorio / quantidade_alunos

print(media)

# 5. Mostre a maior e a menor nota

maior_nota = max(notas_alunos)

menor_nota = min(notas_alunos)

print(f"A maior nota é {maior_nota}, e a menor nota é {menor_nota}.")

# Exercícios para fixar append():

# Crie uma lista vazia chamada "pares"
# Adicione apenas os números pares de 1 a 10
# Use append()

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

print(pares)        

# Crie uma lista "nomes_grandes"
# Adicione apenas nomes com mais de 5 letras

nomes = ["Ana", "Roberto", "Lu", "Fernanda", "João", "Mariana"]

nomes_grandes = []

for nome in nomes:
    if len(nome) > 5: # conta letras do nome
        nomes_grandes.append(nome) # adiciona na lista

print(nomes_grandes)

# Crie uma lista "positivos"
# Adicione apenas números maiores que 0

numeros = [-5, 10, -3, 8, 0, 15, -7]

positivos = []

for numero in numeros:
    if numero > 0:
        positivos.append(numero)

print(positivos)        