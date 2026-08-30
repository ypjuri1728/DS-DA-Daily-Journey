# Pandas — Day 04

## Data Manipulation

Today we learn how to **modify, sort, add, remove, rename, and calculate data in a DataFrame**.

---

# 1. Sorting Data

Sorting means arranging rows according to a column.

## `sort_values()`

```python
df.sort_values("Marks")
```

By default, sorting is **ascending**.

Example:

```python
import pandas as pd

data = {
    "Name": ["Amit", "Priya", "Rahul", "Neha"],
    "Age": [21, 19, 24, 22],
    "Marks": [85, 72, 45, 91]
}

df = pd.DataFrame(data)

print(df.sort_values("Marks"))
```

Output:

```text
    Name  Age  Marks
2  Rahul   24     45
1  Priya   19     72
0   Amit   21     85
3   Neha   22     91
```

---

## Descending Order

Use:

```python
ascending=False
```

Example:

```python
df.sort_values("Marks", ascending=False)
```

Output:

```text
    Name  Age  Marks
3   Neha   22     91
0   Amit   21     85
1  Priya   19     72
2  Rahul   24     45
```

###  Trick

```text
ascending=True   → Small → Large
ascending=False  → Large → Small
```

---

# 2. Sorting by Multiple Columns

We can sort using more than one column.

```python
df.sort_values(["City", "Marks"])
```

Pandas first sorts by `City`.

If two rows have the same city, it sorts those rows by `Marks`.

Example:

```python
df.sort_values(
    ["City", "Marks"],
    ascending=[True, False]
)
```

Here:

```text
City  → Ascending
Marks → Descending
```

---

# 3. Adding a New Column

We can create a new column by assigning values.

```python
df["Passed"] = True
```

This creates:

```text
   Name   Marks  Passed
0  Amit      85    True
1  Priya     72    True
2  Rahul     45    True
3  Neha      91    True
```

---

# 4. Creating a Column from Existing Data

We can use an existing column to create a new column.

```python
df["Bonus"] = df["Marks"] + 5
```

Example:

```text
Marks → Bonus

85    → 90
72    → 77
45    → 50
91    → 96
```

###  Important

Pandas performs the operation on the **whole column**.

```python
df["Marks"] + 5
```

means:

```text
Every Marks value + 5
```

---

# 5. Creating a Boolean Column

```python
df["Passed"] = df["Marks"] >= 50
```

Example:

```text
Marks    Passed
85       True
72       True
45       False
91       True
```

This is very useful for filtering and data analysis.

---

# 6. Column Calculations

We can perform mathematical operations between columns.

Example:

```python
data = {
    "Name": ["Amit", "Priya", "Rahul"],
    "Maths": [80, 70, 50],
    "Science": [90, 75, 45]
}

df = pd.DataFrame(data)
```

Create total:

```python
df["Total"] = df["Maths"] + df["Science"]
```

Create average:

```python
df["Average"] = df["Total"] / 2
```

Result:

```text
    Name  Maths  Science  Total  Average
0   Amit     80       90    170     85.0
1  Priya     70       75    145     72.5
2  Rahul     50       45     95     47.5
```

---

# 7. Updating a Column

We can modify an existing column.

```python
df["Marks"] = df["Marks"] + 5
```

This adds 5 marks to every student.

---

# 8. Updating Values Using `loc[]`

We can update values based on a condition.

```python
df.loc[df["Marks"] < 50, "Result"] = "Fail"
```

Meaning:

> Find rows where Marks < 50 and set Result to `"Fail"`.

Example:

```python
df.loc[df["Marks"] >= 50, "Result"] = "Pass"
```

---

# 9. Removing Columns

Use:

```python
df.drop()
```

To remove a column:

```python
df.drop("Age", axis=1)
```

### Important

This returns a new DataFrame. The original DataFrame is not changed unless we use `inplace=True`.

---

# 10. `inplace=True`

```python
df.drop("Age", axis=1, inplace=True)
```

Now the original DataFrame is modified.

### Without `inplace`

```python
df.drop("Age", axis=1)
```

Original DataFrame remains unchanged.

### With `inplace`

```python
df.drop("Age", axis=1, inplace=True)
```

Original DataFrame is changed.

---

# 11. Removing Multiple Columns

```python
df.drop(
    ["Age", "City"],
    axis=1,
    inplace=True
)
```

This removes both `Age` and `City`.

---

# 12. Removing Rows

`axis=0` is used for rows.

```python
df.drop(2, axis=0)
```

Removes the row with index `2`.

Multiple rows:

```python
df.drop([1, 3], axis=0)
```

---

# 13. Understanding `axis`

This is very important.

```text
axis=0 → Rows
axis=1 → Columns
```

### Easy trick

Think:

```text
axis=0
↓
Remove/operate DOWN the rows

axis=1
↓
Remove/operate ACROSS columns
```

For dropping:

```python
df.drop(2, axis=0)
```

→ Remove row 2.

```python
df.drop("Age", axis=1)
```

→ Remove Age column.

---

# 14. Renaming Columns

Use:

```python
df.rename()
```

Example:

```python
df.rename(
    columns={"Marks": "Score"}
)
```

Now:

```text
Marks → Score
```

---

## Rename Multiple Columns

```python
df.rename(
    columns={
        "Name": "Student_Name",
        "Marks": "Score"
    }
)
```

---

## Rename Permanently

Without `inplace`:

```python
df.rename(
    columns={"Marks": "Score"}
)
```

The original DataFrame doesn't change.

With `inplace=True`:

```python
df.rename(
    columns={"Marks": "Score"},
    inplace=True
)
```

The original DataFrame changes.

---

# 15. Reordering Columns

We can change the order of columns.

Suppose:

```text
Name | Age | Marks | City
```

We want:

```text
Name | Marks | City | Age
```

Use:

```python
df = df[["Name", "Marks", "City", "Age"]]
```

---

# 16. Complete Example

```python
import pandas as pd

data = {
    "Name": ["Amit", "Priya", "Rahul", "Neha", "Karan"],
    "Age": [21, 19, 24, 22, 20],
    "Marks": [85, 72, 45, 91, 65],
    "City": ["Delhi", "Mumbai", "Delhi", "Pune", "Mumbai"]
}

df = pd.DataFrame(data)

# Sort by Marks
print(df.sort_values("Marks"))

# Sort highest to lowest
print(df.sort_values("Marks", ascending=False))

# Add a new column
df["Bonus"] = df["Marks"] + 5

# Add Pass/Fail column
df["Passed"] = df["Marks"] >= 50

# Create Result column
df.loc[df["Marks"] >= 50, "Result"] = "Pass"
df.loc[df["Marks"] < 50, "Result"] = "Fail"

# Rename column
df.rename(columns={"Marks": "Score"}, inplace=True)

print(df)
```

---

# 17. Day 04 Important Functions

| Function          | Purpose                   |
| ----------------- | ------------------------- |
| `sort_values()`   | Sort data                 |
| `df["new"] = ...` | Add column                |
| `df["col"] = ...` | Update column             |
| `loc[]`           | Conditional update        |
| `drop()`          | Remove rows/columns       |
| `rename()`        | Rename rows/columns       |
| `inplace=True`    | Modify original DataFrame |
| `axis=0`          | Rows                      |
| `axis=1`          | Columns                   |

---

#  Quick Revision

### Sort

```python
df.sort_values("Marks")
```

### Sort descending

```python
df.sort_values("Marks", ascending=False)
```

### Add column

```python
df["Bonus"] = df["Marks"] + 5
```

### Boolean column

```python
df["Passed"] = df["Marks"] >= 50
```

### Update conditionally

```python
df.loc[df["Marks"] < 50, "Result"] = "Fail"
```

### Remove column

```python
df.drop("Age", axis=1)
```

### Remove permanently

```python
df.drop("Age", axis=1, inplace=True)
```

### Remove row

```python
df.drop(2, axis=0)
```

### Rename

```python
df.rename(columns={"Marks": "Score"})
```

### Rename permanently

```python
df.rename(
    columns={"Marks": "Score"},
    inplace=True
)
```

---

#  Super Memory Trick

```text
SORT
↓
sort_values()

ADD
↓
df["New"] = ...

UPDATE
↓
df["Column"] = ...

CONDITION + UPDATE
↓
df.loc[...]

REMOVE
↓
drop()

RENAME
↓
rename()

axis
↓
0 = rows
1 = columns
```



