# Python studies <img align="left" alt="Python logo" title="Python" width="38px" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" style="padding-right:10px;" />

Repository created in order to study and practice Python programming language. 

Feel free to fork this repository. 

## Sections

* [What is Python?](#what-is-python)
* [Python Indentation](#python-indentation)
* [Python Comments](#python-comments)
* [Python Variables - Defition](#python-variables)
* [Python Variables - Names](#python-variables---names)
* [Python Variables - Assign Multiple Values](#python-variables---assign-multiple-values)
* [Python Variables - Output Variables](#python-variables---output-variables)
* [Python Variables - Keywords](#python-variables---keywords)
* [Python Data Types](#python-data-types)
* [Python Operators](#python-operators)
* [Python Operators - Arithmetic](#python-operators---arithmetic)
* [Python Operators - Assignment](#python-operators---assignment)
* [Python Operators - Comparison](#python-operators---comparison)
* [Python Operators - Logical](#python-operators---logical)
* [Developer Commands](#developer-commands)
* [Keywords](#keywords)
* [References](#references)

## What is Python?

Created by Guido van Rossum (Dutch mathematician and computer programmer), and released in 1991, Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. Its high-level built in data structures, combined with dynamic typing and dynamic binding, make it very attractive for Rapid Application Development, as well as for use as a scripting or glue language to connect existing components together. 

Python is widely used in: 

* Software Development
* Web Development 
* Data Science 
* Machine Learning
* Scientific Computing
* Automation 

What can Python do?

* Python can be used on a server to create web applications.
* Python can be used alongside software to create workflows.
* Python can connect to database systems. It can also read and modify files.
* Python can be used to handle big data and perform complex mathematics.
* Python can be used for rapid prototyping, or for production-ready software development.

Why Python?

* Python works on different platforms (Windows, Mac, Linux, Raspberry Pi, etc).
* Python has a simple syntax similar to the English language.
* Python has syntax that allows developers to write programs with fewer lines than some other programming languages.
* Python runs on an interpreter system, meaning that code can be executed as soon as it is written. This means that prototyping can be very quick.
* Python can be treated in a procedural way, an object-oriented way or a functional way.

Good to know

The most recent major version of Python is Python 3, which we shall be using in this tutorial. However, Python 2, although not being updated with anything other than security updates, is still quite popular.

## Python Indentation

Indentation refers to the spaces at the beginning of a code line.

Where in other programming languages the indentation in code is for readability only, the *indentation in Python is very important*.

Python uses indentation to indicate a block of code.

Example (syntax ok):

```python
if 5 > 2:
  print("Five is greater than two!")

  # Five is greater than two!
```
>[!WARNING]
>Python will give you an error if you skip the indentation:

Example (syntax error):

```python
if 5 > 2:
print("Five is greater than two!")

# follows below the print result

File "demo_indentation_test.py", line 2
    print("Five is greater than two!")
        ^
IndentationError: expected an indented block
```


## Python Comments

#### `How to comment in Python`

Just like other programming languages, Python supports comments.

Commenting is an integral part of every programming language. With comments, you get a better understanding of your own code, make it more readable, and can help team members understand how it works.

Apart from making your code more readable, comments can also help while you're debugging – if you have two lines of code, you can comment out one to prevent it from running.

Comments are ignored by compilers and interpreters, so they are ignored by the interpreter during the execution of the program.

* Comments enhance the readability of the code.

* Comment can be used to identify functionality or structure the code-base.

* Comment can help understanding unusual or tricky scenarios handled by the code to prevent accidental removal or changes.

* Comments can be used to prevent executing any specific part of your code, while making changes or testing.

In Python, single line comments starts with hashtag symbol #

```python
# this is a single line comment 
```
Python does not provide the option for multiline comments. However, there are different ways through which we can write multiline comments.

Multiline comments using multiple hashtags (#)

We can multiple hashtags (#) to write multiline comments in Python. Each and every line will be considered as a single-line comment.

```python
# Python program to demonstrate
# multiline comments
print("Thanks for reading this documentation!")
```

```python
""" 
this is a multi-line comment with Docstring 

(aka Python documentation strings) 

"""
``` 
## Python Variables

Variables are containers for storing data values.

A variable is created the moment you first assign a value to it.

Example:

```python
x = 5
y = "John"
print(x) # 5
print(y) # John
```
Variables do not need to be declared with any particular **type**, and can even change type after they have been set.

Example: 

```python
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)    # Sally
```
#### `Casting`

If you want to specify the data type of a variable, this can be done with casting.

```python
x = str(3) # x will be '3'
y = int(3) # y will be 3
z = float(3) # z will be 3.0
```
#### `Get the Type`

You can get the data type of a variable with the **type()** function.

Example: 

```python
x = 5
y = "John"
print(type(x)) # <class 'int'>
print(type(y)) # <class 'str'>
```
#### `Single or Double Quotes?`

String variables can be declared either by using single **'string'** or double quotes **"string"**:

Example: 

```python
x = "John"
# is the same as
x = 'John'
``` 
#### `Case-Sensitive`

Variable names are case-sensitive.

Example:

This will create two variables:

```python
a = 5 
A = "Sally" 

print(a) # 5
print(A) # Sally

# A will not overwrite a
```
## Python Variables - Names

A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:

* A variable name must start with a letter or the underscore character
* A variable name cannot start with a number
* A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
* Variable names are case-sensitive (age, Age and AGE are three different variables)
* A variable name cannot be any of the [Python keywords](https://www.w3schools.com/python/python_ref_keywords.asp).

Example:

Legal variable names:

```python
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
```
Illegal variable names:

```python
2myvar = "John"
my-var = "John"
my var = "John"
```

#### ```Multi Words Variable Names```

Variable names with more than one word can be difficult to read.

There are several techniques you can use to make them more readable:

* **Camel Case**

Each word, except the first, starts with a capital letter:

```python
myVariableName = "John"
```
* **Pascal Case**

Each word starts with a capital letter:

```python
MyVariableName = "John"
```
* **Snake Case**

Each word is separated by an underscore character:

```python
my_variable_name = "John"
```
## Python Variables - Assign Multiple Values

* **Many Values to Multiple Variables**

Python allows you to assign values to multiple variables in one line:

Example: 

```python
x, y, z = "Orange", "Banana", "Cherry"
print(x) # Orange
print(y) # Banana
print(z) # Cherry
```
>[!NOTE]
>Make sure the number of variables matches the number of values, or else you will get an error.

#### `One Value to Multiple Variables`

And you can assign the same value to **multiple variables** in one line:

Example: 

```python
x = y = z = "Orange"
print(x) # Orange
print(y) # Orange
print(z) # Orange
```
#### `Unpack a Collection`

If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called **unpacking**.

Example:

Unpack a list

```python
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x) # apple
print(y) # banana
print(z) # cherry
```
## Python Variables - Output Variables

The Python **print( )** function is often used to output variables.

Example

```python
x = "Python is awesome"
print(x) # Python is awesome
```
In the print( ) function, you output multiple variables, separated by a comma:

Example:

```python
x = "Python"
y = "is"
z = "awesome"
print(x, y, z) # Python is awesome
```
You can also use the **+** operator to output multiple variables:

Example:

```python
x = "Python " # note the space after 'Python '
y = "is " # note the space after 'is ' 
z = "awesome"
print(x + y + z) # Python is awesome
```
>[!WARNING]
>Notice the space character after "Python " and "is ", without them the result would be "Pythonisawesome".

For numbers, the **+** character works as a mathematical operator:

Example:

```python
x = 5
y = 10
print(x + y) # 15
```
>[!CAUTION]
>In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error:

```
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

Example:

```python
x = 5
y = "John"
print(x + y)

# TypeError: unsupported operand type(s) for +: 'int' and 'str'
```
The best way to output multiple variables in the print() function is to separate them with commas, which even support different data types:

Example: 

```python
x = 5
y = "John"
print(x, y) # 5 John
```
## Python Variables - Global Variables 

Variables that are created outside of a function (as in all of the examples in the previous pages) are known as global variables.

Global variables can be used by everyone, both inside of functions and outside.

Example:

Create a variable outside of a function, and use it inside the function

```python
x = "awesome"

def myfunc():
  print("Python is " + x) # Python is awesome

myfunc()
```

## Python Variables - Keywords

Python has a set of keywords that are **reserved words that cannot be used as variable names, function names, or any other identifiers**:

|Keyword|Description|
|-------|-----------|
|[and](https://www.w3schools.com/python/ref_keyword_and.asp)|A logical operator|
|[as](https://www.w3schools.com/python/ref_keyword_as.asp)|To create an alias|
|[assert](https://www.w3schools.com/python/ref_keyword_assert.asp)|For debugging|
|[break](https://www.w3schools.com/python/ref_keyword_break.asp)|To break out of a loop|
|[class](https://www.w3schools.com/python/ref_keyword_class.asp)|To define a class|
|[continue](https://www.w3schools.com/python/ref_keyword_continue.asp)|To continue to the next iteration of a loop|
|[def](https://www.w3schools.com/python/ref_keyword_def.asp)|To define a function|
|[elif](https://www.w3schools.com/python/ref_keyword_elif.asp)|Used in conditional statements, same as else if|
|[else](https://www.w3schools.com/python/ref_keyword_else.asp)|Used in conditional statements|
|[except](https://www.w3schools.com/python/ref_keyword_except.asp)|Used with exceptions, what to do when an exception occurs|
|[False](https://www.w3schools.com/python/ref_keyword_false.asp)|Boolean value, result of comparison operations|
|[finally](https://www.w3schools.com/python/ref_keyword_finally.asp)|Used with exceptions, a block of code that will be executed no matter if there is an exception or not|
|[for](https://www.w3schools.com/python/ref_keyword_for.asp)|To create a for loop|
|[from](https://www.w3schools.com/python/ref_keyword_from.asp)|To import specific parts of a module|
|[global](https://www.w3schools.com/python/ref_keyword_global.asp)|To declare a global variable|
|[if](https://www.w3schools.com/python/ref_keyword_if.asp)|To make a conditional statement|
|[import](https://www.w3schools.com/python/ref_keyword_import.asp)|To import a module|
|[in](https://www.w3schools.com/python/ref_keyword_in.asp)|To check if a value is present in a list, tuple, etc.|
|[is](https://www.w3schools.com/python/ref_keyword_is.asp)|To test if two variables are equal|
|[lambda](https://www.w3schools.com/python/ref_keyword_lambda.asp)|To create an anonymous function|
|[None](https://www.w3schools.com/python/ref_keyword_none.asp)|Represents a null value|
|[nonlocal](https://www.w3schools.com/python/ref_keyword_nonlocal.asp)|To declare a non-local variable|
|[not](https://www.w3schools.com/python/ref_keyword_not.asp)|A logical operator|
|[or](https://www.w3schools.com/python/ref_keyword_or.asp)|A logical operator|
|[pass](https://www.w3schools.com/python/ref_keyword_pass.asp)|A null statement, a statement that will do nothing|
|[raise](https://www.w3schools.com/python/ref_keyword_raise.asp)|To raise an exception|
|[return](https://www.w3schools.com/python/ref_keyword_return.asp)|To exit a function and return a value|
|[True](https://www.w3schools.com/python/ref_keyword_true.asp)|Boolean value, result of comparison operations|
|[try](https://www.w3schools.com/python/ref_keyword_try.asp)|To make a try...except statement|
|[while](https://www.w3schools.com/python/ref_keyword_while.asp)|To create a while loop|
|with|Used to simplify exception handling|
|[yield](https://www.w3schools.com/python/ref_keyword_yield.asp)|To return a list of values from a generator|

## Python Data Types

#### `Built-in Data types`

In programming, data type is an important concept.

Variables can store data of different types, and different types can do different things.

Python has the following data types built-in by default, in these categories:

* Text Type: **str**
* Numeric Types: **int**, **float**, **complex**
* Sequence Types: **list**, **tuple**, **range**
* Mapping Type: **dict**
* Set Types: **set**, **frozenset**
* Boolean Type: **bool**
* Binary Types: **bytes**, **bytearray**, **memoryview**
* None Type: **NoneType**

#### `Getting the Data Type`

You can get the data type of any object by using the type( ) function. Example:

Print the data type of the variable x

```python
x = 5 
print(type(x)) # <class 'int'>

y = 5.5
print(type(y)) # <class 'float'>

z = "John"
print(type(z)) # <class 'str'>

a = True
print(type(a)) # <class 'bool'>
``` 

#### `Setting the Data Type`

In Python, the data type is set when you assign a value to a variable:

|Example|Data Type|Print|
|-------|---------|-----|
|x = "Hello World|str|<class 'str'>|
|x = 20|int|<class 'int'>|
|x = 20.5|float|<class 'float'>|
|x = 1j|complex|<class 'complex'>|
|x = ["apple", "banana", "cherry"]|list|<class 'list'>|
|x = ("apple", "banana", "cherry")|tuple|<class 'tuple'>|
|x = range(6)|range|<class 'range'>|
|x = {"name": "John", "age": 36}|dict|<class 'dict'>|
|x = {"apple", "banana", "cherry"}|set|<class 'set'>|
|x = frozenset({"apple", "banana", "cherry"})|frozent|<class 'frozenset'>
|x = True|bool|<class 'bool'>|
|x = b"Hello"|bytes|<class 'bytes'>|
|x = bytearray(5)|bytearray|<class 'bytearray'>|
|x = memoryview(bytes(5))|memoryview|<class 'memoryview'>
|x = None|NoneType|<class 'NoneType'>|

#### `Setting the Specific Data Type`

If you want to specify the data type, you can use the following constructor functions:

|Example|Data Type|Print|
|-------|---------|-----|
|x = str("Hello World")|str|<class 'str'>|
|x = int(20)|int|<class 'int'>|
|x = float(20.5)|float|<class 'float>|
|x = complex(1j)|complex|<class 'complex'>
|x = list(("apple", "banana", "cherry"))|list|<class 'list'>|
|x = tuple(("apple", "banana", "cherry"))|tuple|<class 'tuple'>|
|x = range(6)|range|<class 'range'>|
|x = dict(name="John", age=36)|dict|<class 'dict'>|
|x = set(("apple", "banana", "cherry"))|set|<class 'set'>|
|x = frozenset(("apple", "banana", "cherry"))|frozenset|<class 'frozenset'>|
|x = bool(5)|bool|<class 'bool'>|
|x = bytes(5)|bytes|<class 'bytes'>|
|x = bytearray(5)|bytearray|<class 'bytearray'>|
|x = memoryview(bytes(5))|memomryview|<class 'memoryview'>|

## Python Operators

Operators are used to perform operations on variables and values.

In the example below, we use the + operator to add together two values:

```python
print(10 + 5) # 15
```

Python divides the operators in the following groups: 

* Arithmetic operators
* Assignment operators
* Comparison operators
* Logical operators
* Identity operators
* Membership operators
* Bitwise operators

## Python Operators - Arithmetic

Arithmetic operators are used with numeric values to perform common mathematical operations.

|Operator|Name|Example|
|--------|----|-------|
|+|Addition|x + y|
|-|Subtraction|x - y|
|*|Multiplication|x * y|
|/|Division|x / y|
|%|Modulus|x % y|
|**|Exponentiation|x ** y|
|//|Floor division|x // y|

## Python Operators - Assignment

Assignment operators are used to assign values to variables.

|Operator|Example|Same As|
|--------|-------|-------|
|=|x = 5|x = 5|x = 5|
|+=|x += 3|x = x + 3|
|-=|x -= 3|x = x + 3|
|*=|x *= 3|x = x * 3|
|/=|x /= 3|x = x / 3|
|%=|x %= 3|x = x % 3|
|//=|x //= 3|x = // 3|
|**=|x **= 3|x = x ** 3|
|&=|x &= 3|x = x & 3|
|&#124;=|x &#124;= 3|x = x &#124; 3|
|^=|X ^= 3|x = x ^ 3|
|>>=|x >>= 3|x = x >> 3|
|<<=|x <<= 3|x = x << 3|
|:=|print(x := 3)|x = 3 print(x)|

## Python Operators - Comparison

Comparison operators are used to compare two values.

|Operator|Name|Example|
|--------|----|-------|
|==|Equal|x == y|
|!=|Not equal|x != y|
|>|Greater than|x > y|
|<|Less than|x < y|
|>=|Greater than or equal to|x >= y|
|<=|Less than or equal to|x <= y|

## Python Operators - Logical 

Logical operators are used to combine conditional statements.

|Operator|Description|Example|
|--------|-----------|-------|
|and|Returns **True** if both statements are true|x < 5 **and** x < 10|
|or|Returns **True** if one of the statements is true|x < 5 **or** x < 4|
|not|Reverse the result, returns **False** if the results is **true**|not(x < 5 **and** x < 10) 

## Developer commands

*Python* 

```powershell
python --version

py --version

python -V

python application-name.py # run application e.g: python app.py
```

*Git* 

```powershell
git rm -r --cached .
git add . 
git commit -m "Untrack files in .gitignore" 
```

You can use the following command if you want to ignore an specific file. 

E.g: *node_modules*

```powershell
git rm -r --cached ./node_modules
```

## Keywords


`Jupyter`

*JupyterLab* is the latest web-based interactive development environment for notebooks, code, and data. Its flexible interface allows users to configure and arrange workflows in data science, scientific computing, computational journalism, and machine learning. A modular design invites extensions to expand and enrich functionality.

The *Jupyter extension for Visual Studio Code* (VS Code) enables users to work with Jupyter Notebooks in VS Code. The Jupyter PowerToys extension adds additional features to the Jupyter experience. 

Jupyter extension allows users to:

* to use any Python environment as a Jupyter kernel
* to create, open, and save Jupyter Notebooks
* to work with Jupyter code cells
* Allows users to connect to a remote Jupyter server
* Allows users to debug a Jupyter Notebook

Please note: 

This is *not* a Jupyter kernel--you must have Python environment in which you've installed the Jupyter package, though many language kernels will work with no modification. To enable advanced features, modifications may be needed in the VS Code language extensions.

`Anaconda`

Anaconda is an open-source distribution of Python that's used for data science, machine learning, and artificial intelligence. It includes a package manager, Conda, and a graphical user interface, Anaconda Navigator.

*Packages*

Includes pre-installed packages like NumPy, Pandas, and Scikit-learn, and thousands more available for installation 

*Package management*

Conda analyzes the environment before installing packages to avoid conflicts 

*Environments* 

Isolated workspaces that can be customized for specific projects 

*Jupyter Notebooks*

Works with this open-source web application for creating and sharing documents with equations, code, and visualizations 

`Google Colab`

Google Colab, or Colaboratory, is a free, browser-based environment for writing and running Python code. It's hosted on Google's cloud servers. 

*Features* 

* No setup: You don't need to configure anything to use Colab. 
* Free access to GPUs and TPUs: You can use these powerful computing resources for free. 
* Easy sharing: You can share your notebooks with others. 
* Store in Google Drive: You can save your notebooks to your Google Drive account.

*Use cases* 

* Data science: Analyze and visualize data using Python libraries
* Machine learning: Import image datasets, train image classifiers, and evaluate models
* Education: Use Colab for educational purposes

*How it works* 

* You can write and execute Python code in a web browser. 
* You can combine code, rich text, images, HTML, and LaTeX in your notebooks. 
* You can access your Google Drive directly from your notebook. 

`CR LF`

CR LF stands for *Carriage return plus Line feed*, they are [control characters](https://en.wikipedia.org/wiki/Control_character) or [bytecode](https://en.wikipedia.org/wiki/Bytecode) that can be used to mark a line break in a text file.

* CR = Carriage Return (\r, 0x0D in hexadecimal, 13 in decimal) — moves the cursor to the beginning of the line without advancing to the next line.

* LF = Line Feed (\n, 0x0A in hexadecimal, 10 in decimal) — moves the cursor down to the next line without returning to the beginning of the line.

## References

`W3 Schools`

[W3 Schools | Python Tutorial](https://www.w3schools.com/python/default.asp)

[W3 Schools | Python Syntax & Indentation](https://www.w3schools.com/python/python_syntax.asp)

[W3 Schools | Python Comments](https://www.w3schools.com/python/python_comments.asp)

[W3 Schools | Python Variables](https://www.w3schools.com/python/python_variables.asp)

[W3 Schools | Python Operators](https://www.w3schools.com/python/python_operators.asp)

[W3 Schools | Python Data Types](https://www.w3schools.com/python/python_datatypes.asp)

`Python Org`

[Python Org](https://www.python.org/)

`Git`

[GitHub Gist | List of github markdown emoji markup ](https://gist.github.com/rxaviers/7360908)

[StackOverflow | .gitignore not ignoring files](https://stackoverflow.com/questions/45400361/why-is-gitignore-not-ignoring-my-files)

`Jupyter`

[Visual Studio Code | Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter#:~:text=Jupyter%20Extension%20for%20Visual%20Studio,used%20as%20a%20Jupyter%20kernel.)

`FreeCodeCamp`

[FreeCodeCamp | Python Multiline Comment](https://www.freecodecamp.org/news/python-multiline-comment-how-to-comment-out-multiple-lines-in-python/)

[FreeCodeCamp | How to Create Notice Blocks in Markdown](https://www.freecodecamp.org/news/how-to-create-notice-blocks-in-markdown/)

`GeeksforGeeks`

[GeeksforGeeks | Python Comments](https://www.geeksforgeeks.org/python-comments/)

[GeeksforGeeks | Multiline Comments in Python ](https://www.geeksforgeeks.org/multiline-comments-in-python/)

`MDN Web Docs`

[MDN Web Docs | CRLF](https://developer.mozilla.org/en-US/docs/Glossary/CRLF)

<hr />

<a href="#top">Back to top :arrow_up:</a>