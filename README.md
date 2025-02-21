# Python studies

Repository created in order to study and test Python programming language. 

Feel free to fork this repository.

## Main notes

`What is Python?`

Created by Guido van Rossum (Dutch mathematician and computer programmer), and released in 1991, Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. Its high-level built in data structures, combined with dynamic typing and dynamic binding, make it very attractive for Rapid Application Development, as well as for use as a scripting or glue language to connect existing components together. 

Python is widely used in: 

* Software Development
* Web Development 
* Data Science 
* Machine Learning
* Scientific Computing
* Automation 

<br />

`How to comment in Python`

Just like other programming languages, Python supports comments.

Commenting is an integral part of every programming language. With comments, you get a better understanding of your own code, make it more readable, and can help team members understand how it works.

Apart from making your code more readable, comments can also help while you're debugging – if you have two lines of code, you can comment out one to prevent it from running.

Comments are ignored by compilers and interpreters, so they are ignored by the interpreter during the execution of the program.

* Comments enhance the readability of the code.

* Comment can be used to identify functionality or structure the code-base.

* Comment can help understanding unusual or tricky scenarios handled by the code to prevent accidental removal or changes.

* Comments can be used to prevent executing any specific part of your code, while making changes or testing.

In Python, single line comments starts with hashtag symbol #

```
# this is a single line comment 
```
Python does not provide the option for multiline comments. However, there are different ways through which we can write multiline comments.

Multiline comments using multiple hashtags (#)

We can multiple hashtags (#) to write multiline comments in Python. Each and every line will be considered as a single-line comment.

```
# Python program to demonstrate
# multiline comments
print("Thanks for reading this documentation!")
````




```
""" 
this is a multi-line comment with Docstring 

(aka Python documentation strings) 

"""
``` 

`Data types`

* Strings

* Int

* Float

* Boolean 

`Python Operators Precedence Rule`

|Order|Rule Component|Operators| 
|-|-|-|
|1st|Parentheses|()| 
|2nd|Exponents| ** |
|3rd|Multiplication and Division| * / |
|4th|Addition and Subtraction|+ -|

## Developer commands

*Python* 

```
python --version

py --version

python -V

python application-name.py # run application e.g: python app.py
```

*Git* 

```
git rm -r --cached .
git add . 
git commit -m "Untrack files in .gitignore" 
```

You can use the following command if you want to ignore an specific file. 

E.g: *node_modules*

```
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

[W2 Schools | Python Tutorial](https://www.w3schools.com/python/default.asp)

[W3 Schools | Python Operators](https://www.w3schools.com/python/python_operators.asp)

`Python Org`

[Python Org](https://www.python.org/)

`Git`

[StackOverflow | .gitignore not ignoring files](https://stackoverflow.com/questions/45400361/why-is-gitignore-not-ignoring-my-files)

`Jupyter`

[Visual Studio Code | Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter#:~:text=Jupyter%20Extension%20for%20Visual%20Studio,used%20as%20a%20Jupyter%20kernel.)

`FreeCodeCamp`

[FreeCodeCampy | Python Multiline Comment](https://www.freecodecamp.org/news/python-multiline-comment-how-to-comment-out-multiple-lines-in-python/)

`GeeksforGeeks`

[GeeksforGeeks | Python Comments](https://www.geeksforgeeks.org/python-comments/)

[GeeksforGeeks | Multiline Comments in Python ](https://www.geeksforgeeks.org/multiline-comments-in-python/)

`MDN Web Docs`

[MDN Web Docs | CRLF](https://developer.mozilla.org/en-US/docs/Glossary/CRLF)