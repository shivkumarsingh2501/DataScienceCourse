# Python Data Types - Structured Interview Notes

## 1. What Are Data Types?

A data type defines the kind of value a variable stores.

Data types help Python decide:
- What operations are valid.
- How to represent values in memory.
- How to process values correctly.

```python
age = 25
```

Here, `25` is an `int` (integer).

## 2. Why Data Types Matter

Data types are important because they:
1. Store data efficiently.
2. Enable valid operations.
3. Prevent many runtime errors.
4. Improve code clarity.

Examples:

```python
25 + 10              # valid
"hello" + "world"    # valid
"hello" + 10         # TypeError
```

## 3. Basic Python Data Types

| Data Type | Example | Description |
|---|---|---|
| `int` | `10` | Whole numbers |
| `float` | `5.11` | Decimal numbers |
| `str` | `"Hello"` | Text data |
| `bool` | `True`, `False` | Logical values |

## 4. Integer (`int`)

Integers are whole numbers (positive, negative, or zero).

```python
age = 35
print(type(age))     # <class 'int'>
```

More examples: `10`, `0`, `-50`, `2000`

## 5. Float (`float`)

Floats are decimal numbers.

```python
height = 5.11
print(height)        # 5.11
print(type(height))  # <class 'float'>
```

More examples: `3.14`, `0.5`, `100.75`

## 6. String (`str`)

Strings store text and use single or double quotes.

```python
name = "Krish"
print(name)          # Krish
print(type(name))    # <class 'str'>
```

More examples: `"Python"`, `"Data Science"`, `"Hello World"`

## 7. Boolean (`bool`)

Booleans represent `True` or `False`.

Used in:
- Conditions
- Comparisons
- Logical expressions

```python
is_student = True
print(type(is_student))  # <class 'bool'>
```

Booleans from comparison:

```python
a = 10
b = 10
print(a == b)            # True
```

## 8. Checking Type with `type()`

Use `type()` to inspect a value's data type.

```python
age = 25
name = "Krish"

print(type(age))         # <class 'int'>
print(type(name))        # <class 'str'>
```

## 9. Common Data Type Error

Problem example:

```python
result = "hello" + 5
```

This raises `TypeError` because `str + int` is invalid.

Fix using conversion:

```python
result = "hello" + str(5)
print(result)            # hello5
```

This conversion is called type casting.

## 10. String Methods (Preview)

Useful built-in string methods:
- `upper()`
- `lower()`
- `capitalize()`
- `count()`
- `find()`
- `replace()`
- `split()`

```python
text = "hello"
print(text.upper())      # HELLO
```

## 11. Advanced Data Types (Learn Next)

| Data Type | Example |
|---|---|
| `list` | `[1, 2, 3]` |
| `tuple` | `(1, 2, 3)` |
| `set` | `{1, 2, 3}` |
| `dict` | `{"name": "Krish"}` |

These are heavily used in data analysis and machine learning workflows.

## 12. Combined Example (All Basic Types)

```python
age = 25
height = 5.11
name = "Krish"
is_student = True

print(age)
print(height)
print(name)
print(is_student)

print(type(age))
print(type(height))
print(type(name))
print(type(is_student))
```

## 13. Most Common Interview Questions

Q1. What are Python data types?  
A. They classify values, such as `int`, `float`, `str`, `bool`, `list`, `tuple`, `dict`, and `set`.

Q2. Difference between `int` and `float`?  
A. `int` stores whole numbers (for example, `10`), while `float` stores decimal numbers (for example, `3.14`).

Q3. What is a boolean data type?  
A. It stores logical values: `True` or `False`.

Q4. What does `type()` do?  
A. It returns the data type of a value/variable.

Q5. Why does `"hello" + 5` fail?  
A. Python cannot directly combine `str` and `int`; convert first (for example, `str(5)`).

## 14. Data Science Context

You will frequently work with:
- `list`
- `dict`
- NumPy arrays
- Pandas DataFrames

```python
import pandas as pd

data = pd.read_csv("data.csv")
```

Here, `data` stores a dataset.

## 15. Quick Revision Sheet

- Data type -> kind of value stored in a variable.
- Basic types -> `int`, `float`, `str`, `bool`.
- Check type -> `type(variable)`.
- Convert type -> `int()`, `float()`, `str()`, `bool()`.
- Type mismatch can raise `TypeError`.
