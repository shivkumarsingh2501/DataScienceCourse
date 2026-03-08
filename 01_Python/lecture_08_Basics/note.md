# Python Sets — Complete Notes (Data Science Focus)

## Table of Contents
1. What is a Set?
2. Creating a Set
3. Remove Duplicates
4. Adding & Removing Elements
5. Membership Testing
6. Mathematical Set Operations
7. Subset & Superset
8. Real-World Applications
9. Data Structures Comparison
10. Quick Reference

---

## 1. What is a Set?

A **set** is a built-in Python data structure with these key properties:

| Property | Meaning |
|----------|---------|
| **Unique** | Duplicate values automatically removed |
| **Unordered** | No fixed order of elements |
| **Mutable** | Can add/remove elements |
| **Fast lookup** | Very fast for membership testing |

### Example
```python
my_set = {1, 2, 3, 4}
print(type(my_set))
# Output: <class 'set'>
```

---

## 2. Creating a Set

### Using Curly Braces
```python
my_set = {1, 2, 3, 4, 5}
print(type(my_set))
# Output: <class 'set'>
```

### Creating an Empty Set ⚠️

**Common Beginner Mistake:**
```python
empty_set = {}  # This creates a dictionary, NOT a set!
```

**Correct Way:**
```python
empty_set = set()
print(type(empty_set))
# Output: <class 'set'>
```

---

## 3. Remove Duplicates from Lists

### Converting List to Set

**Very useful for data cleaning!**

```python
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers)
print(unique_numbers)
# Output: {1, 2, 3, 4, 5}
```

### Automatic Duplicate Removal

Duplicates are **automatically removed** when creating a set:

```python
s = {1, 2, 3, 4, 5, 5, 6, 6}
print(s)
# Output: {1, 2, 3, 4, 5, 6}
```

---

## 4. Adding & Removing Elements

### Adding Elements with add()

```python
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)
# Output: {1, 2, 3, 4}

# Adding duplicate (nothing happens)
my_set.add(3)
print(my_set)
# Output: {1, 2, 3, 4}
```

### Removing Elements with remove()

```python
my_set = {1, 2, 3, 4, 5}
my_set.remove(3)
print(my_set)
# Output: {1, 2, 4, 5}

# Trying to remove non-existent element
my_set.remove(10)  # ❌ KeyError!
```

### Safer Removal with discard()

```python
my_set = {1, 2, 3, 4, 5}
my_set.discard(10)  # ✅ No error!
print(my_set)
# Output: {1, 2, 3, 4, 5}
```

| Method | If Element Doesn't Exist |
|--------|--------------------------|
| `remove()` | ❌ Raises KeyError |
| `discard()` | ✅ Does nothing |

### Removing Random Element with pop()

```python
my_set = {1, 2, 3, 4, 5}
my_set.pop()  # Removes random element (unordered)
print(my_set)
# Output: {1, 2, 3, 4}  or {1, 2, 3, 5} etc.
```

### Clearing the Set

```python
my_set = {1, 2, 3, 4, 5}
my_set.clear()
print(my_set)
# Output: set()
```

---

## 5. Membership Testing ⭐

**Sets are extremely fast for checking membership!**

```python
my_set = {1, 2, 3, 4, 5}

# Check if element exists
print(3 in my_set)
# Output: True

print(10 in my_set)
# Output: False

# Check if element doesn't exist
print(10 not in my_set)
# Output: True
```

**Why this matters:** Sets use hash tables, making membership tests **O(1)** instead of **O(n)** like lists!

---

## 6. Mathematical Set Operations

### Union (Combine Both Sets)

```python
set1 = {1, 2, 3, 4, 5, 6}
set2 = {4, 5, 6, 7, 8, 9}

union_set = set1.union(set2)
print(union_set)
# Output: {1, 2, 3, 4, 5, 6, 7, 8, 9}

# Alternative syntax
union_set = set1 | set2
```

### Intersection (Common Elements)

```python
intersection_set = set1.intersection(set2)
print(intersection_set)
# Output: {4, 5, 6}

# Alternative syntax
intersection_set = set1 & set2
```

### Intersection Update

Updates the original set:

```python
set1 = {1, 2, 3, 4, 5, 6}
set2 = {4, 5, 6, 7, 8, 9}

set1.intersection_update(set2)
print(set1)
# Output: {4, 5, 6}  (set1 is modified!)
```

### Difference (Elements Only in set1)

```python
difference_set = set1.difference(set2)
print(difference_set)
# Output: {1, 2, 3}

# Alternative syntax
difference_set = set1 - set2
```

### Difference Update

Updates the original set:

```python
set1.difference_update(set2)
print(set1)
# Output: {1, 2, 3}
```

### Symmetric Difference (Not Common)

```python
sym_diff = set1.symmetric_difference(set2)
print(sym_diff)
# Output: {1, 2, 3, 7, 8, 9}
# (Elements in either set but not in both)

# Alternative syntax
sym_diff = set1 ^ set2
```

---

## 7. Subset & Superset

### Subset

Check if one set is inside another:

```python
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}

print(set1.issubset(set2))
# Output: True

print(set2.issubset(set1))
# Output: False
```

### Superset

Opposite of subset:

```python
print(set2.issuperset(set1))
# Output: True

print(set1.issuperset(set2))
# Output: False
```

---

## 8. Real-World Applications

### Example 1: Remove Duplicates from List

**Common data science interview question:**

```python
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = list(set(numbers))
print(unique_numbers)
# Output: [1, 2, 3, 4, 5]
```

### Example 2: Count Unique Words

```python
text = "in this tutorial we are discussing about sets"
words = text.split()
unique_words = set(words)

print(unique_words)
# Output: {'tutorial', 'we', 'are', 'sets', 'about', 'in', 'this', 'discussing'}

print(f"Total words: {len(words)}")
print(f"Unique words: {len(unique_words)}")
# Output: Total words: 8
#         Unique words: 8
```

**Used in:**
- NLP (Natural Language Processing)
- Text analysis
- Word frequency counting

### Example 3: Finding Common Users

```python
users_day1 = {"Alice", "Bob", "Charlie", "David"}
users_day2 = {"Charlie", "David", "Eve"}

common_users = users_day1.intersection(users_day2)
print(common_users)
# Output: {'Charlie', 'David'}

new_users = users_day2.difference(users_day1)
print(new_users)
# Output: {'Eve'}
```

**Used in:**
- User analytics
- Recommendation systems
- Data cleaning

---

## 9. Data Structures Comparison

| Structure | Ordered | Mutable | Duplicates |
|-----------|---------|---------|-----------|
| **List** | ✅ Yes | ✅ Yes | ✅ Allowed |
| **Tuple** | ✅ Yes | ❌ No | ✅ Allowed |
| **Set** | ❌ No | ✅ Yes | ❌ Not allowed |
| **Dictionary** | ✅ Key ordered | ✅ Yes | Keys unique |

---

## 10. Quick Reference

### Set Methods

| Method | Purpose | Example |
|--------|---------|---------|
| `add()` | Add element | `my_set.add(5)` |
| `remove()` | Remove element (error if missing) | `my_set.remove(5)` |
| `discard()` | Remove element (no error) | `my_set.discard(5)` |
| `pop()` | Remove random element | `my_set.pop()` |
| `clear()` | Remove all elements | `my_set.clear()` |
| `union()` | Combine sets | `set1.union(set2)` |
| `intersection()` | Common elements | `set1.intersection(set2)` |
| `difference()` | Elements only in set1 | `set1.difference(set2)` |
| `issubset()` | Is set1 inside set2? | `set1.issubset(set2)` |
| `issuperset()` | Is set2 inside set1? | `set1.issuperset(set2)` |

### Most Important Operations

```python
# Create
my_set = {1, 2, 3}

# Add
my_set.add(4)

# Remove duplicates
unique = list(set([1, 2, 2, 3]))

# Membership test
if 2 in my_set:
    print("Found!")

# Union
combined = set1 | set2

# Intersection
common = set1 & set2

# Difference
diff = set1 - set2
```

---

## Key Takeaways

1. ✅ **Fast membership testing** — Use sets for `in` operations
2. ✅ **Remove duplicates** — Convert list to set then back
3. ✅ **Mathematical operations** — Union, intersection, difference
4. ✅ **Unordered** — No fixed index order
5. ⚠️ **Empty set syntax** — Use `set()`, not `{}`
6. ✅ **Data cleaning** — Perfect for real-world data science tasks

---

## Why Sets Matter in Data Science

- **Data Cleaning** — Remove duplicates efficiently
- **Unique Values** — Find distinct items quickly
- **Comparisons** — Compare datasets (common elements, differences)
- **Fast Lookups** — O(1) membership testing vs O(n) for lists
- **NLP Tasks** — Analyze text, word frequencies, unique terms

issubset()
issuperset()