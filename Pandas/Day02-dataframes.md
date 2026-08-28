# Pandas — Day 02: DataFrame Basics & Data Inspection

## 1. What is a DataFrame?

A **DataFrame** is a 2-dimensional table in Pandas.

It contains:

* Rows
* Columns
* Index
* Data

```python
import pandas as pd

data = {
    "Name": ["Rahul", "Priya", "Aman", "Neha"],
    "Age": [21, 22, 20, 23],
    "City": ["Delhi", "Mumbai", "Delhi", "Pune"],
    "Salary": [30000, 40000, 25000, 50000]
}

df = pd.DataFrame(data)

print(df)
```

---

## 2. Creating a DataFrame

### From Dictionary

```python
data = {
    "Name": ["A", "B", "C"],
    "Age": [20, 21, 22]
}

df = pd.DataFrame(data)

print(df)
```

### From List of Lists

```python
data = [
    ["Rahul", 21],
    ["Priya", 22],
    ["Aman", 20]
]

df = pd.DataFrame(data, columns=["Name", "Age"])

print(df)
```

---

## 3. `shape`

Returns the number of **rows and columns**.

```python
print(df.shape)
```

Example:

```text
(3, 2)
```

Meaning:

```text
3 rows
2 columns
```

---

## 4. `columns`

Shows column names.

```python
print(df.columns)
```

---

## 5. `index`

Shows the row index.

```python
print(df.index)
```

By default:

```text
0, 1, 2, ...
```

---

## 6. `dtypes`

Shows the data type of each column.

```python
print(df.dtypes)
```

Common types:

```text
int64
float64
object
bool
```

---

## 7. `info()`

Gives general information about the DataFrame.

```python
df.info()
```

It shows:

* Number of rows
* Columns
* Non-null values
* Data types
* Memory usage

---

## 8. `head()`

Shows the first 5 rows by default.

```python
df.head()
```

You can specify the number of rows:

```python
df.head(2)
```

---

## 9. `tail()`

Shows the last 5 rows by default.

```python
df.tail()
```

You can specify the number:

```python
df.tail(2)
```

---

## 10. `describe()`

Provides basic statistical information for numerical columns.

```python
df.describe()
```

It gives:

* count
* mean
* std
* min
* 25%
* 50%
* 75%
* max

Example:

```python
print(df["Salary"].describe())
```

---

# 11. Selecting Columns

### Single column

```python
print(df["Name"])
```

This returns a **Series**.

### Multiple columns

```python
print(df[["Name", "Salary"]])
```

This returns a **DataFrame**.

Remember:

```python
df["Name"]                 # Series
df[["Name", "Salary"]]     # DataFrame
```

---

# 12. Selecting Rows with `iloc`

`iloc` selects data using **integer position**.

### First row

```python
print(df.iloc[0])
```

### Second row

```python
print(df.iloc[1])
```

### First two rows

```python
print(df.iloc[0:2])
```

### Specific row and column

```python
print(df.iloc[0, 1])
```

Meaning:

```text
row position = 0
column position = 1
```

---

# 13. Selecting Data with `loc`

`loc` selects using **labels**.

```python
print(df.loc[0])
```

Specific columns:

```python
print(df.loc[0:2, ["Name", "Salary"]])
```

### Difference

```text
iloc → position
loc  → label
```

---

# 14. Complete Practice Code

```python
import pandas as pd

data = {
    "Name": ["Rahul", "Priya", "Aman", "Neha"],
    "Age": [21, 22, 20, 23],
    "City": ["Delhi", "Mumbai", "Delhi", "Pune"],
    "Salary": [30000, 40000, 25000, 50000]
}

df = pd.DataFrame(data)

# Display DataFrame
print(df)

# Shape
print(df.shape)

# Columns
print(df.columns)

# Index
print(df.index)

# Data types
print(df.dtypes)

# Information
df.info()

# First rows
print(df.head())
print(df.head(2))

# Last rows
print(df.tail())
print(df.tail(2))

# Statistics
print(df.describe())

# Single column
print(df["Name"])

# Multiple columns
print(df[["Name", "Salary"]])

# Rows using iloc
print(df.iloc[0])
print(df.iloc[0:2])

# Rows and columns using loc
print(df.loc[0:2, ["Name", "Salary"]])
```

---

# 15. Practice Yourself

Create this DataFrame without looking at the solution:

```text
Name     Age    City       Salary
Rahul    21     Delhi      30000
Priya    22     Mumbai     40000
Aman     20     Delhi      25000
Neha     23     Pune       50000
```

# Quick Revision

| Method / Attribute    | Use                     |
| --------------------- | ----------------------- |
| `pd.DataFrame()`      | Create DataFrame        |
| `df.shape`            | Rows & columns          |
| `df.columns`          | Column names            |
| `df.index`            | Row index               |
| `df.dtypes`           | Data types              |
| `df.info()`           | DataFrame information   |
| `df.head()`           | First rows              |
| `df.tail()`           | Last rows               |
| `df.describe()`       | Statistics              |
| `df["Name"]`          | Select one column       |
| `df[["Name", "Age"]]` | Select multiple columns |
| `df.iloc[]`           | Select by position      |
| `df.loc[]`            | Select by label         |
