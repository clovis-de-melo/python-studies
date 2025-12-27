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

pessoa["Nome"] = "X"
pessoa["Idade"] = "Y"
pessoa["Cidade"] = "Z"
pessoa["Telefone"] = "W"


# Exercicio pessoa.values()

print("\npessoa.values exercise")

pessoa = {
    "Nome": "Ana",
    "Idade": 28,
    "Cidade": "São Paulo"
}

# Desafios:

# Use pessoa.values() para mostrar todos os valores do dicionário.

print(pessoa.values())

print(list(pessoa.values())) # criar lista


# Use um for para imprimir cada valor em uma linha.

for i in pessoa.values():
    print(i)

# Conte quantos valores existem no dicionário

print(len(pessoa))

""" 
| Método     | O que faz            |
| ---------- | -------------------- |
| values() | Mostra só os valores |
| items()  | Mostra chave + valor |
| del      | Remove uma chave     |
| pop()    | Remove e retorna     |
| clear()  | Apaga tudo           | 

"""

# Exercicio pessoa.items()
print("\nExercise 2")

pessoa = {
    "Nome": "Carlos",
    "Idade": 35,
    "Profissão": "Engenheiro"
}

# Desafios:

# Use pessoa.items() para imprimir chave e valor juntos.

print(pessoa.items())


# Mostre as informações no formato:
# Chave: X | Valor: Y

for key, value in pessoa.items():
    print(f"Chave: {key} | Valor: {value}")

# Use um loop para imprimir todas as informações da pessoa.

for i in pessoa.items():
    print(i)

# better way 

for key, value in pessoa.items():
    print(f"{key}: {value}")


""" Dica de iniciante (importante)

pessoa.values() → valores

pessoa.keys() → chaves

pessoa.items() → pares (chave, valor)

len(pessoa) → quantidade total de itens """


# Exercicio del 

pessoa = {
    "Nome": "Marina",
    "Idade": 22,
    "Cidade": "Rio de Janeiro"
}

# Desafios:

# Remova a chave "Cidade" usando del.
del pessoa["Cidade"]

# Mostre o dicionário após a remoção.

print(pessoa)

# O que acontece se tentar remover uma chave que não existe? (pense antes de testar)

# um erro é gerado. o mais correto nesse caso seria usar pop()

# Important

# del é um comando da linguagem, não um método
# Ele remove algo diretamente da memória
# Por isso a sintaxe é:

""" 
del objeto
del lista[indice]
del dicionario[chave] 
"""

# Exercicio pop()
print("\nPop exercise")

produto = {
    "Nome": "Teclado",
    "Preco": 150,
    "Estoque": 20
}

# Desafios:

# Use pop() para remover a chave "Estoque".

# Guarde o valor removido em uma variável.

removed_item = produto.pop("Estoque")

# Mostre o valor removido.

print(f"Removed item: {removed_item}")

# Mostre o dicionário final.

print(produto)

# Exercicio clear()
print("\nClear exercise")

configuracoes = {
    "tema": "dark",
    "idioma": "pt-BR",
    "notificacoes": True
}

# Desafios:

# Use clear() para apagar todo o dicionário.

configuracoes.clear()

# Mostre o dicionário após usar clear().

print(configuracoes)

# Verifique o tamanho do dicionário depois da limpeza.

print(len(configuracoes))

# Exercício - Usando copy() em dicionários

print("\nCopy exercise")

pessoa = {
    "Nome": "Ana",
    "Idade": 28,
    "Cidade": "Rio de Janeiro"
}

# Desafios:

# 1. Crie uma cópia do dicionário pessoa usando copy()

copia_pessoa = pessoa.copy()

# 2. Altere a idade na cópia para 30

copia_pessoa["Idade"] = 30

# 3. Mostre o dicionário original

print(pessoa)

# 4. Mostre o dicionário copiado

print(copia_pessoa)

# 5. Explique (em comentário) por que o dicionário original não foi alterado

# porque a copia foi armazenada em uma variavel .copy() e é independente

