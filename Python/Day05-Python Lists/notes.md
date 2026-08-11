*# Day 5 – Python Lists

## 1. What is a List?

A list is used to store multiple values in one variable.

```python
numbers = [10, 20, 30, 40]
```

## 2. List can store different data types

```python
data = [10, "Python", 3.5, True]
```

## 3. Indexing

List indexing starts from `0`.

```python
numbers = [10, 20, 30, 40]

print(numbers[0])   # 10
print(numbers[2])   # 30
```

## 4. Negative Indexing

```python
numbers = [10, 20, 30, 40]

print(numbers[-1])  # 40
print(numbers[-2])  # 30
```

## 5. Changing a List Element

Lists are mutable, so we can change values.

```python
numbers = [10, 20, 30]

numbers[1] = 50

print(numbers)
```

Output:

```text
[10, 50, 30]
```

## 6. Adding Elements

### append()

Adds one element at the end.

```python
numbers = [10, 20, 30]

numbers.append(40)

print(numbers)
```

### insert()

Adds an element at a specific index.

```python
numbers.insert(1, 15)
```

## 7. Removing Elements

### remove()

Removes a specific value.

```python
numbers.remove(20)
```

### pop()

Removes an element using index.

```python
numbers.pop(1)
```

Without an index, it removes the last element.

```python
numbers.pop()
```

## 8. Length of List

```python
numbers = [10, 20, 30, 40]

print(len(numbers))
```

Output:

```text
4
```

## 9. Check Element

```python
numbers = [10, 20, 30]

print(20 in numbers)
print(50 in numbers)
```

Output:

```text
True
False
```

## 10. Loop Through List

```python
numbers = [10, 20, 30]

for num in numbers:
    print(num)
```

## 11. Sorting

```python
numbers = [40, 10, 30, 20]

numbers.sort()

print(numbers)
```

Output:

```text
[10, 20, 30, 40]
```

## Important Methods

| Method     | Use                      |
| ---------- | ------------------------ |
| `append()` | Add at end               |
| `insert()` | Add at specific position |
| `remove()` | Remove value             |
| `pop()`    | Remove using index       |
| `sort()`   | Sort list                |
| `len()`    | Find length              |

### Remember

**List → Ordered + Mutable + Allows duplicates**

```python
numbers = [10, 20, 20, 30]
```
**
