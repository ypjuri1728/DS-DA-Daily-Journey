# Day 07 — Sorting & Value Counts

# 1. sort_values()

`sort_values()` is used to sort rows according to the values of a column.

### Syntax

```python
df.sort_values("column_name")
```

### Example

```python
import pandas as pd

data = {
    "Name": ["Aman", "Riya", "Priya", "Rahul"],
    "Marks": [75, 90, 65, 85]
}

df = pd.DataFrame(data)

print(df.sort_values("Marks"))
```

### Output

```text
    Name  Marks
2  Priya     65
0   Aman     75
3  Rahul     85
1   Riya     90
```

By default, sorting is in **ascending order**.

---

# 2. Descending Order

Use:

```python
ascending=False
```

### Example

```python
print(df.sort_values("Marks", ascending=False))
```

### Output

```text
    Name  Marks
1   Riya     90
3  Rahul     85
0   Aman     75
2  Priya     65
```

---

# 3. Sorting by Multiple Columns

We can sort using more than one column.

### Example

```python
data = {
    "Name": ["Aman", "Riya", "Priya", "Rahul"],
    "City": ["Mumbai", "Delhi", "Mumbai", "Delhi"],
    "Marks": [75, 90, 65, 85]
}

df = pd.DataFrame(data)

print(df.sort_values(["City", "Marks"]))
```

Pandas first sorts by `City`, and then sorts `Marks` inside each city.

---

# 4. Different Sorting Orders for Multiple Columns

We can give different ascending/descending orders.

```python
print(df.sort_values(
    ["City", "Marks"],
    ascending=[True, False]
))
```

Here:

* `City` → ascending
* `Marks` → descending

---

# 5. sort_index()

`sort_index()` sorts the DataFrame according to its index.

### Example

```python
data = {
    "Name": ["Aman", "Riya", "Priya"],
    "Marks": [75, 90, 65]
}

df = pd.DataFrame(data, index=[3, 1, 2])

print(df)
```

Sort by index:

```python
print(df.sort_index())
```

---

# 6. value_counts()

`value_counts()` tells us **how many times each value occurs** in a column.

### Example

```python
data = {
    "Name": ["Aman", "Riya", "Priya", "Rahul", "Neha"],
    "City": ["Mumbai", "Delhi", "Mumbai", "Delhi", "Mumbai"]
}

df = pd.DataFrame(data)

print(df["City"].value_counts())
```

### Output

```text
Mumbai    3
Delhi     2
```

So:

* Mumbai → 3 students
* Delhi → 2 students

---

# 7. value_counts() with Sorting

`value_counts()` already returns values in decreasing frequency order by default.

```python
print(df["City"].value_counts())
```

We can also use:

```python
print(df["City"].value_counts().sort_values())
```

This sorts the counts in ascending order.

---

# 8. rank()

`rank()` gives a rank to each value.

### Example

```python
data = {
    "Name": ["Aman", "Riya", "Priya", "Rahul"],
    "Marks": [75, 90, 65, 85]
}

df = pd.DataFrame(data)

df["Rank"] = df["Marks"].rank(ascending=False)

print(df)
```

### Output

```text
    Name  Marks  Rank
0   Aman     75   3.0
1   Riya     90   1.0
2  Priya     65   4.0
3  Rahul     85   2.0
```

Higher marks get a better rank because we used:

```python
ascending=False
```

---

# 9. Sorting + Filtering

We can combine filtering and sorting.

### Example

Find students who scored more than 70 and sort them from highest to lowest.

```python
result = df[df["Marks"] > 70]

result = result.sort_values("Marks", ascending=False)

print(result)
```

---

# 10. Complete Example

```python
import pandas as pd

data = {
    "Name": ["Aman", "Riya", "Priya", "Rahul", "Neha", "Karan"],
    "City": ["Mumbai", "Delhi", "Mumbai", "Delhi", "Mumbai", "Delhi"],
    "Marks": [75, 90, 65, 85, 92, 70]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

print("\nSorted by Marks:")
print(df.sort_values("Marks"))

print("\nSorted by Marks Descending:")
print(df.sort_values("Marks", ascending=False))

print("\nCity Counts:")
print(df["City"].value_counts())

df["Rank"] = df["Marks"].rank(ascending=False)

print("\nDataFrame with Rank:")
print(df)

print("\nStudents with Marks > 70:")
result = df[df["Marks"] > 70]
print(result)

print("\nFiltered and Sorted:")
result = result.sort_values("Marks", ascending=False)
print(result)
```

---

# 11. Important Difference

| Function         | Purpose                       |
| ---------------- | ----------------------------- |
| `sort_values()`  | Sort using column values      |
| `sort_index()`   | Sort using index              |
| `value_counts()` | Count frequency of each value |
| `rank()`         | Give ranking to values        |

---

#  Quick Revision

### `sort_values()`

**"Sort rows based on column values."**

```python
df.sort_values("Marks")
```

### `sort_index()`

**"Sort rows based on index."**

```python
df.sort_index()
```

### `value_counts()`

**"Count how many times each value appears."**

```python
df["City"].value_counts()
```

### `rank()`

**"Give rank to values."**

```python
df["Marks"].rank(ascending=False)
```

