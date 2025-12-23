# Dictionaries

# Um dictionary é uma coleção de dados no formato: chave -> valor 

""" Exemplo do mundo real:

Nome → "Clovis"

Idade → 37

Cidade → "São Paulo" """

# Normalmente, em projetos reais, usamos chaves em minúsculo. Não é obrigatório, mas é uma boa prática

pessoa = {
    "nome": "Clovis",
    "idade": 37,
    "cidade": "São Paulo"
}

""" Regras importantes dos dictionaries

✔ Usam chaves (keys)
✔ Cada chave é única
✔ Os valores podem se repetir
✔ São mutáveis (podem ser alterados)
✔ Acessamos dados pela chave, não por índice """

# Acessando valores 

print(pessoa["nome"])    # Clovis
print(pessoa["idade"])   # 37
print(pessoa["cidade"])  # São Paulo 

# Diferente de listas/tuplas, não existe índice numérico

# print(pessoa[0]) -> erro

# Alterando valores 

pessoa["idade"] = 38
print(pessoa["idade"])
print(pessoa)

# Adicionando novos dados 

pessoa["Profissão"] = "Senior Content Editor"
print(pessoa)

pessoa["Chave"] = "Valor"
print(pessoa)

# Removendo dados

del pessoa["Chave"]
print(pessoa)

# Loop em dictionary (muito comum!) 

for chave in pessoa:
    print(chave)

for valor in pessoa.values():
    print(valor)

for chave, valor in pessoa.items():
    print(chave, ":", valor)

# Exemplo bem real 

produto = {
    "nome": "Laptop",
    "preco": 3500,
    "estoque": 10
}

print(produto)

if produto["estoque"] > 0:
    print("Produto disponível")
else:
    print("Produto não disponível no momento")

print("\nExercise 1")

# Exercício 1 — Dictionary básico

# Crie um dictionary chamado carro com as seguintes informações:
# marca, modelo e ano

carro = {
    "marca": "Volvo",
    "modelo": "XC90",
    "ano": 2020,
}

# 1. Mostre o modelo do carro

print(carro["modelo"])

# 2. Altere o ano do carro

carro["ano"] = 2025

# 3. Adicione a chave "cor"

carro["cor"] = "Preto"
print(carro)

""" Dicas

Use {} para criar o dict

Acesse usando ["chave"]

Para adicionar, basta atribuir uma nova chave """

# Exercício get()

pessoa = {
    "nome": "Carlos",
    "idade": 28,
    "cidade": "São Paulo"
}

# Desafios 

# Use get() para mostrar o nome da pessoa

print(pessoa.get("nome"))

# Use get() para mostrar a idade

print(pessoa.get("idade"))

# Use get() para tentar mostrar a chave "telefone" Se a chave não existir, mostre "Não informado"

print(pessoa.get("Telefone", "Valor não informado"))

# Mostre todas as informações da pessoa no formato:

""" 
Nome: X
Idade: Y
Cidade: Z
Telefone: W 
"""

""" 
Dicas: 

Use get("chave")

Use get("chave", "valor padrão")

Não use colchetes [] neste exercício 
"""

pessoa["Telefone"] = "W"

for chave, valor in pessoa:
    print(chave)