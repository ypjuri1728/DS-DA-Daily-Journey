# Day 08 — Pandas: Merging & Joining DataFrames

##  Today's Goal

Learn how to combine data from **multiple DataFrames**.

Topics:

* `concat()`
* `merge()`
* `join()`
* Inner Join
* Left Join
* Right Join
* Outer Join

---

## 1. Why Combine DataFrames?

In real-world datasets, data is often stored in different tables.

Example:

### Students

| student_id | name |
| ---------- | ---- |
| 1          | Aman |
| 2          | Riya |
| 3          | Raj  |

### Marks

| student_id | marks |
| ---------- | ----: |
| 1          |    85 |
| 2          |    90 |
| 4          |    75 |

We can combine these DataFrames using Pandas.

---

# 2. `concat()`

`concat()` is used to **combine DataFrames along rows or columns**.

```python
import pandas as pd

df1 = pd.DataFrame({
    "Name": ["Aman", "Riya"],
    "Marks": [80, 90]
})

df2 = pd.DataFrame({
    "Name": ["Raj", "Neha"],
    "Marks": [75, 85]
})

result = pd.concat([df1, df2])

print(result)
```

### Output

```text
   Name  Marks
0  Aman     80
1  Riya     90
0   Raj     75
1  Neha     85
```

### Reset index

```python
result = pd.concat([df1, df2], ignore_index=True)
```

Now index becomes:

```text
0
1
2
3
```

---

## 3. `concat()` Along Columns

```python
df1 = pd.DataFrame({
    "Name": ["Aman", "Riya"]
})

df2 = pd.DataFrame({
    "Marks": [80, 90]
})

result = pd.concat([df1, df2], axis=1)

print(result)
```

### Remember

```text
axis=0 → combine rows
axis=1 → combine columns
```

---

# 4. `merge()`

`merge()` is used to combine DataFrames using a **common column**.

Example:

```python
students = pd.DataFrame({
    "ID": [1, 2, 3],
    "Name": ["Aman", "Riya", "Raj"]
})

marks = pd.DataFrame({
    "ID": [1, 2, 4],
    "Marks": [80, 90, 75]
})

result = pd.merge(students, marks, on="ID")

print(result)
```

Output:

```text
   ID  Name  Marks
0   1  Aman     80
1   2  Riya     90
```

Only matching IDs are included because the default is **inner join**.

---

# 5. Types of Joins

There are four important joins:

```text
Inner
Left
Right
Outer
```

---

## 6. Inner Join

Returns **only matching rows** from both DataFrames.

```python
pd.merge(students, marks, on="ID", how="inner")
```

### Easy Trick

```text
INNER → common data
```

---

## 7. Left Join

Keeps **all rows from the left DataFrame**.

```python
pd.merge(students, marks, on="ID", how="left")
```

If a matching value is not found, Pandas gives `NaN`.

### Easy Trick

```text
LEFT → keep everything from left table
```

---

## 8. Right Join

Keeps **all rows from the right DataFrame**.

```python
pd.merge(students, marks, on="ID", how="right")
```

### Easy Trick

```text
RIGHT → keep everything from right table
```

---

## 9. Outer Join

Keeps **all rows from both DataFrames**.

```python
pd.merge(students, marks, on="ID", how="outer")
```

Missing values become `NaN`.

### Easy Trick

```text
OUTER → keep everything
```

---

# 10. Join Comparison

| Join  | What it keeps             |
| ----- | ------------------------- |
| Inner | Matching rows only        |
| Left  | All left + matching right |
| Right | All right + matching left |
| Outer | All rows from both        |

###  Easy Memory Trick

```text
INNER → Common
LEFT  → Left everything
RIGHT → Right everything
OUTER → Everything
```

---

# 11. `join()`

`join()` is another way to combine DataFrames, usually using their **index**.

```python
df1 = pd.DataFrame({
    "Name": ["Aman", "Riya", "Raj"]
}, index=[1, 2, 3])

df2 = pd.DataFrame({
    "Marks": [80, 90, 75]
}, index=[1, 2, 3])

result = df1.join(df2)

print(result)
```

Output:

```text
   Name  Marks
1  Aman     80
2  Riya     90
3   Raj     75
```

---

# 12. `merge()` vs `join()` vs `concat()`

| Function   | Main Use                    |
| ---------- | --------------------------- |
| `concat()` | Stack/combine DataFrames    |
| `merge()`  | Combine using common column |
| `join()`   | Combine mainly using index  |

### Quick Trick

```text
concat → Put together
merge  → Match a common column
join   → Match using index
```

---

# 13. Practical Example

```python
import pandas as pd

students = pd.DataFrame({
    "ID": [1, 2, 3, 4],
    "Name": ["Aman", "Riya", "Raj", "Neha"]
})

marks = pd.DataFrame({
    "ID": [1, 2, 3, 5],
    "Marks": [85, 90, 75, 80]
})

print("Students:")
print(students)

print("\nMarks:")
print(marks)

print("\nInner Join:")
print(pd.merge(students, marks, on="ID", how="inner"))

print("\nLeft Join:")
print(pd.merge(students, marks, on="ID", how="left"))

print("\nRight Join:")
print(pd.merge(students, marks, on="ID", how="right"))

print("\nOuter Join:")
print(pd.merge(students, marks, on="ID", how="outer"))
```
