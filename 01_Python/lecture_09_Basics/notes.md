# Python Dictionaries — Complete Notes (Data Science Focus)

## Table of Contents
1. What is a Dictionary?
2. Key Properties
3. Creating Dictionaries
4. Accessing Elements
5. Modifying Dictionaries
6. Deleting Elements
7. Dictionary Methods
8. Copying Dictionaries
9. Iterating Over Dictionaries
10. Nested Dictionaries
11. Dictionary Comprehension
12. Real-World Applications
13. Quick Reference

---

## 1. What is a Dictionary?

A **dictionary** stores data in **key-value pairs** (like a real dictionary maps words to definitions).

### Structure
```python
student = {
    "name": "Krish",
    "age": 32,
    "grade": "A"
}
```

### Key-Value Concept
```
"name"  →  "Krish"
"age"   →  32
"grade" →  "A"
```

---

## 2. Key Properties

| Property | Meaning |
|----------|---------|
| **Key-Value Pair** | Data stored as key:value |
| **Unique Keys** | No duplicate keys allowed |
| **Mutable Values** | Values can change |
| **Immutable Keys** | Keys cannot change |
| **Key-Ordered** | Keys maintain insertion order (Python 3.7+) |

### Valid Key Types
- String
- Number
- Tuple

### Valid Value Types
- **Any data type** (string, number, list, tuple, another dict, etc.)

---

## 3. Creating Dictionaries

### Empty Dictionary

**Method 1:**
```python
student = {}
```

**Method 2:**
```python
student = dict()
```

### Dictionary with Values

```python
student = {
    "name": "Krish",
    "age": 32,
    "grade": "A"
}

print(student)
# Output: {'name': 'Krish', 'age': 32, 'grade': 'A'}
```

### Important Rule: Keys Must Be Unique

**Last value wins!**

```python
student = {
    "name": "Krish",
    "name": "Alex",    # Duplicate key!
    "age": 32
}

print(student)
# Output: {'name': 'Alex', 'age': 32}
# Latest value replaces previous value
```

---

## 4. Accessing Elements

### Method 1: Direct Access with []

```python
student = {
    "name": "Krish",
    "age": 32,
    "grade": "A"
}

print(student["grade"])
# Output: A
```

⚠️ **Error if key doesn't exist:**
```python
print(student["last_name"])  # KeyError!
```

### Method 2: Using get() Method (Safer)

```python
print(student.get("grade"))
# Output: A
```

**If key doesn't exist:**
```python
print(student.get("last_name"))
# Output: None
```

**With default value:**
```python
print(student.get("last_name", "Not Available"))
# Output: Not Available
```

| Scenario | `[]` | `.get()` |
|----------|------|---------|
| Key exists | Returns value | Returns value |
| Key missing | ❌ KeyError | ✅ Returns None |
| Key missing + default | — | ✅ Returns default |

---

## 5. Modifying Dictionaries

**Dictionaries are mutable!**

### Update Existing Value

```python
student = {"name": "Krish", "age": 32}
student["age"] = 33
print(student)
# Output: {'name': 'Krish', 'age': 33}
```

### Add New Key

```python
student["address"] = "India"
print(student)
# Output: {'name': 'Krish', 'age': 33, 'address': 'India'}
```

---

## 6. Deleting Elements

### Using del

```python
student = {
    "name": "Krish",
    "age": 33,
    "grade": "A",
    "address": "India"
}

del student["grade"]
print(student)
# Output: {'name': 'Krish', 'age': 33, 'address': 'India'}
```

### Using pop()

```python
value = student.pop("address")
print(value)  # Output: India
print(student)  # 'address' is removed
```

### Using clear()

```python
student.clear()
print(student)
# Output: {}
```

---

## 7. Dictionary Methods

### keys() — Get All Keys

```python
student = {
    "name": "Krish",
    "age": 33,
    "address": "India"
}

print(student.keys())
# Output: dict_keys(['name', 'age', 'address'])

# Convert to list
keys_list = list(student.keys())
print(keys_list)
# Output: ['name', 'age', 'address']
```

### values() — Get All Values

```python
print(student.values())
# Output: dict_values(['Krish', 33, 'India'])

# Convert to list
values_list = list(student.values())
print(values_list)
# Output: ['Krish', 33, 'India']
```

### items() — Get Key-Value Pairs

```python
print(student.items())
# Output: dict_items([('name', 'Krish'), ('age', 33), ('address', 'India')])

# Returns tuples!
for pair in student.items():
    print(pair, type(pair))
# Output: ('name', 'Krish') <class 'tuple'>
```

| Method | Returns | Type |
|--------|---------|------|
| `keys()` | All keys | dict_keys object |
| `values()` | All values | dict_values object |
| `items()` | Key-value pairs | dict_items object (tuples) |

---

## 8. Copying Dictionaries ⭐

### The Wrong Way (Shallow Reference)

```python
student = {"name": "Krish", "age": 32}
copy_student = student

# Problem: Both refer to same memory!
student["name"] = "New Name"

print(copy_student)
# Output: {'name': 'New Name', 'age': 32}
# copy_student changed too! ❌
```

### The Correct Way (Deep Copy)

```python
student = {"name": "Krish", "age": 32}
copy_student = student.copy()

# Now they have separate memory
student["name"] = "New Name"

print(student)
# Output: {'name': 'New Name', 'age': 32}

print(copy_student)
# Output: {'name': 'Krish', 'age': 32} ✅
```

---

## 9. Iterating Over Dictionaries

### Iterate Over Keys

```python
student = {
    "name": "Krish",
    "age": 33,
    "address": "India"
}

for key in student.keys():
    print(key)
```

Output:
```
name
age
address
```

### Iterate Over Values

```python
for value in student.values():
    print(value)
```

Output:
```
Krish
33
India
```

### Iterate Over Key-Value Pairs (Most Common)

```python
for key, value in student.items():
    print(f"{key}: {value}")
```

Output:
```
name: Krish
age: 33
address: India
```

---

## 10. Nested Dictionaries

### Creating Nested Dictionaries

Dictionary inside a dictionary:

```python
students = {
    "student1": {
        "name": "Chris",
        "age": 32
    },
    "student2": {
        "name": "Peter",
        "age": 35
    }
}
```

### Accessing Nested Values

```python
# Access value in nested dictionary
print(students["student2"]["name"])
# Output: Peter

print(students["student1"]["age"])
# Output: 32
```

### Iterating Over Nested Dictionaries

```python
for id, info in students.items():
    print(f"ID: {id}")
    for key, value in info.items():
        print(f"  {key}: {value}")
```

Output:
```
ID: student1
  name: Chris
  age: 32
ID: student2
  name: Peter
  age: 35
```

---

## 11. Dictionary Comprehension

### Basic Dictionary Comprehension

Similar to list comprehension!

```python
# Create a mapping of numbers to their squares
squares = {x: x**2 for x in range(5)}

print(squares)
# Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

### With Condition

```python
# Even numbers only
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}

print(even_squares)
# Output: {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}
```

### With Key Transformation

```python
# Map strings to their lengths
words = ["hello", "world", "python"]
word_lengths = {word: len(word) for word in words}

print(word_lengths)
# Output: {'hello': 5, 'world': 5, 'python': 6}
```

---

## 12. Real-World Applications

### Example 1: Frequency Counter ⭐

**Very common data science interview question!**

```python
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

print(frequency)
# Output: {1: 1, 2: 2, 3: 3, 4: 4}
```

**Used in:**
- Word frequency analysis
- Data distribution analysis
- Feature engineering

### Example 2: Mapping Data

```python
user_mapping = {
    101: "John",
    102: "Jane",
    103: "Bob"
}

# Quickly find user
print(user_mapping[102])
# Output: Jane
```

### Example 3: JSON Data (From APIs)

```python
# JSON response from API
user_data = {
    "user_id": 101,
    "name": "Shiv",
    "age": 30,
    "email": "shiv@example.com"
}

# Access data like a dictionary
print(user_data["name"])
# Output: Shiv
```

---

## 13. Merging Dictionaries

### Using ** Operator

```python
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

merged = {**dict1, **dict2}

print(merged)
# Output: {'a': 1, 'b': 3, 'c': 4}
# Note: 'b' from dict2 (latest value) overwrites dict1
```

### Using update() Method

```python
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

dict1.update(dict2)
print(dict1)
# Output: {'a': 1, 'b': 3, 'c': 4}
# dict1 is modified!
```

---

## Quick Reference Sheet

| Operation | Syntax | Example |
|-----------|--------|---------|
| **Create** | `{}` or `dict()` | `d = {"name": "Krish"}` |
| **Access** | `d[key]` | `d["name"]` |
| **Access safe** | `d.get(key)` | `d.get("name", "N/A")` |
| **Add/Update** | `d[key] = value` | `d["age"] = 32` |
| **Delete** | `del d[key]` | `del d["age"]` |
| **Get keys** | `d.keys()` | `list(d.keys())` |
| **Get values** | `d.values()` | `list(d.values())` |
| **Get pairs** | `d.items()` | `list(d.items())` |
| **Copy** | `d.copy()` | `copy_d = d.copy()` |
| **Iterate** | `for k, v in d.items()` | Loop through pairs |
| **Merge** | `{**d1, **d2}` | Combine dictionaries |

---

## Data Structures Comparison

| Structure | Ordered | Mutable | Duplicates | Use Case |
|-----------|---------|---------|-----------|----------|
| **List** | ✅ Yes | ✅ Yes | ✅ Allowed | Ordered data |
| **Tuple** | ✅ Yes | ❌ No | ✅ Allowed | Fixed data |
| **Set** | ❌ No | ✅ Yes | ❌ Not allowed | Unique items |
| **Dictionary** | ✅ Key-ordered | ✅ Yes | Keys unique | Key-value mapping |

---

## Why Dictionaries Are Critical in Data Science ⭐

Dictionaries are **everywhere** in data science:

- **JSON data** — APIs return JSON (which is basically a dictionary)
- **Pandas DataFrames** — Each row can be accessed as a dictionary
- **ML datasets** — Features and labels stored as dictionaries
- **Feature mappings** — Map categories to numerical values
- **Configuration files** — Store parameters and settings
- **Data preprocessing** — Frequency counts, mappings, lookups

### Example: Typical Data Science Dictionary Use

```python
# Feature mapping (one-hot encoding alternative)
color_map = {
    "red": 1,
    "green": 2,
    "blue": 3
}

# JSON from API
user_response = {
    "user_id": 101,
    "name": "Shiv",
    "email": "shiv@example.com"
}

# Frequency analysis
word_count = {
    "python": 15,
    "data": 12,
    "science": 10
}
```

---

## Most Important Concept

**Dictionary is the most important Python data structure for Data Science** because:

✅ **JSON equivalence** — JSON is dictionary-like  
✅ **Data access** — Fast **O(1)** lookups  
✅ **Flexibility** — Store any combination of data types  
✅ **Real-world standard** — Every API, database, and tool uses it  
✅ **Common operations** — Frequency counting, mapping, grouping