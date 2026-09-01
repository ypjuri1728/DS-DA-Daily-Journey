#  Pandas Day 05 — Data Cleaning

## 1. What is Data Cleaning?

Data cleaning means **finding and fixing incorrect, missing, duplicate, or inconsistent data**.

### Common problems:

* Missing values
* Duplicate rows
* Wrong data types
* Extra spaces
* Inconsistent values
* Incorrect formatting

---

# 2. Missing Values

Missing values are usually represented by `NaN`.

```python
import pandas as pd

df = pd.DataFrame({
    "Name": ["A", "B", "C", "D"],
    "Age": [20, None, 22, None],
    "Marks": [80, 90, None, 75]
})

print(df)
```

---

## 3. `isnull()`

Checks whether values are missing.

```python
print(df.isnull())
```

Returns:

```text
True  → value is missing
False → value exists
```

### Count missing values

```python
print(df.isnull().sum())
```

### Trick

```text
isnull() → Find missing values
```

---

# 4. `notnull()`

Checks whether values are **not missing**.

```python
print(df.notnull())
```

### Trick

```text
isnull()    → missing
notnull()   → available
```

---

# 5. `dropna()`

Removes rows containing missing values.

```python
df = df.dropna()

print(df)
```

### Remove rows with missing values from a specific column

```python
df = df.dropna(subset=["Age"])
```

### Important

```text
dropna() → Delete missing data
```

---

# 6. `fillna()`

Instead of deleting missing values, we can replace them.

```python
df["Age"] = df["Age"].fillna(0)
```

Example:

```python
df["Age"] = df["Age"].fillna(21)
```

### Fill with mean

```python
df["Age"] = df["Age"].fillna(df["Age"].mean())
```

### Fill with median

```python
df["Age"] = df["Age"].fillna(df["Age"].median())
```

### Fill with mode

```python
df["Name"] = df["Name"].fillna(df["Name"].mode()[0])
```

### Trick

```text
dropna() → Remove
fillna() → Replace
```

---

# 7. Duplicate Data

Sometimes the same row appears more than once.

```python
print(df.duplicated())
```

Returns:

```text
True  → duplicate row
False → unique row
```

### Count duplicates

```python
print(df.duplicated().sum())
```

---

# 8. `drop_duplicates()`

Removes duplicate rows.

```python
df = df.drop_duplicates()
```

### Remove duplicates based on one column

```python
df = df.drop_duplicates(subset=["Name"])
```

### Trick

```text
duplicated()      → Find duplicates
drop_duplicates() → Remove duplicates
```

---

# 9. `replace()`

Used to replace existing values.

```python
df["Gender"] = df["Gender"].replace("M", "Male")
```

Multiple values:

```python
df["Gender"] = df["Gender"].replace({
    "M": "Male",
    "F": "Female"
})
```

### Example

```python
df["City"] = df["City"].replace("Baroda", "Vadodara")
```

---

# 10. Changing Data Types

Use `astype()` to change the datatype.

```python
df["Age"] = df["Age"].astype(int)
```

Example:

```python
df["Marks"] = df["Marks"].astype(float)
```

Check datatype:

```python
print(df.dtypes)
```

### Common types

```text
int
float
str
bool
```

### Trick

```text
astype() → Change datatype
```

---

# 11. String Cleaning

Pandas provides `.str` for string operations.

Example:

```python
df["Name"] = df["Name"].str.lower()
```

---

## 12. `.str.lower()`

Converts text to lowercase.

```python
df["Name"] = df["Name"].str.lower()
```

```text
PRIYANSHI → priyanshi
```

---

# 13. `.str.upper()`

Converts text to uppercase.

```python
df["Name"] = df["Name"].str.upper()
```

```text
priyanshi → PRIYANSHI
```

---

# 14. `.str.strip()`

Removes extra spaces from the beginning and end.

```python
df["Name"] = df["Name"].str.strip()
```

Example:

```text
"  Priyanshi  " → "Priyanshi"
```

### Trick

```text
strip() → Remove extra spaces
```

---

# 15. `.str.replace()`

Replaces text inside strings.

```python
df["City"] = df["City"].str.replace("Baroda", "Vadodara")
```

Example:

```text
"Data Science" → "Data-Science"
```

```python
df["Course"] = df["Course"].str.replace(" ", "-")
```

---

# 16. Combining String Cleaning

You can use multiple operations together.

```python
df["Name"] = df["Name"].str.strip().str.lower()
```

Example:

```text
"  PRIYANSHI  "
        ↓
strip()
        ↓
"PRIYANSHI"
        ↓
lower()
        ↓
"priyanshi"
```

---

# 17. Checking Data After Cleaning

Useful functions:

```python
print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())
print(df.duplicated().sum())
print(df.dtypes)
```

---

# 18. Basic Data Cleaning Workflow

Remember this order:

```text
1. Load data
       ↓
2. Understand data
       ↓
3. Find missing values
       ↓
4. Handle missing values
       ↓
5. Find duplicates
       ↓
6. Remove duplicates
       ↓
7. Fix incorrect values
       ↓
8. Fix datatypes
       ↓
9. Clean strings
       ↓
10. Check final data
```

---

# 19. Complete Example

```python
import pandas as pd

df = pd.DataFrame({
    "Name": [" Priyanshi ", "Rahul", "Priyanshi ", "Amit"],
    "Age": [21, None, 21, 22],
    "City": [" Surat", "Baroda", " Surat", "Ahmedabad"]
})

print("Original Data:")
print(df)

# Remove extra spaces
df["Name"] = df["Name"].str.strip()
df["City"] = df["City"].str.strip()

# Fill missing Age
df["Age"] = df["Age"].fillna(df["Age"].mean())

# Remove duplicates
df = df.drop_duplicates()

# Convert Age to integer
df["Age"] = df["Age"].astype(int)

# Convert names to lowercase
df["Name"] = df["Name"].str.lower()

# Replace city name
df["City"] = df["City"].replace("Baroda", "Vadodara")

print("\nClean Data:")
print(df)
```

---

# 20. Quick Revision Table

| Function            | Purpose                 |
| ------------------- | ----------------------- |
| `isnull()`          | Find missing values     |
| `notnull()`         | Find available values   |
| `dropna()`          | Remove missing values   |
| `fillna()`          | Fill missing values     |
| `duplicated()`      | Find duplicate rows     |
| `drop_duplicates()` | Remove duplicates       |
| `replace()`         | Replace values          |
| `astype()`          | Change datatype         |
| `.str.lower()`      | Lowercase               |
| `.str.upper()`      | Uppercase               |
| `.str.strip()`      | Remove extra spaces     |
| `.str.replace()`    | Replace text            |
| `dtypes`            | Check datatypes         |
| `info()`            | Get dataset information |

---

#  Easy Tricks to Remember

```text
MISSING
isnull()  → Find
dropna()  → Delete
fillna()  → Fill

DUPLICATE
duplicated()       → Find
drop_duplicates()  → Delete

VALUE
replace() → Replace

TYPE
astype() → Change datatype

STRING
lower()   → small letters
upper()   → CAPITAL letters
strip()   → remove spaces
replace() → change text
```



---

## Summary

```text
Data Cleaning
│
├── Missing Values
│   ├── isnull()
│   ├── notnull()
│   ├── dropna()
│   └── fillna()
│
├── Duplicates
│   ├── duplicated()
│   └── drop_duplicates()
│
├── Values
│   └── replace()
│
├── Data Types
│   └── astype()
│
└── Strings
    ├── lower()
    ├── upper()
    ├── strip()
    └── replace()
```
