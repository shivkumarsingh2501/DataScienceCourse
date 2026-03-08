# Python Tuples — Complete Notes (Data Science Focus)

## Table of Contents
1. What is a Tuple?
2. List vs Tuple (Important Differences)
3. Creating a Tuple
4. Multiple Data Types
5. Accessing Elements
6. Tuple Slicing
7. Tuple Operations
8. Immutable Nature
9. Tuple Methods
10. Tuple Packing & Unpacking
11. Nested Tuples
12. Real-World Applications

---

## 1. What is a Tuple?

A **tuple** is a Python data structure with these properties:

| Property | Meaning |
|----------|---------|
| **Ordered** | Elements maintain their order |
| **Immutable** | Cannot modify elements after creation |
| **Collection** | Stores multiple values |

---

## 2. List vs Tuple (Important Differences)

| Feature | List | Tuple |
|---------|------|-------|
| **Syntax** | `[ ]` | `( )` |
| **Mutable** | ✅ Yes | ❌ No |
| **Speed** | Slower | Faster |
| **Use Case** | Data manipulation | Fixed data |

### Example
```python
my_list = [1, 2, 3]
my_tuple = (1, 2, 3)
```

---

## 3. Creating a Tuple

### Empty Tuple
```python
t = ()
print(type(t))
# Output: <class 'tuple'>
```

### Using tuple() Function
```python
t = tuple()
```

### Convert List to Tuple
```python
numbers = tuple([1, 2, 3, 4, 5])
print(numbers)
# Output: (1, 2, 3, 4, 5)
```

### Convert Tuple to List
```python
numbers = (1, 2, 3, 4)
list_numbers = list(numbers)
print(list_numbers)
# Output: [1, 2, 3, 4]
```

---

## 4. Multiple Data Types in One Tuple

Tuples can store **any data type**:

```python
mixed_tuple = (1, "Hello", 3.14, True)
print(mixed_tuple)
# Output: (1, 'Hello', 3.14, True)
```

---

## 5. Accessing Tuple Elements

### Same as List Indexing
```python
numbers = (1, 2, 3, 4, 5, 6)

# First element
print(numbers[0])
# Output: 1

# Last element
print(numbers[-1])
# Output: 6
```

---

## 6. Tuple Slicing

### Syntax
```python
tuple[start:end]
```

### Examples

**Basic slicing:**
```python
numbers = (1, 2, 3, 4, 5, 6)
print(numbers[0:4])
# Output: (1, 2, 3, 4)
```

**Reverse tuple:**
```python
print(numbers[::-1])
# Output: (6, 5, 4, 3, 2, 1)
```

---

## 7. Tuple Operations

### Concatenation
```python
tuple1 = (1, 2, 3)
tuple2 = ("A", "B")

result = tuple1 + tuple2
print(result)
# Output: (1, 2, 3, 'A', 'B')
```

### Repetition
```python
t = (1, 2)
print(t * 3)
# Output: (1, 2, 1, 2, 1, 2)
```

---

## 8. Immutable Nature of Tuple ⭐

**This is the main difference from lists!**

### List Example (Mutable)
```python
my_list = [1, 2, 3]
my_list[0] = 10
print(my_list)
# Output: [10, 2, 3] ✅ Works!
```

### Tuple Example (Immutable)
```python
my_tuple = (1, 2, 3)
my_tuple[0] = 10
# Output: TypeError ❌ Cannot modify!
```

### How to Modify a Tuple (Workaround)

Convert → Modify → Convert back:

```python
t = (1, 2, 3)

# Convert to list
temp = list(t)

# Modify
temp[0] = 10

# Convert back to tuple
t = tuple(temp)
print(t)
# Output: (10, 2, 3)
```

---

## 9. Tuple Methods

Tuples have only **2 built-in methods**:

### count()
Counts occurrences of an element.

```python
numbers = (1, 2, 3, 1, 1)
print(numbers.count(1))
# Output: 3
```

### index()
Returns the index of the first occurrence.

```python
numbers = (1, 2, 3, 4)
print(numbers.index(3))
# Output: 2
```

---

## 10. Tuple Packing & Unpacking

### Packing

Storing values in a tuple automatically:

```python
# Explicit
packed_tuple = (1, "Hello", 3.14)

# Implicit (no parentheses needed)
packed_tuple = 1, "Hello", 3.14

print(packed_tuple)
# Output: (1, 'Hello', 3.14)
```

### Unpacking

Extracting tuple values into variables:

```python
t = (1, "Hello", 3.14)

a, b, c = t

print(a)  # Output: 1
print(b)  # Output: Hello
print(c)  # Output: 3.14
```

### Unpacking with `*` (Advanced)

Used when tuple has many values:

```python
numbers = (1, 2, 3, 4, 5, 6)

first, *middle, last = numbers

print(first)   # Output: 1
print(middle)  # Output: [2, 3, 4, 5]
print(last)    # Output: 6
```

**Note:** `*middle` captures middle values as a list.

---

## 11. Nested Tuples

### Creating Nested Tuples

Tuple inside a tuple:

```python
nested_tuple = ((1, 2, 3), ('A', 'B', 'C'), (True, False))
```

### Accessing Nested Elements

**First inner tuple:**
```python
print(nested_tuple[0])
# Output: (1, 2, 3)
```

**Specific element inside nested tuple:**
```python
print(nested_tuple[1][2])
# Output: 'C'
```

### Iterating Over Nested Tuples

```python
nested = ((1, 2, 3), ('A', 'B', 'C'), (True, False))

for sub_tuple in nested:
    for item in sub_tuple:
        print(item)
```

Output:
```
1
2
3
A
B
C
True
False
```

---

## 12. Real-World Applications

### Where Tuples Are Used in Data Science

- **Returning multiple values** from functions
- **Dictionary keys** (tuples can be keys, lists cannot)
- **Fixed configuration data**
- **Coordinates** (x, y) or (x, y, z)
- **Database records**

### Example: Return Multiple Values

```python
def get_coordinates():
    return (10, 20)

x, y = get_coordinates()
print(x, y)
# Output: 10 20
```

### Why Use Tuples?

✅ **Faster** than lists  
✅ **Immutable** — safe from accidental changes  
✅ **Can be dictionary keys**  
✅ **Memory efficient**  
❌ Cannot modify after creation

---

## Quick Reference Sheet

| Operation | Syntax |
|-----------|--------|
| **Create** | `t = (1, 2, 3)` |
| **Access** | `t[0]` |
| **Slice** | `t[start:end]` |
| **Count** | `t.count(value)` |
| **Index** | `t.index(value)` |
| **Pack** | `t = 1, 2, 3` |
| **Unpack** | `a, b, c = t` |
| **Concatenate** | `t1 + t2` |
| **Repeat** | `t * 3` |

---

## Key Takeaways

1. **Immutable** — Cannot change elements (unlike lists)
2. **Faster** — Better performance than lists
3. **Unpacking** — Powerful feature for multiple assignments
4. **Dictionary keys** — Tuples can be dict keys, lists cannot
5. **Use in functions** — Perfect for returning multiple values
Operations
+
*
slicing
Important Concept

The most important thing from this lecture is:

Tuple = Immutable List