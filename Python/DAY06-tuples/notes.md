# Day 6 – Python Tuples

## 1. What is a Tuple?

A tuple is a collection used to store multiple values in one variable.

```python
numbers = (10, 20, 30, 40)
```

A tuple is:

* Ordered
* Immutable
* Allows duplicate values
* Allows different data types

---

## 2. Creating a Tuple

```python
numbers = (10, 20, 30)

names = ("A", "B", "C")

data = (10, "Python", 3.5, True)
```

---

## 3. Indexing

Index starts from `0`.

```python
numbers = (10, 20, 30, 40)

print(numbers[0])
print(numbers[2])
```

Output:

```text
10
30
```

---

## 4. Negative Indexing

```python
numbers = (10, 20, 30, 40)

print(numbers[-1])
print(numbers[-2])
```

Output:

```text
40
30
```

---

## 5. Tuple is Immutable

We cannot change an existing tuple element.

```python
numbers = (10, 20, 30)

# numbers[0] = 50  # Error
```

This is the main difference from a list.

---

## 6. Length

Use `len()` to find the number of elements.

```python
numbers = (10, 20, 30, 40)

print(len(numbers))
```

Output:

```text
4
```

---

## 7. Loop Through Tuple

```python
numbers = (10, 20, 30)

for num in numbers:
    print(num)
```

---

## 8. Check an Element

Use `in`.

```python
numbers = (10, 20, 30)

print(20 in numbers)
print(50 in numbers)
```

Output:

```text
True
False
```

---

## 9. Tuple Methods

### count()

Counts how many times a value occurs.

```python
numbers = (10, 20, 20, 30)

print(numbers.count(20))
```

Output:

```text
2
```

### index()

Returns the index of a value.

```python
numbers = (10, 20, 30)

print(numbers.index(20))
```

Output:

```text
1
```

---

## 10. Tuple vs List

| List              | Tuple                |
| ----------------- | -------------------- |
| `[]`              | `()`                 |
| Mutable           | Immutable            |
| Can change values | Cannot change values |
| More flexible     | More fixed           |

Example:

```python
my_list = [10, 20, 30]
my_tuple = (10, 20, 30)
```

### Remember

**List → Mutable**

**Tuple → Immutable**
