# Python Indexing & Slicing — Complete Beginner Guide

This document shows **all common indexing and slicing variations in Python**, with clear explanations and simple examples.

---

## 1. Basic Indexing

Indexing is used to access a single element from a sequence (string, list, tuple).

```python
texto = "Python"
numeros = [10, 20, 30, 40, 50]
```

| Expression | Meaning |
|-----------|--------|
| texto[0] | First character |
| texto[1] | Second character |
| texto[-1] | Last character |
| numeros[2] | Third element |
| numeros[-2] | Second-to-last element |

---

## 2. Basic Slicing Syntax

```python
sequencia[inicio:fim:passo]
```

- **inicio** → where slicing starts (inclusive)
- **fim** → where slicing ends (exclusive)
- **passo** → how many steps to jump

---

## 3. Slice Variations (Most Used)

### First N elements
```python
texto[:3]
numeros[:3]
```

### From index N to the end
```python
texto[2:]
numeros[2:]
```

### From index A to B
```python
texto[1:4]
numeros[1:4]
```

### Last N elements
```python
texto[-3:]
numeros[-3:]
```

---

## 4. Slicing With Step

### Every element (default)
```python
texto[::1]
```

### Skip every second element
```python
texto[::2]
numeros[::2]
```

### Reverse sequence
```python
texto[::-1]
numeros[::-1]
```

---

## 5. Slicing With Negative Indices

```python
texto[-5:-2]
numeros[-4:-1]
```

Works the same way as positive indices, counting from the end.

---

## 6. Slicing From Middle

```python
texto[2:5]
numeros[2:5]
```

Starts at index 2, stops before index 5.

---

## 7. Common Pythonic Shortcuts

| Expression | Meaning |
|---------|--------|
| [:] | Copy entire sequence |
| [:3] | First 3 items |
| [-3:] | Last 3 items |
| [::2] | Every second item |
| [::-1] | Reverse sequence |

---

## 8. Indexing vs Slicing

| Indexing | Slicing |
|--------|--------|
| Returns one element | Returns a sequence |
| Uses one index | Uses start:end:step |
| Can raise IndexError | Never raises IndexError |

---

## 9. Works With All Sequences

Indexing and slicing work the same for:

- Strings
- Lists
- Tuples

❌ Not supported directly by:
- Sets
- Dictionaries (keys must be used)

---

## 10. Mental Model (Very Important)

- Python **starts counting at 0**
- The **end index is never included**
- Negative indices count **from the end**
- Step controls direction and jumps

---

## 11. Practice Examples

```python
palavra = "Pythonista"
numeros = [1, 2, 3, 4, 5, 6, 7, 8]
```

Try to:
- Get first 4 letters
- Get last 2 numbers
- Get numbers at even indices
- Reverse both sequences

---

## Final Tip

If you master slicing, **loops become easier**, and your code becomes more **Pythonic**.
