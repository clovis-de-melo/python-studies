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

Sets são ótimos quando você quer:

Remover duplicados

Verificar se algo existe rapidamente

Comparar grupos de dados """

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

cores[0] # ERRO

# A ordem não é garantida 

# Para criar um set vazio: 

s = set() # correto 

