# Day 03 — SQL Functions + GROUP BY

## 1. SQL Functions

SQL functions are used to perform operations on data and return a result.

### Aggregate Functions

Aggregate functions perform calculations on multiple rows.

| Function  | Use                 |
| --------- | ------------------- |
| `COUNT()` | Counts rows         |
| `SUM()`   | Calculates total    |
| `AVG()`   | Calculates average  |
| `MAX()`   | Finds maximum value |
| `MIN()`   | Finds minimum value |

### Examples

```sql
SELECT COUNT(*) FROM students;
```

```sql
SELECT SUM(salary) FROM employees;
```

```sql
SELECT AVG(salary) FROM employees;
```

```sql
SELECT MAX(salary) FROM employees;
```

```sql
SELECT MIN(salary) FROM employees;
```

---

## 2. GROUP BY

`GROUP BY` is used to **group rows having the same value**.

It is commonly used with aggregate functions.

### Syntax

```sql
SELECT column, aggregate_function(column)
FROM table_name
GROUP BY column;
```

### Example

Suppose we have an `employees` table:

| name | department | salary |
| ---- | ---------- | -----: |
| A    | IT         |  30000 |
| B    | IT         |  40000 |
| C    | HR         |  25000 |
| D    | HR         |  35000 |

Find the total salary of each department:

```sql
SELECT department, SUM(salary)
FROM employees
GROUP BY department;
```

Output:

```text
IT   70000
HR   60000
```

---

## 3. GROUP BY with COUNT

Find the number of employees in each department:

```sql
SELECT department, COUNT(*)
FROM employees
GROUP BY department;
```

---

## 4. GROUP BY with AVG

Find the average salary of each department:

```sql
SELECT department, AVG(salary)
FROM employees
GROUP BY department;
```

---

## 5. GROUP BY with MAX and MIN

```sql
SELECT department, MAX(salary)
FROM employees
GROUP BY department;
```

```sql
SELECT department, MIN(salary)
FROM employees
GROUP BY department;
```

---

## 6. WHERE with GROUP BY

`WHERE` filters rows **before grouping**.

```sql
SELECT department, AVG(salary)
FROM employees
WHERE salary > 20000
GROUP BY department;
```

### Order

```text
SELECT
FROM
WHERE
GROUP BY
```

---

## 7. HAVING

`HAVING` is used to **filter groups** after `GROUP BY`.

```sql
SELECT department, AVG(salary)
FROM employees
GROUP BY department
HAVING AVG(salary) > 30000;
```

### WHERE vs HAVING

| WHERE                                    | HAVING                         |
| ---------------------------------------- | ------------------------------ |
| Filters rows                             | Filters groups                 |
| Used before `GROUP BY`                   | Used after `GROUP BY`          |
| Cannot normally use aggregate conditions | Used with aggregate conditions |

---

## 8. Important Query Order

Remember this order:

```text
FROM
WHERE
GROUP BY
HAVING
SELECT
ORDER BY
```

### Example

```sql
SELECT department, AVG(salary) AS avg_salary
FROM employees
WHERE salary > 20000
GROUP BY department
HAVING AVG(salary) > 30000
ORDER BY avg_salary DESC;
```

## Key Points

* `COUNT()` → number of rows
* `SUM()` → total
* `AVG()` → average
* `MAX()` → maximum
* `MIN()` → minimum
* `GROUP BY` → creates groups
* `WHERE` → filters rows
* `HAVING` → filters groups
* Aggregate functions are commonly used with `GROUP BY`
