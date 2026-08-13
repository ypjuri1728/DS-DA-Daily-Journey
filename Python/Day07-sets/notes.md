# Day 7 – Python Sets

## 1. What is a Set?

A Set is a collection used to store multiple values.

```python
numbers = {10, 20, 30, 40}
```

A Set is:

* Unordered
* Mutable
* Does not allow duplicates
* Can contain different data types

---

## 2. Duplicate Values

Duplicates are automatically removed.

```python
numbers = {10, 20, 20, 30, 30}

print(numbers)
```

Output:

```text
{10, 20, 30}
```

---

## 3. Creating an Empty Set

Use `set()`.

```python
numbers = set()
```

Don't use `{}` for an empty set because `{}` creates an empty dictionary.

---

## 4. Adding Elements

Use `add()`.

```python
numbers = {10, 20, 30}

numbers.add(40)

print(numbers)
```

---

## 5. Adding Multiple Elements

Use `update()`.

```python
numbers = {10, 20}

numbers.update([30, 40, 50])

print(numbers)
```

---

## 6. Removing Elements

### remove()

```python
numbers = {10, 20, 30}

numbers.remove(20)
```

If the value doesn't exist, `remove()` gives an error.

### discard()

```python
numbers.discard(50)
```

If the value doesn't exist, `discard()` does not give an error.

---

## 7. Check an Element

Use `in`.

```python
numbers = {10, 20, 30}

print(20 in numbers)
print(50 in numbers)
```

Output:

```text
True
False
```

---

## 8. Loop Through Set

```python
numbers = {10, 20, 30}

for num in numbers:
    print(num)
```

---

## 9. Union

Union combines elements from both sets.

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))
```

Result:

```text
{1, 2, 3, 4, 5}
```

---

## 10. Intersection

Intersection gives common elements.

```python
a = {1, 2, 3}
b = {2, 3, 4}

print(a.intersection(b))
```

Result:

```text
{2, 3}
```

---

## 11. Difference

Difference gives elements present in the first set but not in the second.

```python
a = {1, 2, 3}
b = {2, 3, 4}

print(a.difference(b))
```

Result:

```text
{1}
```

---

## 12. Set vs List vs Tuple

| List               | Tuple              | Set           |
| ------------------ | ------------------ | ------------- |
| `[]`               | `()`               | `{}`          |
| Ordered            | Ordered            | Unordered     |
| Mutable            | Immutable          | Mutable       |
| Allows duplicates  | Allows duplicates  | No duplicates |
| Indexing available | Indexing available | No indexing   |

### Remember

**List → Ordered + Mutable + Duplicates**

**Tuple → Ordered + Immutable + Duplicates**

**Set → Unordered + Mutable + No Duplicates**
