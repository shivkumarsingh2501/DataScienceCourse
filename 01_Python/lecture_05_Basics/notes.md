# Python Loops — Interview Ready Notes

## Table of Contents
1. What are Loops?
2. Types of Loops
3. For Loop
4. Range Function
5. While Loop
6. Loop Control Statements
7. Nested Loops
8. Practical Examples

---

## 1. What are Loops?

**Definition:** Loops allow a program to execute a block of code multiple times.

**Purpose:** Instead of writing repetitive code, loops automate repetition.

**Example Problem:** Print numbers from 1 to 10
- Without loop → 10 print statements ❌
- With loop → 1 loop ✅

---

## 2. Types of Loops in Python

| Loop Type | Purpose |
|-----------|---------|
| **For Loop** | Iterate over sequences |
| **While Loop** | Run until condition becomes false |

### Loop Control Statements
- `break` — Stop the loop immediately
- `continue` — Skip current iteration
- `pass` — Placeholder (do nothing)

---

## 3. For Loop

### Definition
A for loop is used to iterate over a sequence such as:
- list
- string
- range
- dictionary
- tuple

### Syntax
```python
for variable in sequence:
    statement
```

### Example
```python
for i in range(5):
    print(i)
```

**Output:**
```
0
1
2
3
4
```

---

## 4. Range Function

### Definition
`range()` generates a sequence of numbers.

### Syntax
```python
range(start, stop, step)
```

| Parameter | Meaning |
|-----------|---------|
| `start` | Starting number (default: 0) |
| `stop` | Ending number (excluded) |
| `step` | Increment value (default: 1) |

### Examples

**Basic Range (0 to 4):**
```python
for i in range(5):
    print(i)
```
Output: `0 1 2 3 4` (Note: 5 is not included)

**Range with Start and Stop (1 to 5):**
```python
for i in range(1, 6):
    print(i)
```
Output: `1 2 3 4 5`

**Range with Step (increment by 2):**
```python
for i in range(1, 10, 2):
    print(i)
```
Output: `1 3 5 7 9`

**Reverse Loop:**
```python
for i in range(10, 0, -1):
    print(i)
```
Output: `10 9 8 7 6 5 4 3 2 1`

### Loop Through String

Strings are collections of characters.

```python
name = "Krish"
for char in name:
    print(char)
```

Output:
```
K
r
i
s
h
```

---

## 5. While Loop

### Definition
A while loop runs until the condition becomes false.

### Syntax
```python
while condition:
    statement
```

### Example
```python
count = 0
while count < 5:
    print(count)
    count = count + 1
```

Output:
```
0
1
2
3
4
```

### Important Rule ⚠️
**Always update the variable inside the loop**, otherwise you'll create an infinite loop.

**Bad Example (Infinite Loop):**
```python
while True:
    print("Hello")  # Runs forever!
```

---

## 6. Loop Control Statements

### Break Statement
`break` stops the loop immediately.

```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

Output:
```
0
1
2
3
4
```
Loop stops when i = 5.

### Continue Statement
`continue` skips the current iteration.

**Example:** Print only odd numbers
```python
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
```

Output:
```
1
3
5
7
9
```

### Pass Statement
`pass` does nothing. Used as a placeholder.

```python
for i in range(5):
    if i == 3:
        pass
    print(i)
```

Output:
```
0
1
2
3
4
```

---

## 7. Nested Loops

**Definition:** A loop inside another loop.

```python
for i in range(3):
    for j in range(2):
        print(f"i = {i} j = {j}")
```

Output:
```
i = 0 j = 0
i = 0 j = 1
i = 1 j = 0
i = 1 j = 1
i = 2 j = 0
i = 2 j = 1
```

---

## 8. Practical Examples

### Example 1: Sum of Natural Numbers

**Using While Loop:**
```python
n = 10
sum = 0
count = 1

while count <= n:
    sum = sum + count
    count += 1

print(sum)  # Output: 55
```

**Using For Loop:**
```python
sum = 0
for i in range(1, 11):
    sum = sum + i

print(sum)  # Output: 55
```

### Example 2: Prime Numbers

**Problem:** Print prime numbers between 1–100

```python
for num in range(1, 101):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)
```

Output: `2 3 5 7 11 13 17 19 23 ...`
Most Common Python Loop Interview Questions
Q1 What is a loop?

A loop executes a block of code repeatedly.

Q2 Difference between for loop and while loop?
For Loop	While Loop
Used for sequences	Used for conditions
Fixed iterations	Unknown iterations
Q3 What does break do?

Stops loop immediately.

Q4 What does continue do?

Skips current iteration.

Q5 What does pass do?

Null operation (does nothing).

Data Science Use of Loops

Loops are used in:

data cleaning
model training
feature engineering
data processing

Example:

for column in dataframe.columns:
    print(column)

Used frequently in Pandas and ML pipelines.

Quick Revision Sheet
Loop Types
for loop
while loop
Loop Control
break
continue
pass
Range
range(start, stop, step)
Important Next Topic in Your Course

The next Python topics will become extremely important for Data Science:

Strings
Lists
Tuples
Sets
Dictionaries
Functions

Especially:

Lists
Dictionaries

These are used heavily in NumPy and Pandas.