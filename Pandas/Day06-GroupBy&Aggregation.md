# Pandas Day 06 — GroupBy & Aggregation

# 1. What is `groupby()`?

`groupby()` is used to **divide data into groups based on a column** and then perform calculations on each group.

### Syntax

```python
df.groupby("column")
```

### Example

```python
df.groupby("City")["Marks"].mean()
```

This means:

> Group students according to their city and find the average marks of each city.

---

# 2. Basic Aggregation Functions

Aggregation functions are used to calculate summary values.

| Function   | Meaning            |
| ---------- | ------------------ |
| `sum()`    | Total              |
| `mean()`   | Average            |
| `count()`  | Number of values   |
| `min()`    | Minimum value      |
| `max()`    | Maximum value      |
| `median()` | Middle value       |
| `std()`    | Standard deviation |

### Examples

```python
df["Marks"].sum()
```

```python
df["Marks"].mean()
```

```python
df["Marks"].max()
```

```python
df["Marks"].min()
```

---

# 3. GroupBy + Mean

```python
df.groupby("City")["Marks"].mean()
```

### Example

| City   | Marks |
| ------ | ----: |
| Mumbai |    80 |
| Mumbai |    90 |
| Delhi  |    70 |
| Delhi  |    80 |

Output:

```text
City
Delhi     75
Mumbai    85
```

---

# 4. GroupBy + Sum

```python
df.groupby("City")["Sales"].sum()
```

It calculates the **total sales for each city**.

---

# 5. GroupBy + Count

```python
df.groupby("City")["Name"].count()
```

It tells us the **number of records/students/customers in each city**.

---

# 6. GroupBy Multiple Columns

We can group data using more than one column.

### Syntax

```python
df.groupby(["City", "Gender"])["Marks"].mean()
```

This first groups by:

1. City
2. Gender

Then calculates the average marks.

---

# 7. Multiple Aggregations

We can apply multiple functions to the same column.

```python
df.groupby("City")["Marks"].agg(["mean", "max", "min"])
```

Output can look like:

| City   | mean | max | min |
| ------ | ---: | --: | --: |
| Delhi  |   75 |  80 |  70 |
| Mumbai |   85 |  90 |  80 |

---

# 8. `agg()` Function

`agg()` means **aggregation**.

It allows us to apply different functions to different columns.

### Example

```python
df.groupby("City").agg({
    "Marks": "mean",
    "Age": "max"
})
```

Meaning:

* Find average `Marks`
* Find maximum `Age`

---

# 9. Multiple Functions Using `agg()`

```python
df.groupby("City").agg({
    "Marks": ["mean", "max", "min"],
    "Age": ["mean", "max"]
})
```

This gives multiple summary statistics.

---

# 10. `value_counts()`

`value_counts()` counts how many times each unique value appears.

### Example

```python
df["City"].value_counts()
```

Output:

```text
Mumbai    10
Delhi      8
Surat      5
```

This tells us how many students belong to each city.

### Important Difference

```python
df["City"].value_counts()
```

Counts each unique value.

```python
df.groupby("City")["Marks"].mean()
```

Performs a calculation for each group.

---

# 11. GroupBy + Sorting

We can sort the result.

```python
df.groupby("City")["Marks"].mean().sort_values()
```

For descending order:

```python
df.groupby("City")["Marks"].mean().sort_values(ascending=False)
```

---

# 12. GroupBy + Multiple Operations

Example:

```python
df.groupby("Department")["Salary"].mean().sort_values(ascending=False)
```

This means:

> Group employees by department → calculate average salary → sort from highest to lowest.

---

# 13. GroupBy with `reset_index()`

After `groupby()`, the grouping column often becomes an index.

```python
result = df.groupby("City")["Marks"].mean()
```

To convert it back into a normal DataFrame:

```python
result = result.reset_index()
```

---

# 14. Real-World Example

Suppose we have:

| Name | City   | Marks | Gender |
| ---- | ------ | ----: | ------ |
| A    | Mumbai |    80 | F      |
| B    | Mumbai |    90 | M      |
| C    | Delhi  |    70 | F      |
| D    | Delhi  |    80 | M      |

### Average marks by city

```python
df.groupby("City")["Marks"].mean()
```

### Maximum marks by city

```python
df.groupby("City")["Marks"].max()
```

### Number of students by city

```python
df["City"].value_counts()
```

### Average marks by city and gender

```python
df.groupby(["City", "Gender"])["Marks"].mean()
```

---

# 15. GroupBy with Filtering

We can filter groups using conditions.

Example:

```python
result = df.groupby("City")["Marks"].mean()

result[result > 80]
```

This returns only cities where the average marks are greater than 80.

---

# 16. Common GroupBy Patterns

### Average

```python
df.groupby("City")["Marks"].mean()
```

### Total

```python
df.groupby("City")["Sales"].sum()
```

### Maximum

```python
df.groupby("City")["Marks"].max()
```

### Minimum

```python
df.groupby("City")["Marks"].min()
```

### Count

```python
df.groupby("City")["Name"].count()
```

### Multiple statistics

```python
df.groupby("City")["Marks"].agg(["mean", "max", "min"])
```

### Multiple groups

```python
df.groupby(["City", "Gender"])["Marks"].mean()
```

---

# 17. `groupby()` vs `value_counts()`

| `groupby()`                    | `value_counts()`           |
| ------------------------------ | -------------------------- |
| Used for grouping and analysis | Used mainly for counting   |
| Can perform many calculations  | Counts unique values       |
| More flexible                  | Simple and quick           |
| Can work with multiple columns | Usually used on one Series |

---

# 18. Important Parameters

### `as_index=False`

Instead of making the grouping column an index:

```python
df.groupby("City", as_index=False)["Marks"].mean()
```

The result keeps `City` as a normal column.

---

# 19. Important Things to Remember

### `groupby()`

Used to **divide data into groups**.

### Aggregation

Used to **calculate summary information**.

### `agg()`

Used to **apply multiple aggregation functions**.

### `value_counts()`

Used to **count unique values**.

### `reset_index()`

Used to **convert index back into a column**.

---

#  Quick Memory Trick

## GROUP → CALCULATE → SORT

```text
GROUPBY
   ↓
Aggregation
   ↓
SORT
```
#  Last-Minute Revision

| Concept                 | Syntax                       |
| ----------------------- | ---------------------------- |
| Group data              | `df.groupby("City")`         |
| Average                 | `.mean()`                    |
| Total                   | `.sum()`                     |
| Maximum                 | `.max()`                     |
| Minimum                 | `.min()`                     |
| Count                   | `.count()`                   |
| Multiple functions      | `.agg()`                     |
| Count unique values     | `.value_counts()`            |
| Sort                    | `.sort_values()`             |
| Convert index to column | `.reset_index()`             |
| Multiple groups         | `groupby(["City","Gender"])` |

---
