#  Pandas — Day 03

## Data Selection & Filtering

---

## 1. Selecting a Single Column

Use `df["column_name"]` to select one column.

```python
import pandas as pd

data = {
    "Name": ["Amit", "Priya", "Rahul", "Neha"],
    "Age": [21, 19, 24, 22],
    "Marks": [85, 72, 45, 91]
}

df = pd.DataFrame(data)

print(df["Name"])
```

### Output

```text
0     Amit
1    Priya
2    Rahul
3     Neha
Name: Name, dtype: object
```

The result is a **Series**.

---

# 2. Selecting Multiple Columns

Use a list of column names.

```python
print(df[["Name", "Marks"]])
```

### Output

```text
    Name  Marks
0   Amit     85
1  Priya     72
2  Rahul     45
3   Neha     91
```

### Important

```python
df["Name"]                 # One column → Series

df[["Name", "Marks"]]      # Multiple columns → DataFrame
```

---

# 3. Selecting Rows with `iloc[]`

`iloc[]` selects data using **integer positions**.

```python
print(df.iloc[0])
```

Selects the first row.

```python
print(df.iloc[2])
```

Selects the third row.

### Example

```python
print(df.iloc[0:3])
```

Selects rows at positions:

```text
0
1
2
```

---

# 4. Selecting Rows with `loc[]`

`loc[]` is mainly used for **labels** and **conditions**.

```python
print(df.loc[0])
```

Selects the row whose index label is `0`.

Multiple rows:

```python
print(df.loc[0:2])
```

With the default integer index, `loc[0:2]` includes both `0` and `2`.

---

# 5. `loc[]` vs `iloc[]`

| Method   | Used For            |
| -------- | ------------------- |
| `loc[]`  | Labels / conditions |
| `iloc[]` | Integer positions   |

Example:

```python
df.loc[2]
```

Means:

> Give me the row with index label `2`.

```python
df.iloc[2]
```

Means:

> Give me the row at position `2`.

---

# 6. Selecting Specific Rows and Columns

Using `loc[]`:

```python
print(df.loc[0:2, ["Name", "Marks"]])
```

Format:

```python
df.loc[rows, columns]
```

Example:

```python
df.loc[0:2, "Name"]
```

Selects:

* Rows 0 to 2
* Only the `Name` column

---

# 7. Filtering Rows

Filtering means selecting rows based on a condition.

Example:

```python
print(df[df["Marks"] > 70])
```

This returns students whose marks are greater than 70.

### How it works

```python
df["Marks"] > 70
```

Creates a Boolean Series:

```text
0     True
1     True
2    False
3     True
```

Pandas keeps only the rows where the condition is `True`.

---

# 8. Filtering with `>`

```python
df[df["Marks"] > 70]
```

Greater than 70.

---

# 9. Filtering with `<`

```python
df[df["Marks"] < 70]
```

Less than 70.

---

# 10. Filtering with `>=`

```python
df[df["Age"] >= 21]
```

Age greater than or equal to 21.

---

# 11. Filtering with `<=`

```python
df[df["Age"] <= 21]
```

Age less than or equal to 21.

---

# 12. Filtering with `==`

Use `==` to check equality.

```python
df[df["City"] == "Delhi"]
```

Returns students from Delhi.

### Important

Do not use:

```python
df[df["City"] = "Delhi"]
```

Use:

```python
df[df["City"] == "Delhi"]
```

`=` means assignment.

`==` means comparison.

---

# 13. Filtering with `!=`

`!=` means "not equal to".

```python
df[df["City"] != "Delhi"]
```

Returns students who are not from Delhi.

---

# 14. Multiple Conditions — AND

Use `&` for **AND**.

Example:

```python
df[(df["Age"] >= 21) & (df["Marks"] > 70)]
```

Meaning:

> Age must be at least 21 AND marks must be greater than 70.

### Important

Put each condition inside parentheses:

```python
(df["Age"] >= 21) & (df["Marks"] > 70)
```

---

# 15. Multiple Conditions — OR

Use `|` for **OR**.

```python
df[(df["City"] == "Delhi") | (df["City"] == "Mumbai")]
```

Meaning:

> City is Delhi OR Mumbai.

---

# 16. AND vs OR

| Operator | Meaning |    |
| -------- | ------- | -- |
| `&`      | AND     |    |
| `        | `       | OR |
| `~`      | NOT     |    |

Example:

```python
df[(df["Age"] > 20) & (df["Marks"] > 70)]
```

Both conditions must be true.

```python
df[(df["City"] == "Delhi") | (df["City"] == "Pune")]
```

At least one condition must be true.

---

# 17. Using `isin()`

`isin()` checks whether values belong to a list.

```python
df[df["City"].isin(["Delhi", "Mumbai"])]
```

This is useful when checking multiple possible values.

Instead of:

```python
df[(df["City"] == "Delhi") | (df["City"] == "Mumbai")]
```

You can write:

```python
df[df["City"].isin(["Delhi", "Mumbai"])]
```

---

# 18. NOT with `~`

`~` means NOT.

Example:

```python
df[~df["City"].isin(["Delhi", "Mumbai"])]
```

Meaning:

> Give me students who are NOT from Delhi or Mumbai.

---

# 19. Filtering + Selecting Columns

We can filter rows and select only specific columns.

```python
result = df.loc[
    df["Marks"] > 70,
    ["Name", "Marks"]
]

print(result)
```

Meaning:

> Find students with marks greater than 70 and show only Name and Marks.

---

# 20. Updating Values Using `loc[]`

We can change values based on a condition.

Example:

```python
df.loc[df["Marks"] < 50, "Result"] = "Fail"
```

Students with marks below 50 get:

```text
Result = Fail
```

Another example:

```python
df.loc[df["Marks"] >= 50, "Result"] = "Pass"
```

---

# 21. Complete Example

```python
import pandas as pd

data = {
    "Name": ["Amit", "Priya", "Rahul", "Neha", "Karan"],
    "Age": [21, 19, 24, 22, 20],
    "Marks": [85, 72, 45, 91, 65],
    "City": ["Delhi", "Mumbai", "Delhi", "Pune", "Mumbai"]
}

df = pd.DataFrame(data)

# Single column
print(df["Name"])

# Multiple columns
print(df[["Name", "Marks"]])

# First 3 rows
print(df.iloc[0:3])

# Third row
print(df.iloc[2])

# Marks greater than 70
print(df[df["Marks"] > 70])

# Age >= 21
print(df[df["Age"] >= 21])

# Students from Delhi
print(df[df["City"] == "Delhi"])

# Delhi OR Mumbai
print(df[df["City"].isin(["Delhi", "Mumbai"])])

# Age >= 21 AND Marks > 70
print(df[(df["Age"] >= 21) & (df["Marks"] > 70)])

# Only Name and Marks where Marks > 70
print(df.loc[
    df["Marks"] > 70,
    ["Name", "Marks"]
])
```

---

# 22. Quick Revision

| Task             | Syntax                              |   |
| ---------------- | ----------------------------------- | - |
| Single column    | `df["Name"]`                        |   |
| Multiple columns | `df[["Name", "Age"]]`               |   |
| Row by position  | `df.iloc[2]`                        |   |
| Rows by label    | `df.loc[2]`                         |   |
| Row slicing      | `df.iloc[0:3]`                      |   |
| Filter `>`       | `df[df["Marks"] > 70]`              |   |
| Filter `<`       | `df[df["Marks"] < 70]`              |   |
| Filter `==`      | `df[df["City"] == "Delhi"]`         |   |
| Filter `!=`      | `df[df["City"] != "Delhi"]`         |   |
| AND              | `&`                                 |   |
| OR               | `                                   | ` |
| NOT              | `~`                                 |   |
| Multiple values  | `df["City"].isin([...])`            |   |
| Filter + columns | `df.loc[condition, columns]`        |   |
| Update values    | `df.loc[condition, column] = value` |   |

---

#  Day 03 Key Points

1. `df["column"]` → select one column.
2. `df[["col1", "col2"]]` → select multiple columns.
3. `iloc[]` → position-based selection.
4. `loc[]` → label/condition-based selection.
5. `df[condition]` → filter rows.
6. `&` → AND.
7. `|` → OR.
8. `~` → NOT.
9. `isin()` → check multiple values.
10. `loc[]` can be used to update values.

---



