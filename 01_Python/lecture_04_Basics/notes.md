# Python Operators - Structured Interview Notes

## 1. What Are Operators?

Operators are symbols used to perform operations on values or variables.

```python
a = 10
b = 5
result = a + b
```

Here:
- `+` is the operator.
- `a` and `b` are operands.

Operators are used for:
- Mathematical calculations
- Comparisons
- Logical decision-making

## 2. Main Types of Operators

| Type | Purpose |
|---|---|
| Arithmetic operators | Perform math operations |
| Comparison operators | Compare two values |
| Logical operators | Combine or invert conditions |

## 3. Arithmetic Operators

| Operator | Meaning | Example |
|---|---|---|
| `+` | Addition | `a + b` |
| `-` | Subtraction | `a - b` |
| `*` | Multiplication | `a * b` |
| `/` | Division | `a / b` |
| `//` | Floor division | `a // b` |
| `%` | Modulus (remainder) | `a % b` |
| `**` | Exponent (power) | `a ** b` |

Example:

```python
a = 10
b = 5

print(a + b)   # 15
print(a - b)   # 5
print(a * b)   # 50
print(a / b)   # 2.0
print(a // b)  # 2
print(a % b)   # 0
print(a ** b)  # 100000
```

## 4. Division vs Floor Division

Normal division (`/`): returns a float.

```python
print(21 / 5)   # 4.2
```

Floor division (`//`): returns integer quotient (floor value).

```python
print(21 // 5)  # 4
```

Use `//` when you only need the whole-number part.

## 5. Modulus Operator (`%`)

`%` returns the remainder after division.

```python
print(10 % 3)   # 1
```

Reason: `10 / 3` gives quotient `3` with remainder `1`.

## 6. Exponent Operator (`**`)

`**` is used for powers.

```python
print(2 ** 3)   # 8
```

This means `2` raised to the power `3`.

## 7. Comparison Operators

Comparison operators return Boolean results: `True` or `False`.

| Operator | Meaning |
|---|---|
| `==` | Equal to |
| `!=` | Not equal to |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal to |
| `<=` | Less than or equal to |

Examples:

```python
a = 10
b = 10
print(a == b)   # True

x = 45
y = 55
print(x > y)    # False
```

## 8. String Comparison

Comparison also works with strings.

```python
str1 = "Krish"
str2 = "Krish"
print(str1 == str2)   # True

str3 = "Krish"
str4 = "krish"
print(str3 == str4)   # False
```

String comparison is case-sensitive.

## 9. Logical Operators

| Operator | Meaning |
|---|---|
| `and` | `True` only if both conditions are `True` |
| `or` | `True` if at least one condition is `True` |
| `not` | Reverses `True` to `False` and vice versa |

### `and` Operator

```python
x = True
y = True
print(x and y)   # True

x = True
y = False
print(x and y)   # False
```

Truth table (`and`):

| A | B | A and B |
|---|---|---|
| True | True | True |
| True | False | False |
| False | True | False |
| False | False | False |

### `or` Operator

```python
x = True
y = False
print(x or y)    # True
```

Truth table (`or`):

| A | B | A or B |
|---|---|---|
| True | True | True |
| True | False | True |
| False | True | True |
| False | False | False |

### `not` Operator

```python
x = True
print(not x)     # False

x = False
print(not x)     # True
```

## 10. Example: Simple Calculator

```python
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)
print("Floor Division:", num1 // num2)
print("Modulus:", num1 % num2)
print("Exponent:", num1 ** num2)
```

## 11. Common Operator Error

Problem:

```python
"hello" + 5
```

This raises `TypeError` because Python cannot add `str` and `int` directly.

Fix:

```python
"hello" + str(5)
```

## 12. Most Common Interview Questions

Q1. What are operators in Python?  
A. Symbols used to perform operations on variables and values.

Q2. What are arithmetic operators?  
A. Operators used for mathematical calculations such as `+`, `-`, `*`, `/`, `//`, `%`, `**`.

Q3. Difference between `/` and `//`?  
A. `/` returns decimal (float) division, `//` returns floor (whole-number) division.

Q4. What does `%` do?  
A. Returns the remainder of division.

Q5. What does logical `and` do?  
A. Returns `True` only when both conditions are `True`.

## 13. Data Science Context

Operators are heavily used in filtering data.

```python
import pandas as pd

# Single condition
df[df["age"] > 30]

# Multiple conditions
df[(df["age"] > 30) & (df["salary"] > 50000)]
```

In filtering:
- `>` is a comparison operator.
- `&` combines multiple Boolean conditions.

## 14. Quick Revision Sheet

Arithmetic: `+`, `-`, `*`, `/`, `//`, `%`, `**`  
Comparison: `==`, `!=`, `>`, `<`, `>=`, `<=`  
Logical: `and`, `or`, `not`
