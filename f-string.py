# f string 

# F-strings, also known as formatted string literals, are a way to embed expressions inside string literals for formatting. Introduced in Python 3.6, they provide a concise and readable method for string interpolation 

# To create an f-string, prefix a string with the letter "f" or "F". Inside the string, expressions can be placed within curly braces {}. These expressions are evaluated at runtime and their values are inserted into the string

name = "John"
age = 30
print(f"My name is {name} and I am {age} years old")
# output: My name is John and I am 30 years old 

# F-strings can also be used to format numbers, dates, and other data types using Python's mini-language for formatting

price = 50
quantity = 3
print(f"Total cost: ${price * quantity}")
#print("the total is" price)
# print("total cost is {price * quantity}")
# output: Total cost: $150 



# Key advantages of f-strings include:

# Readability: Embedding expressions directly into strings makes the code easier to understand.

# Efficiency: F-strings are generally faster than other string formatting methods.

# Flexibility: They support a wide range of formatting options.

# Overall, f-strings are a powerful tool for string formatting in Python, offering a more intuitive and efficient alternative to older methods.

# Reference 

# https://pythonacademy.com.br/blog/f-strings-no-python
# https://www.w3schools.com/python/python_string_formatting.asp