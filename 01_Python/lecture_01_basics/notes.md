# Python Basics Notes (Syntax and Semantics) - Interview Ready

## 1. Syntax vs Semantics

### Syntax
- Syntax is the set of rules for writing valid code.
- It defines code structure.

Example (valid syntax):

```python
age = 30
print(age)
```

Example (syntax error):

```python
if age > 30
    print(age)
```

Reason: missing `:` after condition.

Correct version:

```python
if age > 30:
    print(age)
```

Interview answer:
`Syntax defines the rules for writing valid code in a programming language.`

### Semantics
- Semantics is the meaning or behavior of code at runtime.
- Syntax = structure, semantics = meaning.

```python
x = 5
y = 10
z = x + y
```

Semantic meaning: the program adds `x` and `y`, then stores the result in `z`.

Interview answer:
`Semantics defines what code actually does when it executes.`

## 2. Comments in Python

- Comments improve readability and are ignored by the interpreter.

Single-line comment:

```python
# This is a comment
print("Hello")
```

Multi-line style (commonly used):

```python
"""
This is a multi-line comment style.
"""
```

Note: triple quotes create multi-line strings; they are often used like comments.

## 3. Case Sensitivity

- Python is case-sensitive.
- `name` and `Name` are different variables.

```python
name = "Krish"
Name = "Nick"

print(name)  # Krish
print(Name)  # Nick
```

Interview answer:
`Yes, Python is case-sensitive. Identifiers with different letter cases are different.`

## 4. Indentation (Very Important)

- Python uses indentation to define code blocks.
- No braces (`{}`) are used for block structure.

```python
age = 32

if age > 30:
    print(age)
```

Incorrect indentation:

```python
if age > 30:
print(age)
```

This raises `IndentationError`.

Interview answer:
`Indentation defines blocks in Python, such as if statements, loops, and functions.`

## 5. Variables

- A variable stores a value.
- Python determines type automatically.

```python
age = 32
name = "Krish"
```

## 6. Dynamic Typing

- Python is dynamically typed.
- You do not declare variable types explicitly.
- A variable can refer to different types over time.

```python
x = 10
x = "Krish"
```

Interview answer:
`Python is dynamically typed, so variable types are decided at runtime.`

## 7. Type Inference

- Python infers type from assigned value.

```python
age = 32
print(type(age))   # <class 'int'>

name = "Krish"
print(type(name))  # <class 'str'>
```

Interview answer:
`Type inference means Python automatically determines a variable's type from its value.`

## 8. Line Continuation

Use backslash for explicit continuation:

```python
total = 1 + 2 + 3 + 4 + \
        5 + 6 + 7
print(total)  # 28
```

Preferred style: parentheses.

```python
total = (
    1 + 2 + 3 +
    4 + 5 + 6
)
```

## 9. Multiple Statements on One Line

Allowed but usually not recommended:

```python
x = 5; y = 10; z = x + y
print(z)  # 15
```

## 10. Common Errors

| Error | Meaning |
|---|---|
| `SyntaxError` | Invalid code syntax |
| `IndentationError` | Wrong indentation |
| `NameError` | Variable not defined |
| `TypeError` | Unsupported data type operation |
| `ValueError` | Correct type but invalid value |

`NameError` example:

```python
a = b  # NameError: name 'b' is not defined
```

## 11. Nested Indentation Example

```python
if True:
    print("Correct indentation")

    if False:
        print("This will not print")

print("Outside block")
```

Output:

```text
Correct indentation
Outside block
```

## 12. Quick Interview Questions

Q1. What is syntax in Python?  
A. Rules for writing valid code.

Q2. What is semantics?  
A. Meaning/behavior of code during execution.

Q3. Is Python case-sensitive?  
A. Yes, `name` and `Name` are different identifiers.

Q4. Why is indentation important?  
A. It defines code blocks.

Q5. What is dynamic typing?  
A. Types are resolved at runtime; no explicit type declaration required.

Q6. What is type inference?  
A. Python infers variable type from assigned value.

## 13. Combined Example

```python
# User age example
age = 32

if age > 30:
    print("Age is greater than 30")

print("Program finished")
```

Output:

```text
Age is greater than 30
Program finished
```
