# Python Lists (Data Structures) — Complete Notes

## Table of Contents
1. What is a List?
2. Creating a List
3. Multiple Data Types
4. Accessing Elements (Indexing)
5. Negative Indexing
6. List Slicing
7. Modifying Elements
8. Important List Methods
9. Advanced Slicing
10. Iterating Over Lists
11. List Comprehension
12. Quick Reference & Interview Tips

---

## 1. What is a List?

A **list** is a Python data structure with these properties:

| Property | Meaning |
|----------|---------|
| **Ordered** | Elements keep their order |
| **Mutable** | Elements can be changed/modified |
| **Collection** | Can store multiple values |

---

## 2. Creating a List

### Empty List
```python
my_list = []
print(type(my_list))
```
Output: `<class 'list'>`

### List with Values
```python
names = ["Krish", "Jack", "Jacob"]
print(names)
```
Output: `['Krish', 'Jack', 'Jacob']`

---

## 3. Multiple Data Types in One List

Lists can store **any data type**:

```python
mixed_list = [1, "Hello", 3.5, True]
print(mixed_list)
```
Output: `[1, 'Hello', 3.5, True]`

---

## 4. Accessing List Elements (Indexing)

### Understanding Indexing
```
Index:  0        1        2       3       4
      apple   banana   cherry   kiwi   guava
```

### Examples
```python
fruits = ["apple", "banana", "cherry", "kiwi", "guava"]

# First element
print(fruits[0])    # Output: apple

# Middle element
print(fruits[2])    # Output: cherry
```

---

## 5. Negative Indexing

Negative indexing starts from the **end** of the list:

```
Index:  -5       -4       -3      -2      -1
      apple   banana   cherry   kiwi   guava
```

### Example
```python
fruits = ["apple", "banana", "cherry", "kiwi", "guava"]
print(fruits[-1])   # Output: guava (last element)
```

---

## 6. List Slicing

### Syntax
```python
list[start:end]
```

### Important Rule ⚠️
**The end index is NOT included.**

### Examples

**From index 1 to end:**
```python
print(fruits[1:])
# Output: ['banana', 'cherry', 'kiwi', 'guava']
```

**Specific range:**
```python
print(fruits[1:3])
# Output: ['banana', 'cherry']
```

---

## 7. Modifying List Elements

Lists are **mutable**, so we can change elements:

```python
fruits = ["apple", "banana", "cherry", "kiwi", "guava"]
fruits[1] = "watermelon"
print(fruits)
# Output: ['apple', 'watermelon', 'cherry', 'kiwi', 'guava']
```

---

## 8. Important List Methods

| Method | Purpose | Example |
|--------|---------|---------|
| **append()** | Add element at end | `fruits.append("orange")` |
| **insert()** | Insert at specific index | `fruits.insert(1, "watermelon")` |
| **remove()** | Remove first occurrence | `fruits.remove("banana")` |
| **pop()** | Remove last element | `fruits.pop()` |
| **index()** | Find index of element | `fruits.index("cherry")` → `2` |
| **count()** | Count occurrences | `fruits.count("banana")` |
| **sort()** | Sort list | `fruits.sort()` |
| **reverse()** | Reverse order | `fruits.reverse()` |
| **clear()** | Remove all elements | `fruits.clear()` → `[]` |

### Examples

```python
fruits = ["apple", "banana", "cherry"]

# append()
fruits.append("orange")
# ['apple', 'banana', 'cherry', 'orange']

# insert()
fruits.insert(1, "watermelon")
# ['apple', 'watermelon', 'banana', 'cherry', 'orange']

# remove()
fruits.remove("banana")

# sort()
fruits.sort()
# Output: ['apple','cherry','orange','watermelon']
```

---

## 9. Advanced Slicing

### Setup
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

### Slicing Examples

**Specific range:**
```python
numbers[2:5]    # Output: [3, 4, 5]
```

**Start to specific index:**
```python
numbers[:5]     # Output: [1, 2, 3, 4, 5]
```

**From index to end:**
```python
numbers[5:]     # Output: [6, 7, 8, 9, 10]
```

### Step Slicing

**Syntax:** `[start:end:step]`

**Every 2nd element:**
```python
numbers[::2]    # Output: [1, 3, 5, 7, 9]
```

**Reverse list:**
```python
numbers[::-1]   # Output: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
```

---

## 10. Iterating Over Lists

### Simple Loop
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

### With Index using enumerate()
```python
for index, fruit in enumerate(fruits):
    print(index, fruit)
```

Output:
```
0 apple
1 banana
2 cherry
```

---

## 11. List Comprehension ⭐ (Most Important)

### What is it?
A **powerful Python feature** to create lists in a single line instead of loops.

### Before (Multiple lines):
```python
squares = []
for x in range(10):
    squares.append(x**2)
print(squares)
```

### After (One line):
```python
squares = [x**2 for x in range(10)]
print(squares)
# Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

### With Condition
```python
# Get only even numbers
even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)
# Output: [0, 2, 4, 6, 8]
```

### Nested List Comprehension
```python
list1 = [1, 2, 3]
list2 = ['A', 'B', 'C']

pairs = [(i, j) for i in list1 for j in list2]
print(pairs)
# Output: [(1,'A'), (1,'B'), (1,'C'), 
#          (2,'A'), (2,'B'), (2,'C'), 
#          (3,'A'), (3,'B'), (3,'C')]
```

### Using Functions
```python
words = ["hello", "world", "python"]
lengths = [len(word) for word in words]
print(lengths)
# Output: [5, 5, 6]
```

---

## 12. Quick Reference & Interview Tips

### Quick Revision Sheet

| Operation | Syntax |
|-----------|--------|
| **Create** | `my_list = []` or `[1, 2, 3]` |
| **Access** | `my_list[0]` |
| **Append** | `my_list.append(x)` |
| **Insert** | `my_list.insert(index, value)` |
| **Remove** | `my_list.remove(x)` |
| **Pop** | `my_list.pop()` |
| **Index** | `my_list.index(x)` |
| **Slice** | `my_list[start:end:step]` |

### Why Lists Matter in Data Science

Lists are used for:
- Data storage
- Data cleaning
- Feature lists
- Iteration over datasets

**Example:**
```python
columns = ["age", "salary", "experience"]
for column in columns:
    print(column)
```

### Most Important Concept ⭐

**List Comprehension** — You'll see it **everywhere** in Data Science code!

```python
[x for x in dataset if x > 10]
```

### Next Data Structures in Your Course

Krish Naik will teach you:
- Tuples
- Sets
- **Dictionaries** ⭐ (Most important for Data Science)

**Why Dictionaries are Important:**
- JSON (API data)
- Pandas (DataFrames)
- ML datasets
- API responses