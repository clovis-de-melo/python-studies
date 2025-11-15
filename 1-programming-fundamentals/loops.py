# loop 

# A loop is a programming structure that allows you to repeat a block of code multiple times, automatically.

# The two main types of loops in Python are:

""" 
for loop (Counting, iterating through lists)
Repeats a fixed number of times or over a collection

while loop (Repeating until something changes, like guessing a number)
Repeats while a condition is true 
"""

print("Hello")
print("Hello")
print("Hello")

""" 
That works — but it’s repetitive and not efficient.

With a loop, you can do the same in one line:
"""

for i in range(3):
    print("Hello World")

# For

for i in range(5):
    print(i)


for i in range(5):
    print(f"This is loop number {i}")


# List of fruits 

fruits = ["apple", "banana", "orange", "grape", "mango"]

# How I'd print without using the loop feature 

print(f"I like{fruits[0]}")
print(f"I like {fruits[1]}")
print(f"I like {fruits[3]}")
print(f"I like {fruits[4]}")

# Loop through the list 

for fruit in fruits:
    print(f"I like {fruit}")

# Cars

cars = ["car1", "car2", "car3", "car4", "car5", "car6"]

for car in cars:
    print(f"I like {car}")

# Letters

for number in range(1, 10):
    print(number)


name = "Clovis de Melo"

for letter in name:
    print(letter)

# Numbers

numbers = [5, 8, 2, 9, 0, 1, 3, 4]

for n in numbers:
    if n % 2 != 0:
        print(f"The number {n} is even")
    else:
        print(f"The number {n} is odd")

# Exercise

# 1- Write a Python program that prints all even numbers from 1 to 20

for even_number in range(1, 21):
    if even_number % 2 == 0:
        print(even_number)

# If your goal is to list all even numbers together, you can improve it like this:

even_numbers = [] # create an empty list

for number in range(1, 21):
    if number % 2 == 0:
        even_numbers.append(number) # add even number to the list

print("\nThe even numbers from 1 to 20 are (on a list):", even_numbers)
print(f"\nThe even numbers from 1 to 20 are (on a list): {even_numbers}")



# 2- Write a Python program that prints all odd numbers from 1 to 20

for odd_number in range(1,21):
    if odd_number % 2 != 0:
        print(f"The odd numbers on a list from 1 to 20 are: {odd_number}")


# 3- Write a Python program that displays the multiplication table of the number 5 (from 1 to 10) using a for loop

for multiplication in range(1, 11):
    print(multiplication * 5)

# another option

for multiplication in range(1, 11):
    print(f"5 x {multiplication} = {multiplication * 5}")


for multiplation in range(1, 11):
    print(f"4 x {multiplation} = {multiplation * 4}")



# += Exercise 

# Write a Python program that adds the numbers from 1 to 5 using a for loop and the += operator.

total = 0 

for number in range(1, 6):
    total += number # total = total + number

print("A soma total é:", total)

# += 1 Exercise
# to do 

sum_total = 0

for numbers in range(1,5):
    sum_total += numbers # total = total + number 

print("The total sum is:", sum_total)






# While Loop 

count = 1

while count <= 10:
    print(f"Count is: {count}")
    count += 1

#

count = 1

while count <= 5:
    print(f"Count: {count}")
    count += 1

# 

# While Loop - Password Exercise

correct_password = "python123"
attempt = input("Type your password: ")

while attempt != correct_password:
    print("Wrong password. Please try again.")
    attempt = input("Type your password: ")

print("Access granted")

# For Loop - Password Exercise 

correct_password = "python123"

for attempt in range(3):
    password = input("Digite a senha: ")
    if password == correct_password:
        print("Acesso permitido")
        break
    else:
        print("Senha incorreta. Tentativas restantes:", 2 - attempt)
else:
    print("Acesso bloqueado")

# Break (examples)

# Exemplo 1 — Usando break com for

""" Você quer procurar um número específico em uma sequência.
Assim que encontrar, o loop deve parar. """

# exemplo: de 1 a 10, o loop deve parar quando chegar no numero 5

print("\nFor Loop: Must stop when reaching number 5")

for number in range(1, 11):
    print(f"Checking number {number}")
    if number == 5:
        print("Number 5 found! Loop stopped")
        break 

# \n (newline character)


""" Você quer pedir um número até o usuário acertar o número secreto (por exemplo, 7)
Quando chegar no numero 7, o loop deve encerrar  """

print("\nWhile loop: Must stop when user types number 7")

secret_number = 7 # número secreto fixo

number = 0 # inicializa a variável

while number != secret_number:
    number = int(input("Type a number from 1 to 50: "))

    if number == secret_number:
        print("Congratulations! The secret number is 7!")
        break
    else:
        print("Wrong number, keep trying")

# Lógica de Programação — “Adivinhar o Número Secreto”

""" Pedir números ao usuário até ele acertar o número secreto (7).
Quando o número digitado for igual ao número secreto, o programa deve encerrar. """

""" Passos Lógicos (em ordem):

1 Definir o número secreto

Guardar um valor fixo (exemplo: 7) que o usuário deve adivinhar.

2 Iniciar o processo de tentativa

Permitir que o usuário digite um número (entrada de dados).

3 Comparar o número digitado com o número secreto

Verificar se o número digitado é igual ao número secreto.

Essa é a condição principal.

4 Tomar uma decisão (estrutura condicional)

Se o número estiver correto:
→ Mostrar uma mensagem de acerto (“Parabéns!”)
→ Encerrar o programa.

Se o número estiver errado:
→ Mostrar uma mensagem de erro (“Tente novamente.”)
→ Voltar ao passo 2 (pedir outro número).

5 Repetir o processo até acertar

O programa deve continuar repetindo os passos 2, 3 e 4 até a condição ser satisfeita (acertar o número secreto).

6 Finalizar o programa

Quando o usuário acerta o número secreto, o programa deve sair do loop e terminar. """

""" Você quer pedir um número até o usuário acertar o número secreto (por exemplo, 37)
Quando chegar no numero 37, o loop deve encerrar  """

age = 37

guess_number = 0

while guess_number != age:
    guess_number = int(input("Guess my age. Type a number from 1 to 40: "))
    if guess_number == age:
        print("Congratulations! I'm 37 years old")
        break
    else:
        print("Try again.")

""" Try to guess a letter from A to Z using while loop

The correct letter should be C

When the user provides the correct letter, the loop should stop

Otherwise, the loop should continue until the user gets the correct answer """

correct_letter = "c" 

letter_guess = ""

while letter_guess != correct_letter:
    letter_guess = input("Try to guess a letter from A to Z: ")
    if letter_guess == correct_letter:
        print("Congratulations! The correct letter is C")
        break
    else:
        print("Wrong letter. Try again")

# pilares da lógica de programação: entrada → condição → repetição → saída.

# next: add lower case and upper case sensitive

# While loop exercise

# 1- Crie um programa em Python que continue pedindo um número ao usuário enquanto o número digitado NÃO for 0.

""" Quando o usuário digitar 0, o programa deve parar e exibir:

"Programa encerrado."

Dicas para iniciantes:

Use input() para receber o número.

Use int() para converter a entrada.

O loop deve ser:
while numero != 0:

Você precisa pedir o número de novo dentro do loop.

Certifique-se de que a variável seja criada antes do while. """

ask_numero = int(input("Digite um número: "))

while ask_numero != 0: # Continue repetindo enquanto o número NÃO for 0
    ask_numero = int(input("Digite o número novamente: "))

print("Programa encerrado")

""" Fluxo do programa (lógica simples)

Usuário digita um número

Enquanto o número NÃO for 0 → repete

Assim que o número for 0 → encerra e mostra a mensagem """

""" Continue repetindo enquanto o número NÃO for 0.

Então, quando o usuário digita 0:

a condição ask_numero != 0 fica falsa

o while para automaticamente

e o programa segue para a linha seguinte

Não é necessário verificar de novo. """

""" Redundância

Você sugeriu:

if ask_numero == 0:
    print("Programa encerrado")

Mas isso é redundante porque:

se o loop parou

é obrigatoriamente porque ask_numero == 0

Ou seja:

Não faz sentido checar algo que já sabemos ser verdade. """

# 1.1 - Opção com while True e break 

""" while True:
    ask_numero = int(input("Digite um número (0 para sair): "))
    
    if ask_numero == 0:
        print("Programa encerrado.")
        break
    
    print("Digite o número novamente.") """

# 2- Crie um programa que continue pedindo uma palavra ao usuário até ele digitar "exit".

""" Pergunta:

Quando o usuário digitar "exit", o programa deve parar e mostrar:

"Programa encerrado."

Dicas para iniciantes:

Use input() para receber a palavra do usuário.

Compare strings usando ==.

Lembre-se: texto digitado deve ser comparado entre aspas.

O loop deve continuar enquanto a palavra não for "exit".

Pode usar:
while palavra != "exit":

Não esqueça de atualizar a variável dentro do loop. """

ask_word = input("Digite uma palavra: ")

while ask_word != "exit":
    ask_word = input("Digite uma palavra novamente: ")

print("Programa encerrado")

""" O que significa “Pythonic”?

Pythonic é um termo usado pela comunidade Python para descrever código que é:

✔ simples
✔ limpo
✔ legível
✔ direto
✔ elegante
✔ escrito do jeito que a comunidade Python recomenda

Em outras palavras:

Pythonic = código escrito do jeito mais natural, bonito e idiomático para a linguagem Python.

É quando você usa os recursos do Python do jeito que eles foram feitos para serem usados """

# 3

""" Crie um programa que continue pedindo ao usuário para digitar um número maior que 10.

O programa só deve parar quando o usuário finalmente digitar um número acima de 10.

Quando isso acontecer, exiba:

"Obrigado! Número maior que 10 digitado." """

ask_number = int(input("Type any number greater than 10: "))

while ask_number <= 10:
    ask_number = int(input("Try again. Note: The number must be greater than 10: "))

print("Obrigado! Número digitado maior que 10 digitado.")

# 4 

""" Crie um programa que peça ao usuário para digitar um número positivo.
O programa deve continuar pedindo novos números enquanto o usuário digitar um número negativo.

Quando o usuário finalmente digitar um número zero ou positivo, exiba:

"Obrigado! Número válido digitado."

Dicas para resolver:

Converta o valor usando int().

Use uma condição de repetição:
while numero < 0:

Atualize o número dentro do loop.

A mensagem final deve estar fora do while. """

positive_number = int(input("Type a positive number: "))

while positive_number < 0: 
    positive_number = int(input("Try again. The number must be greater than zero: "))

print("Obrigado! Número válido digitado.")


# 5

""" Logic

1 Usuário digita um número

2 Se for negativo → repete

3 Se for zero ou positivo → encerra

4 Mensagem final aparece: Obrigado! Número zero ou positivo digitado """

numero_positivo = int(input("Digite um numero (zero ou positivo): "))

while numero_positivo < 0:
    numero_positivo = int(input("Digite um numero maior ou igual que zero novamente: "))

print("Obrigado! Número zero ou positivo digitado")