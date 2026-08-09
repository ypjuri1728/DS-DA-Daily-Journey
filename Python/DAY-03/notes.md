# Day 03 — Python Collections

## 1. What are Collections?

Collections are used to store **multiple values in a single variable**.

Python has four important built-in collections:

| Collection | Ordered | Changeable | Duplicates | Syntax         |
| ---------- | ------- | ---------- | ---------- | -------------- |
| List       | ✅       | ✅          | ✅          | `[]`           |
| Tuple      | ✅       | ❌          | ✅          | `()`           |
| Set        | ❌       | ✅          | ❌          | `{}`           |
| Dictionary | ✅       | ✅          | Keys ❌     | `{key: value}` |

---

# 2. List

A **list** stores multiple values in one variable.

Lists are:

* Ordered
* Changeable (mutable)
* Allow duplicate values
* Can contain different data types

```python
numbers = [10, 20, 30, 40]
```

### Accessing elements

Index starts from `0`.

```python
numbers = [10, 20, 30, 40]

print(numbers[0])   # 10
print(numbers[2])   # 30
print(numbers[-1])  # 40
```

### Updating elements

```python
numbers[1] = 25
print(numbers)
```

Output:

```text
[10, 25, 30, 40]
```

### List slicing

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])   # [20, 30, 40]
print(numbers[:3])    # [10, 20, 30]
print(numbers[2:])    # [30, 40, 50]
print(numbers[::-1])  # reverse
```

---

## Important List Methods

### append()

Adds one element at the end.

```python
numbers = [1, 2, 3]
numbers.append(4)

print(numbers)
```

```text
[1, 2, 3, 4]
```

### insert()

Adds an element at a specific index.

```python
numbers.insert(1, 10)
```

### extend()

Adds multiple elements.

```python
numbers.extend([5, 6, 7])
```

### remove()

Removes a specific value.

```python
numbers.remove(10)
```

### pop()

Removes an element using its index.

```python
numbers.pop(2)
```

If no index is given, it removes the last element.

```python
numbers.pop()
```

### sort()

Sorts the list.

```python
numbers.sort()
```

### reverse()

Reverses the list.

```python
numbers.reverse()
```

### count()

Counts how many times a value appears.

```python
numbers.count(2)
```

### index()

Returns the index of a value.

```python
numbers.index(3)
```

### len()

Returns the number of elements.

```python
len(numbers)
```

---

# 3. Tuple

A **tuple** is similar to a list, but it **cannot be changed after creation**.

Tuple is:

* Ordered
* Immutable
* Allows duplicates
* Can contain different data types

```python
student = ("Priyanshi", 21, "Python")
```

### Accessing tuple

```python
print(student[0])
print(student[-1])
```

### Tuple slicing

```python
numbers = (10, 20, 30, 40, 50)

print(numbers[1:4])
```

### Tuple methods

Only a few methods are commonly used.

```python
numbers.count(20)
numbers.index(30)
```

### Why use tuple?

Use a tuple when the data **should not be changed**.

Example:

```python
coordinates = (10, 20)
```

---

# 4. Set

A **set** stores unique values.

Set is:

* Unordered
* Changeable
* Does not allow duplicates
* Does not support indexing

```python
numbers = {10, 20, 30, 20, 10}

print(numbers)
```

Output will contain each value only once.

```text
{10, 20, 30}
```

### Adding elements

```python
numbers.add(40)
```

### Adding multiple elements

```python
numbers.update([50, 60, 70])
```

### Removing elements

```python
numbers.remove(20)
```

`remove()` gives an error if the value does not exist.

Safer option:

```python
numbers.discard(100)
```

`discard()` does not give an error if the value is missing.

---

## Set Operations

Suppose:

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
```

### Union

Combines all unique elements.

```python
print(A | B)
```

or

```python
print(A.union(B))
```

Result:

```text
{1, 2, 3, 4, 5, 6}
```

### Intersection

Returns common elements.

```python
print(A & B)
```

or

```python
print(A.intersection(B))
```

Result:

```text
{3, 4}
```

### Difference

Elements present in A but not B.

```python
print(A - B)
```

Result:

```text
{1, 2}
```

### Symmetric Difference

Elements that are not common.

```python
print(A ^ B)
```

Result:

```text
{1, 2, 5, 6}
```

---

# 5. Dictionary

A dictionary stores data in **key-value pairs**.

```python
student = {
    "name": "Priyanshi",
    "age": 21,
    "course": "Data Science"
}
```

Here:

```text
name   → key
Priyanshi → value
```

### Accessing values

```python
print(student["name"])
print(student["age"])
```

Safer method:

```python
print(student.get("name"))
```

### Adding a new key-value pair

```python
student["city"] = "Surat"
```

### Updating a value

```python
student["age"] = 22
```

### Removing an item

```python
student.pop("age")
```

### Getting all keys

```python
print(student.keys())
```

### Getting all values

```python
print(student.values())
```

### Getting key-value pairs

```python
print(student.items())
```

---

# 6. Dictionary Loop

We can loop through keys:

```python
student = {
    "name": "Priyanshi",
    "age": 21,
    "course": "Data Science"
}

for key in student:
    print(key)
```

Loop through values:

```python
for value in student.values():
    print(value)
```

Loop through both:

```python
for key, value in student.items():
    print(key, value)
```

---

# 7. Nested Collections

A collection can contain another collection.

### List inside list

```python
numbers = [
    [1, 2, 3],
    [4, 5, 6]
]

print(numbers[0][1])
```

Output:

```text
2
```

### List of dictionaries

Very useful in Data Science:

```python
students = [
    {"name": "Priyanshi", "marks": 90},
    {"name": "Rahul", "marks": 85}
]

print(students[0]["name"])
```

---

# 8. List vs Tuple vs Set vs Dictionary

### List

Use when:

* Order matters
* Data needs to change
* Duplicates are allowed

```python
[1, 2, 3]
```

### Tuple

Use when:

* Order matters
* Data should not change

```python
(1, 2, 3)
```

### Set

Use when:

* Only unique values are needed
* Duplicate removal is required
* Fast membership checking is useful

```python
{1, 2, 3}
```

### Dictionary

Use when:

* Data has a key-value relationship

```python
{"name": "Priyanshi", "age": 21}
```

---

# 9. Important Interview Questions

### Q1. Difference between List and Tuple?

**List:**

* Mutable
* Uses `[]`
* More suitable when data changes

**Tuple:**

* Immutable
* Uses `()`
* Suitable for fixed data

---

### Q2. Difference between List and Set?

**List:**

* Ordered
* Allows duplicates
* Supports indexing

**Set:**

* Unordered
* Does not allow duplicates
* Does not support indexing

---

### Q3. Why use a Dictionary?

A dictionary stores data as **key-value pairs**, making it easy to access values using meaningful keys.

---

### Q4. How to remove duplicates from a list?

```python
numbers = [1, 2, 2, 3, 3, 4]

unique = list(set(numbers))

print(unique)
```

---

### Q5. What is mutable and immutable?

**Mutable:** Can be changed after creation.

Examples:

```text
List
Set
Dictionary
```

**Immutable:** Cannot be changed after creation.

Examples:

```text
Tuple
String
Integer
Float
Boolean
```

---

# 10. Data Science Connection

Collections are very important in Data Science.

### List

Used to store data:

```python
marks = [85, 90, 78, 92]
```

### Dictionary

Used to represent structured records:

```python
student = {
    "name": "Priyanshi",
    "age": 21,
    "marks": 90
}
```

### Set

Useful for finding unique values:

```python
cities = {"Surat", "Delhi", "Surat", "Mumbai"}

print(cities)
```

Later, libraries such as **NumPy and Pandas** will use these concepts heavily.

---

# Quick Revision

```text
List       → [] → Ordered → Mutable → Duplicates allowed

Tuple      → () → Ordered → Immutable → Duplicates allowed

Set        → {} → Unordered → Mutable → No duplicates

Dictionary → {key:value} → Key-Value → Mutable → Keys unique
```

### Most Important Methods

```text
List:
append()
insert()
extend()
remove()
pop()
sort()
reverse()
count()
index()

Set:
add()
update()
remove()
discard()
union()
intersection()
difference()

Dictionary:
get()
keys()
values()
items()
update()
pop()
```
