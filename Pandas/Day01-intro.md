# Pandas — Day 01: Introduction & Basic Filtering

---

# 1. What is Pandas?

**Pandas** is a Python library used for:

* Data manipulation
* Data cleaning
* Data analysis
* Working with tabular data
* Reading and writing datasets

Pandas is one of the most important libraries for **Data Science and Data Analysis**.

### Easy Definition

> **Pandas = Python library for working with structured/tabular data.**

---

# 2. Why do we use Pandas?

Pandas makes it easy to work with large datasets.

| Task                | Pandas               |
| ------------------- | -------------------- |
| Load data           | `pd.read_csv()`      |
| View data           | `df.head()`          |
| Check rows/columns  | `df.shape`           |
| Check column names  | `df.columns`         |
| Check data types    | `df.dtypes`          |
| Statistical summary | `df.describe()`      |
| Select column       | `df["Name"]`         |
| Filter data         | `df[df["Age"] > 20]` |

---

# 3. Installation

### Terminal

```bash
pip install pandas
```

### Jupyter Notebook

```python
!pip install pandas
```

---

# 4. Import Pandas

```python
import pandas as pd
```

`pd` is the commonly used alias for Pandas.

After importing:

```python
pd.DataFrame()
pd.Series()
```

---

# 5. Pandas Data Structures

The two main Pandas data structures are:

1. **Series**
2. **DataFrame**

---

# 6. Series

A **Series** is a **1-dimensional labeled data structure**.

### Easy Trick

> **Series = Single Column**

### Example

```python
import pandas as pd

data = [10, 20, 30, 40]

s = pd.Series(data)

print(s)
```

Output:

```text
0    10
1    20
2    30
3    40
dtype: int64
```

Here:

* `0, 1, 2, 3` → Index
* `10, 20, 30, 40` → Values

---

## Custom Index

```python
marks = pd.Series(
    [85, 90, 78],
    index=["Math", "Python", "SQL"]
)

print(marks)
```

Access a value:

```python
print(marks["Python"])
```

Output:

```text
90
```

---

# 7. DataFrame

A **DataFrame** is a **2-dimensional labeled data structure**.

### Easy Trick

> **DataFrame = Complete Table**

A DataFrame contains:

* Rows
* Columns
* Index
* Values

### Example

```python
import pandas as pd

data = {
    "Name": ["Amit", "Priya", "Rahul"],
    "Age": [21, 22, 20],
    "Marks": [85, 90, 78]
}

df = pd.DataFrame(data)

print(df)
```

Output:

```text
    Name  Age  Marks
0   Amit   21     85
1  Priya   22     90
2  Rahul   20     78
```

---

# 8. Series vs DataFrame

| Feature    | Series            | DataFrame        |
| ---------- | ----------------- | ---------------- |
| Dimension  | 1D                | 2D               |
| Looks like | Single column     | Complete table   |
| Function   | `pd.Series()`     | `pd.DataFrame()` |
| Example    | One set of values | Rows + columns   |

###  Remember

```text
Series    → One Column
DataFrame → Complete Table
```

---

# 9. Create a DataFrame

We can create a DataFrame using a dictionary.

```python
data = {
    "Name": ["Amit", "Priya", "Rahul"],
    "Age": [21, 22, 20],
    "Marks": [85, 90, 78]
}

df = pd.DataFrame(data)

print(df)
```

---

# 10. Inspecting a DataFrame

After creating/loading a dataset, **first inspect it**.

---

## `head()`

Shows the first 5 rows by default.

```python
df.head()
```

First 2 rows:

```python
df.head(2)
```

---

## `tail()`

Shows the last 5 rows by default.

```python
df.tail()
```

Last 2 rows:

```python
df.tail(2)
```

---

## `shape`

Returns:

```text
(rows, columns)
```

Example:

```python
print(df.shape)
```

Output:

```text
(3, 3)
```

Meaning:

```text
3 rows
3 columns
```

### Important

`shape` is an **attribute**, not a function.

```python
df.shape      # do this
df.shape()    # no use this
```

---

## `columns`

Shows column names.

```python
print(df.columns)
```

---

## `index`

Shows row indexes.

```python
print(df.index)
```

---

## `dtypes`

Shows data types of each column.

```python
print(df.dtypes)
```

Example:

```text
Name     object
Age       int64
Marks     int64
```

---

## `info()`

Provides information about the DataFrame.

```python
df.info()
```

It shows:

* Number of rows
* Column names
* Non-null values
* Data types
* Memory usage

---

## `describe()`

Provides statistical information for numerical columns.

```python
df.describe()
```

It usually gives:

| Statistic | Meaning            |
| --------- | ------------------ |
| `count`   | Number of values   |
| `mean`    | Average            |
| `std`     | Standard deviation |
| `min`     | Minimum            |
| `25%`     | First quartile     |
| `50%`     | Median             |
| `75%`     | Third quartile     |
| `max`     | Maximum            |

---

# 11. Selecting Columns

Suppose:

```python
df = pd.DataFrame({
    "Name": ["Amit", "Priya", "Rahul"],
    "Age": [21, 22, 20],
    "Marks": [85, 90, 78]
})
```

## Select one column

```python
df["Name"]
```

This returns a **Series**.

---

## Select multiple columns

```python
df[["Name", "Marks"]]
```

This returns a **DataFrame**.

###  Important Trick

```python
df["Name"]       # Series
df[["Name"]]     # DataFrame
```

---

# 🔎 12. Basic Filtering

Filtering means:

> **Selecting rows based on a condition.**

This is one of the most important operations in Data Analysis.

---

## Filter using `>`

Students with marks greater than 80:

```python
df[df["Marks"] > 80]
```

---

## Filter using `<`

Students whose age is less than 22:

```python
df[df["Age"] < 22]
```

---

## Filter using `>=`

Students with marks greater than or equal to 80:

```python
df[df["Marks"] >= 80]
```

---

## Filter using `<=`

Students whose age is less than or equal to 21:

```python
df[df["Age"] <= 21]
```

---

## Filter using `==`

Students whose age is exactly 21:

```python
df[df["Age"] == 21]
```

---

## Filter using `!=`

Students whose age is not 21:

```python
df[df["Age"] != 21]
```

---

# 13. Multiple Conditions

We can combine conditions.

## AND → `&`

Both conditions must be true.

```python
df[(df["Age"] > 20) & (df["Marks"] > 80)]
```

Meaning:

> Age > 20 **AND** Marks > 80

---

## OR → `|`

At least one condition must be true.

```python
df[(df["Age"] > 20) | (df["Marks"] > 80)]
```

Meaning:

> Age > 20 **OR** Marks > 80

---

## NOT → `~`

Reverse the condition.

```python
df[~(df["Age"] > 20)]
```

---

###  Important Filtering Rule

Use parentheses around each condition.

```python
df[(df["Age"] > 20) & (df["Marks"] > 80)]
```

Not:

```python
df[df["Age"] > 20 & df["Marks"] > 80]  # no use
```

### Remember

```text
&  → AND
|  → OR
~  → NOT
```

---

# 14. DataFrame Basic Workflow

When you receive a new dataset, follow this order:

```text
Import Pandas
      ↓
Load Dataset
      ↓
View Data
      ↓
Understand Data
      ↓
Select Data
      ↓
Filter Data
```

Example:

```python
import pandas as pd

df = pd.read_csv("data.csv")

print(df.head())
print(df.shape)
print(df.columns)
print(df.dtypes)
df.info()
print(df.describe())

print(df["Age"])

print(df[df["Age"] > 20])
```

---

# 15. Complete Day 01 Example

```python
import pandas as pd

# Create DataFrame
data = {
    "Name": ["Amit", "Priya", "Rahul", "Neha", "Karan"],
    "Age": [21, 22, 20, 23, 21],
    "Marks": [85, 92, 67, 88, 76]
}

df = pd.DataFrame(data)

# Display DataFrame
print(df)

# First rows
print(df.head())

# Last rows
print(df.tail())

# Shape
print(df.shape)

# Columns
print(df.columns)

# Data types
print(df.dtypes)

# Information
df.info()

# Statistics
print(df.describe())

# Select one column
print(df["Name"])

# Select multiple columns
print(df[["Name", "Marks"]])

# Basic filtering
print(df[df["Marks"] > 80])

# Multiple conditions
print(df[(df["Age"] > 20) & (df["Marks"] > 80)])
```

---

# 🧠 16. Day 01 Cheat Sheet

| Operation        | Code                     |   |
| ---------------- | ------------------------ | - |
| Import           | `import pandas as pd`    |   |
| Series           | `pd.Series(data)`        |   |
| DataFrame        | `pd.DataFrame(data)`     |   |
| First rows       | `df.head()`              |   |
| Last rows        | `df.tail()`              |   |
| Shape            | `df.shape`               |   |
| Columns          | `df.columns`             |   |
| Index            | `df.index`               |   |
| Data types       | `df.dtypes`              |   |
| Information      | `df.info()`              |   |
| Statistics       | `df.describe()`          |   |
| One column       | `df["column"]`           |   |
| Multiple columns | `df[["col1", "col2"]]`   |   |
| Greater than     | `df[df["col"] > value]`  |   |
| Less than        | `df[df["col"] < value]`  |   |
| Equal            | `df[df["col"] == value]` |   |
| Not equal        | `df[df["col"] != value]` |   |
| AND              | `&`                      |   |
| OR               | `                        | ` |
| NOT              | `~`                      |   |

---

#  17. Important Tricks

### Trick 1 — Series vs DataFrame

```python
df["Name"]       # Series
df[["Name"]]     # DataFrame
```

---

### Trick 2 — Shape

```python
df.shape
```

Always remember:

```text
(rows, columns)
```

---

### Trick 3 — Data Inspection

```python
df.head()
df.shape
df.columns
df.dtypes
df.info()
df.describe()
```

These are the first things you should check when you get a new dataset.

---

### Trick 4 — Filtering

```python
df[df["Marks"] > 80]
```

Means:

> Give me rows where Marks are greater than 80.

---

### Trick 5 — Multiple Filtering

```python
df[(df["Age"] > 20) & (df["Marks"] > 80)]
```

```text
& → AND
| → OR
~ → NOT
```
