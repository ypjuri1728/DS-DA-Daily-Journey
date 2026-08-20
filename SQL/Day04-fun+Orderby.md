# Day 03 — SQL ORDER BY + DISTINCT + LIMIT + CASE

## 1. ORDER BY

`ORDER BY` is used to **sort the result** of a query.

### Ascending Order

Smallest → Largest / A → Z

```sql
SELECT *
FROM employee
ORDER BY salary ASC;
```

`ASC` is the default, so this also works:

```sql
SELECT *
FROM employee
ORDER BY salary;
```

### Descending Order

Largest → Smallest / Z → A

```sql
SELECT *
FROM employee
ORDER BY salary DESC;
```

---

## 2. ORDER BY Multiple Columns

We can sort by more than one column.

```sql
SELECT name, department, salary
FROM employee
ORDER BY department ASC, salary DESC;
```

First, employees are sorted by `department`.

If two employees belong to the same department, they are sorted by `salary` from highest to lowest.

---

## 3. ORDER BY with WHERE

`WHERE` filters the rows, and `ORDER BY` sorts the filtered result.

```sql
SELECT name, salary
FROM employee
WHERE salary > 30000
ORDER BY salary DESC;
```

### Execution idea

```text
FROM → WHERE → ORDER BY
```

---

## 4. ORDER BY with Alias

We can give a calculated column an alias using `AS` and then sort using that alias.

```sql
SELECT name, salary * 12 AS annual_salary
FROM employee
ORDER BY annual_salary DESC;
```

This sorts employees by their annual salary.

---

# 5. LIMIT

`LIMIT` is used to restrict the number of rows returned.

```sql
SELECT *
FROM employee
LIMIT 5;
```

Returns only 5 rows.

### Top 3 Highest Salaries

```sql
SELECT name, salary
FROM employee
ORDER BY salary DESC
LIMIT 3;
```

### Top 5 Students

```sql
SELECT name, marks
FROM student
ORDER BY marks DESC
LIMIT 5;
```

### Bottom 3 Salaries

```sql
SELECT name, salary
FROM employee
ORDER BY salary ASC
LIMIT 3;
```

### Important Pattern

```sql
SELECT columns
FROM table_name
ORDER BY column_name DESC
LIMIT N;
```

This pattern is commonly used for **Top N problems**.

---

# 6. DISTINCT

`DISTINCT` removes duplicate values from the result.

```sql
SELECT DISTINCT department
FROM employee;
```

If the table contains:

```text
IT
HR
IT
Sales
HR
```

The result will be:

```text
IT
HR
Sales
```

---

## DISTINCT with ORDER BY

```sql
SELECT DISTINCT department
FROM employee
ORDER BY department ASC;
```

This gives unique departments in alphabetical order.

---

# 7. NULL Values

`NULL` represents a missing or unknown value.

We should **not** use:

```sql
WHERE phone = NULL;
```

Instead, use `IS NULL`.

### Find NULL values

```sql
SELECT *
FROM employee
WHERE phone IS NULL;
```

### Find non-NULL values

```sql
SELECT *
FROM employee
WHERE phone IS NOT NULL;
```

---

# 8. COALESCE()

`COALESCE()` is used to replace `NULL` with another value.

```sql
SELECT name,
       COALESCE(phone, 'Not Available') AS phone
FROM employee;
```

If `phone` is `NULL`, the result will show:

```text
Not Available
```

instead of `NULL`.

### Another Example

```sql
SELECT name,
       COALESCE(salary, 0) AS salary
FROM employee;
```

If salary is `NULL`, it displays `0`.

---

# 9. CASE WHEN

`CASE` is used to create conditional logic inside SQL.

It works similar to `if-else`.

### Syntax

```sql
CASE
    WHEN condition THEN result
    WHEN condition THEN result
    ELSE result
END
```

### Example

```sql
SELECT name, salary,
       CASE
           WHEN salary >= 50000 THEN 'High'
           WHEN salary >= 30000 THEN 'Medium'
           ELSE 'Low'
       END AS salary_category
FROM employee;
```

Example result:

| name  | salary | salary_category |
| ----- | -----: | --------------- |
| Rahul |  60000 | High            |
| Aman  |  40000 | Medium          |
| Raj   |  20000 | Low             |

---

# 10. CASE with Marks

```sql
SELECT name, marks,
       CASE
           WHEN marks >= 90 THEN 'A'
           WHEN marks >= 75 THEN 'B'
           WHEN marks >= 60 THEN 'C'
           ELSE 'D'
       END AS grade
FROM student;
```

---

# 11. CASE with ORDER BY

We can also sort using a `CASE` expression.

```sql
SELECT name, salary,
       CASE
           WHEN salary >= 50000 THEN 'High'
           WHEN salary >= 30000 THEN 'Medium'
           ELSE 'Low'
       END AS category
FROM employee
ORDER BY salary DESC;
```

---

# 12. Important Combined Queries

### Top 5 employees earning more than 30,000

```sql
SELECT name, salary
FROM employee
WHERE salary > 30000
ORDER BY salary DESC
LIMIT 5;
```

### Unique departments in alphabetical order

```sql
SELECT DISTINCT department
FROM employee
ORDER BY department ASC;
```

### Employees with missing phone numbers

```sql
SELECT name, phone
FROM employee
WHERE phone IS NULL;
```

### Replace NULL phone numbers

```sql
SELECT name,
       COALESCE(phone, 'Not Available') AS phone
FROM employee;
```

### Categorize employees by salary

```sql
SELECT name, salary,
       CASE
           WHEN salary >= 50000 THEN 'High'
           WHEN salary >= 30000 THEN 'Medium'
           ELSE 'Low'
       END AS category
FROM employee;
```

### Top 3 salaries with names

```sql
SELECT name, salary
FROM employee
ORDER BY salary DESC
LIMIT 3;
```

---

# 13. SQL Query Order

A useful order to remember:

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

# 14. Quick Revision

| Concept       | Purpose                  |
| ------------- | ------------------------ |
| `ORDER BY`    | Sorts results            |
| `ASC`         | Ascending order          |
| `DESC`        | Descending order         |
| `LIMIT`       | Restricts number of rows |
| `DISTINCT`    | Removes duplicates       |
| `IS NULL`     | Finds NULL values        |
| `IS NOT NULL` | Finds non-NULL values    |
| `COALESCE()`  | Replaces NULL            |
| `CASE WHEN`   | Conditional logic        |
| `AS`          | Creates an alias         |

## Most Important Patterns

### Sort

```sql
SELECT *
FROM table_name
ORDER BY column_name DESC;
```

### Top N

```sql
SELECT *
FROM table_name
ORDER BY column_name DESC
LIMIT N;
```

### Unique values

```sql
SELECT DISTINCT column_name
FROM table_name
ORDER BY column_name;
```

### NULL check

```sql
SELECT *
FROM table_name
WHERE column_name IS NULL;
```

### Replace NULL

```sql
SELECT COALESCE(column_name, 'Default Value')
FROM table_name;
```

### Conditional column

```sql
SELECT column_name,
       CASE
           WHEN condition THEN 'Result 1'
           ELSE 'Result 2'
       END AS category
FROM table_name;
```
