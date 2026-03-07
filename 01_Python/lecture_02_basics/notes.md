# Python Variables - Structured Interview Notes

## 1. What Is a Variable?

A variable is a named reference to a value in memory.

In Python:
- A variable is created when you assign a value.
- You do not declare its type explicitly.

```python
a = 100
```

Here:
- `a` is the variable name.
- `100` is the value.

Real examples:

```python
age = 32
height = 6.1
name = "Krish"
is_student = True
```

## 2. Declaring and Assigning Variables

Use the assignment operator `=`.

```python
age = 32
height = 6.1
name = "Krish"
is_student = True
```

Printing variables:

```python
print(age)
print(height)
print(name)
```

Readable output:

```python
print("Age:", age)
print("Height:", height)
print("Name:", name)
```

## 3. Variable Naming Rules

### Rules
1. Must start with a letter (`a-z`, `A-Z`) or underscore (`_`).
2. Can contain letters, numbers, and underscores.
3. Cannot start with a number.
4. Cannot contain special symbols like `-`, `@`, `%`.
5. Variable names are case-sensitive (`name` and `Name` are different).
6. Cannot use Python keywords like `if`, `for`, `class`.

Valid examples:

```python
name = "Krish"
_age = 25
first_name = "Krish"
age1 = 30
student_id = 101
```

Invalid examples:

```python
1age = 30        # starts with number
first-name = "A" # contains '-'
@name = "A"      # contains '@'
```

Interview answer:
`A Python variable name must start with a letter or underscore, cannot start with a number, cannot contain special characters, and is case-sensitive.`

## 4. Common Variable Types

| Type | Example |
|---|---|
| `int` | `25` |
| `float` | `6.1` |
| `str` | `"Krish"` |
| `bool` | `True`, `False` |

```python
age = 25
height = 6.1
name = "Krish"
is_student = True
```

## 5. Type Checking

Use `type()` to inspect the data type.

```python
age = 25
print(type(age))      # <class 'int'>

name = "Krish"
print(type(name))     # <class 'str'>
```

## 6. Type Conversion (Type Casting)

### int to str

```python
age = 25
age_str = str(age)
print(type(age_str))  # <class 'str'>
```

### str to int

```python
age = "25"
age_int = int(age)
print(type(age_int))  # <class 'int'>
```

### float to int

```python
height = 5.9
print(int(height))    # 5
```

Note: converting `float` to `int` truncates the decimal part.

Invalid conversion:

```python
name = "Krish"
int(name)             # ValueError
```

## 7. Dynamic Typing

Python is dynamically typed: the same variable can hold different types at different times.

```python
var = 10
print(type(var))      # <class 'int'>

var = "Hello"
print(type(var))      # <class 'str'>

var = 3.14
print(type(var))      # <class 'float'>
```

Interview answer:
`In Python, variable types are determined at runtime and can change during execution.`

## 8. Taking User Input

Use `input()` to read user input.

```python
age = input("Enter your age: ")
print(age)
print(type(age))      # <class 'str'>
```

Important: `input()` always returns a string.

Convert input when needed:

```python
age = int(input("Enter your age: "))
print(type(age))      # <class 'int'>
```

## 9. Example: Simple Calculator

```python
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

total = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1 / num2

print("Sum:", total)
print("Difference:", difference)
print("Product:", product)
print("Division:", quotient)
```

## 10. Common Python Errors

| Error | Example | Reason |
|---|---|---|
| `NameError` | `a = b` | `b` is not defined |
| `ValueError` | `int("Krish")` | invalid conversion to integer |
| `SyntaxError` | `if age > 30` | missing `:` |

## 11. Most Common Interview Questions

Q1. What is a variable?  
A. A named container/reference used to store data values.

Q2. How do you declare variables in Python?  
A. By assignment using `=` (for example, `age = 25`).

Q3. What is dynamic typing?  
A. Python decides types at runtime, and a variable can change type later.

Q4. What does `type()` do?  
A. Returns the data type of a value or variable.

Q5. What does `input()` return?  
A. It always returns a string.

## 12. Data Science Context

Variables are used heavily in:
- Pandas DataFrames
- Machine learning models
- Data preprocessing pipelines
- Feature engineering

```python
import pandas as pd

data = pd.read_csv("data.csv")
```

Here, `data` is a variable storing a dataset.

## 13. Naming Best Practices

Use `snake_case` in professional Python code.

Good names:
- `student_name`
- `total_salary`
- `model_accuracy`

Avoid unclear names:
- `x`
- `data1`
- `StudentName` (for normal variable names)

## 14. Quick Revision Sheet

- Variable -> stores a value.
- `type()` -> checks data type.
- `input()` -> reads user input (string).
- Dynamic typing -> variable type can change at runtime.
- Type casting -> converts one type to another.
