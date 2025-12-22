# Sets 

""" 
Um set é uma coleção de dados:

Não ordenada

Sem elementos duplicados

Mutável (você pode adicionar e remover itens)

Criada usando {} ou set() 
"""

numeros = {1, 2, 3, 3, 4}
print(numeros) # {1, 2, 3, 4}

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

""" Quando usar sets no mundo real?

Valores únicos (sem repetição)

Verificação rápida se algo existe

Comparar grupos de dados

Não se importa com ordem

Remover duplicados

"""

# Exemplo: remover nomes repetidos

nomes = ["Ana", "João", "Ana", "Maria"]
nomes_unicos = set(nomes)
print(nomes_unicos)

# Operações comuns com sets

# Adicionar 

cores = {"vermelho", "azul"}
cores.add("verde")
print(cores)

# Remover

cores.remove("azul")
print(cores)

# Verificar se existe 

print("vermelho" in cores) # True

# Operações matemáticas (bem comuns)

a = {1, 2, 3}
b = {3, 4, 5}

print(a | b) # união → {1, 2, 3, 4, 5}
print(a & b) # interseção → {3}
print(a - b) # diferença → {1, 2}

# Atenção 

# Sets não tem índice

# cores[0] # ERRO

# A ordem não é garantida 

# Para criar um set vazio: 

s = set() # correto 

# Exercício 1 - Criando um set 

# Você tem uma lista com números repeditos: 

numeros = [1, 2, 2, 3, 4, 4, 5]

# Desafios:

# Converta essa lista em um set
numeros_nao_repetidos = set(numeros)

# Mostre o resultado
print(numeros_nao_repetidos)

# Explique (em comentário) por que alguns números desapareceram
# quando convertido para set, os valores repetidos são removidos, pois set nao permite elementos duplicados

# Dica: use set()

# Exercício 2 - Verificando existência 

cores = {"vermelho", "azul", "verde"}

# Desafios:

# Verifique se "azul" está no set

print("azul" in cores)

# Verifique se "amarelo" está no set

print("amarelo" in cores)

# Mostre uma mensagem diferente para cada caso

if "azul" in cores:
    print("A cor azul está no set.")
else:
    print("A cor azul não está no set.")

if "amarelo" in cores:
    print("A cor amarela está no set.")
else: 
    print("A cor amarela não está no set.")

# Dica: use "in"

# Exercício 3 - Adicionando elementos 

# Você tem um set vazio 

frutas = set()

# Desafio 
 
# Adicione "maçã"

frutas.add("maçã")

print(frutas)

# Adicione "banana"

frutas.add("banana")

print(frutas)

# Tente adicionar "maçã" novamente

frutas.add("maçã") # set nao aceita valores repetidos

# Mostre o set final 

print(frutas)

# Dica: use .add()

# Exercício 4 - Removendo elementos

cores = {"vermelho", "azul", "verde", "amarelo"}

# Desafios:

# 1. Remova a cor "verde" do set

cores.remove("verde")

# 2. Tente remover a cor "preto" sem causar erro no programa

cores.discard("preto")

# 3. Mostre o set final

print(cores)

# Dicas

""" Existe um método que gera erro se o item não existir

Existe outro método que não gera erro

Use print() para ver o resultado final """

print("\nExercicio 5")

# Exercício 5 – Comparando sets

# Você tem dois sets de números:

numeros_a = {1, 2, 3, 4, 5}
numeros_b = {4, 5, 6, 7}

# Desafios:

# Mostre quais números aparecem nos dois sets

print(numeros_a & numeros_b)

# Mostre quais números existem apenas em numeros_a

print(numeros_a - numeros_b)

# Mostre quais números existem apenas em numeros_b

print(numeros_b - numeros_a)

# Mostre todos os números dos dois sets sem repetição

print(numeros_a | numeros_b)

""" Dicas:

Pesquise sobre: intersection, difference e union

Lembre-se: sets não permitem valores duplicados """