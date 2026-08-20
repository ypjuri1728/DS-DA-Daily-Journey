*# Day 03 — SQL Functions + ORDER BY

## 1. SQL Functions

SQL functions are built-in operations used to perform calculations, modify data, or get useful information from rows.

There are two main types:

* **Aggregate Functions** → work on multiple rows and return one result.
* **Scalar/String/Date Functions** → work on individual values/rows.

---

## 2. Aggregate Functions

Aggregate functions are commonly used with `GROUP BY`.

### COUNT()

Counts the number of rows.

```sql
SELECT COUNT(*) 
FROM student;
```

Count a specific column:

```sql
SELECT COUNT(name)
FROM student;
```

> `COUNT(*)` counts all rows, while `COUNT(column)` ignores `NULL` values.

---

### SUM()

Returns the total of a numeric column.

```sql
SELECT SUM(salary)
FROM employee;
```

---

### AVG()

Returns the average value.

```sql
SELECT AVG(salary)
FROM employee;
```

---

### MAX()

Returns the highest value.

```sql
SELECT MAX(salary)
FROM employee;
```

---

### MIN()

Returns the lowest value.

```sql
SELECT MIN(salary)
FROM employee;
```

---

## 3. Using Multiple Aggregate Functions

```sql
SELECT 
    COUNT(*) AS total_employees,
    SUM(salary) AS total_salary,
    AVG(salary) AS average_salary,
    MAX(salary) AS highest_salary,
    MIN(salary) AS lowest_salary
FROM employee;
```

`AS` is used to give a temporary name (alias) to the result.

---

# 4. String Functions

String functions are used to work with text.

### UPPER()

Converts text to uppercase.

```sql
SELECT UPPER(name)
FROM student;
```

Example:

```text
Priyanshi → PRIYANSHI
```

---

### LOWER()

Converts text to lowercase.

```sql
SELECT LOWER(name)
FROM student;
```

---

### LENGTH()

Returns the number of characters.

```sql
SELECT name, LENGTH(name)
FROM student;
```

---

### CONCAT()

Combines multiple strings.

```sql
SELECT CONCAT(first_name, ' ', last_name) AS full_name
FROM student;
```

---

# 5. Numeric Functions

### ROUND()

Rounds a decimal value.

```sql
SELECT ROUND(AVG(salary), 2)
FROM employee;
```

Example:

```text
24567.678 → 24567.68
```

---

### CEIL()

Rounds a number upward.

```sql
SELECT CEIL(10.2);
```

Output:

```text
11
```

---

### FLOOR()

Rounds a number downward.

```sql
SELECT FLOOR(10.8);
```

Output:

```text
10
```

---

# 6. ORDER BY

`ORDER BY` is used to **sort the result**.

### Ascending Order

```sql
SELECT *
FROM student
ORDER BY marks ASC;
```

`ASC` means smallest → largest.

`ASC` is the default, so this also works:

```sql
SELECT *
FROM student
ORDER BY marks;
```

---

### Descending Order

```sql
SELECT *
FROM student
ORDER BY marks DESC;
```

`DESC` means largest → smallest.

---

# 7. ORDER BY with Multiple Columns

We can sort using more than one column.

```sql
SELECT *
FROM student
ORDER BY marks DESC, name ASC;
```

SQL first sorts by `marks`.

If two students have the same marks, it sorts those students by `name`.

---

# 8. ORDER BY with SELECT

```sql
SELECT name, salary
FROM employee
ORDER BY salary DESC;
```

This displays employees from **highest salary to lowest salary**.

---

# 9. ORDER BY with WHERE

`WHERE` filters the rows first, then `ORDER BY` sorts the filtered result.

```sql
SELECT name, salary
FROM employee
WHERE salary > 30000
ORDER BY salary DESC;
```

Meaning:

1. Select employees.
2. Keep only employees with salary greater than `30000`.
3. Sort them by salary from highest to lowest.

---

# 10. ORDER BY with Aggregate Functions

We can sort using an aggregate result.

```sql
SELECT department, AVG(salary) AS avg_salary
FROM employee
GROUP BY department
ORDER BY avg_salary DESC;
```

This shows departments from **highest average salary to lowest average salary**.

We can also write:

```sql
ORDER BY AVG(salary) DESC;
```

---

# 11. DISTINCT

`DISTINCT` removes duplicate values.

```sql
SELECT DISTINCT department
FROM employee;
```

Example:

```text
IT
HR
IT
Sales
HR
```

Result:

```text
IT
HR
Sales
```

---

# 12. DISTINCT + ORDER BY

```sql
SELECT DISTINCT department
FROM employee
ORDER BY department ASC;
```

This gives unique departments in alphabetical order.

---

# 13. LIMIT

`LIMIT` restricts the number of rows returned.

```sql
SELECT *
FROM employee
LIMIT 5;
```

Returns only the first 5 rows.

### Top 3 Salaries

```sql
SELECT name, salary
FROM employee
ORDER BY salary DESC
LIMIT 3;
```

This is an important pattern for finding the **top N values**.

---

# 14. Important SQL Query Order

Remember the logical order:

```text
FROM
↓
WHERE
↓
GROUP BY
↓
HAVING
↓
SELECT
↓
ORDER BY
↓
LIMIT
```

Example:

```sql
SELECT department, AVG(salary) AS avg_salary
FROM employee
WHERE salary > 20000
GROUP BY department
HAVING AVG(salary) > 30000
ORDER BY avg_salary DESC
LIMIT 3;
```

---

# 15. Important Practice Queries

### Find highest salary

```sql
SELECT MAX(salary)
FROM employee;
```

### Find lowest salary

```sql
SELECT MIN(salary)
FROM employee;
```

### Find average salary

```sql
SELECT AVG(salary)
FROM employee;
```

### Count employees

```sql
SELECT COUNT(*)
FROM employee;
```

### Total salary

```sql
SELECT SUM(salary)
FROM employee;
```

### Employees with highest salary first

```sql
SELECT name, salary
FROM employee
ORDER BY salary DESC;
```

### Employees with lowest salary first

```sql
SELECT name, salary
FROM employee
ORDER BY salary ASC;
```

### Top 5 highest-paid employees

```sql
SELECT name, salary
FROM employee
ORDER BY salary DESC
LIMIT 5;
```

### Unique departments alphabetically

```sql
SELECT DISTINCT department
FROM employee
ORDER BY department ASC;
```

### Average salary by department

```sql
SELECT department, AVG(salary) AS avg_salary
FROM employee
GROUP BY department
ORDER BY avg_salary DESC;
```

---

# Quick Revision

| Function / Clause | Purpose                  |
| ----------------- | ------------------------ |
| `COUNT()`         | Counts rows              |
| `SUM()`           | Calculates total         |
| `AVG()`           | Calculates average       |
| `MAX()`           | Finds maximum            |
| `MIN()`           | Finds minimum            |
| `UPPER()`         | Converts to uppercase    |
| `LOWER()`         | Converts to lowercase    |
| `LENGTH()`        | Counts characters        |
| `CONCAT()`        | Joins strings            |
| `ROUND()`         | Rounds decimal values    |
| `DISTINCT`        | Removes duplicates       |
| `ORDER BY ASC`    | Sorts ascending          |
| `ORDER BY DESC`   | Sorts descending         |
| `LIMIT`           | Restricts number of rows |

## Key Patterns to Remember

```sql
-- Highest value
SELECT MAX(column_name)
FROM table_name;

-- Average
SELECT AVG(column_name)
FROM table_name;

-- Sort high → low
SELECT *
FROM table_name
ORDER BY column_name DESC;

-- Top N
SELECT *
FROM table_name
ORDER BY column_name DESC
LIMIT N;

-- Group + aggregate + sorting
SELECT column_name, AVG(value)
FROM table_name
GROUP BY column_name
ORDER BY AVG(value) DESC;
```
**
