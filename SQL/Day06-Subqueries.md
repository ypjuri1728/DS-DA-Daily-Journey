# Day 06 — SQL Subqueries

##  Topic: Subqueries

A **subquery** is a SQL query written inside another SQL query.

The inner query runs first and its result is used by the outer query.

### Basic Syntax

```sql
SELECT column_name
FROM table_name
WHERE column_name = (
    SELECT column_name
    FROM table_name
);
```

---

## 1. Subquery Basics

Example table: `employees`

| id | name  | salary | department |
| -: | ----- | -----: | ---------- |
|  1 | Rahul |  50000 | IT         |
|  2 | Priya |  70000 | HR         |
|  3 | Aman  |  60000 | IT         |
|  4 | Neha  |  80000 | HR         |

### Example

Find employees who earn more than the average salary:

```sql
SELECT name, salary
FROM employees
WHERE salary > (
    SELECT AVG(salary)
    FROM employees
);
```

### How it works

First:

```sql
SELECT AVG(salary)
FROM employees;
```

Suppose the result is:

```text
65000
```

Then the outer query becomes:

```sql
SELECT name, salary
FROM employees
WHERE salary > 65000;
```

---

# 2. Subquery with WHERE

A subquery is commonly used inside `WHERE`.

### Example

Find employees earning the maximum salary:

```sql
SELECT name, salary
FROM employees
WHERE salary = (
    SELECT MAX(salary)
    FROM employees
);
```

The inner query finds the maximum salary.

The outer query finds the employee having that salary.

---

# 3. Subquery with IN

`IN` is useful when the subquery returns **multiple values**.

### Example

Find employees who work in departments located in a particular group.

```sql
SELECT name, department
FROM employees
WHERE department IN (
    SELECT department
    FROM employees
    WHERE salary > 60000
);
```

The inner query may return:

```text
HR
IT
```

Then the outer query becomes similar to:

```sql
WHERE department IN ('HR', 'IT');
```

### Remember

```sql
IN
```

means:

> Match with any value returned by the subquery.

---

# 4. Subquery with NOT IN

`NOT IN` returns rows that do **not** match the values returned by the subquery.

### Example

```sql
SELECT name, department
FROM employees
WHERE department NOT IN (
    SELECT department
    FROM employees
    WHERE salary > 60000
);
```

### Remember

```sql
IN      → matching values
NOT IN  → non-matching values
```

>  Be careful with `NULL` values when using `NOT IN`, because they can cause unexpected results.

---

# 5. Subquery with = and Comparison Operators

A subquery can be used with comparison operators.

Common operators:

```text
=
>
<
>=
<=
<>
```

### Example: `=`

Find the employee with the highest salary:

```sql
SELECT name
FROM employees
WHERE salary = (
    SELECT MAX(salary)
    FROM employees
);
```

### Example: `>`

Find employees earning more than the average:

```sql
SELECT name, salary
FROM employees
WHERE salary > (
    SELECT AVG(salary)
    FROM employees
);
```

### Example: `<`

Find employees earning less than the average:

```sql
SELECT name, salary
FROM employees
WHERE salary < (
    SELECT AVG(salary)
    FROM employees
);
```

---

# 6. Subquery with MAX()

Find the employee with the highest salary.

```sql
SELECT name, salary
FROM employees
WHERE salary = (
    SELECT MAX(salary)
    FROM employees
);
```

### Important

`MAX()` returns the largest value.

---

# 7. Subquery with MIN()

Find the employee with the lowest salary.

```sql
SELECT name, salary
FROM employees
WHERE salary = (
    SELECT MIN(salary)
    FROM employees
);
```

`MIN()` returns the smallest value.

---

# 8. Subquery with AVG()

Find employees earning more than the average salary.

```sql
SELECT name, salary
FROM employees
WHERE salary > (
    SELECT AVG(salary)
    FROM employees
);
```

`AVG()` returns the average value.

---

# 9. Correlated Subquery

A **correlated subquery** depends on the current row of the outer query.

The inner query runs for each row of the outer query.

### Example

Find employees whose salary is greater than the average salary of their own department.

```sql
SELECT e1.name, e1.salary, e1.department
FROM employees e1
WHERE e1.salary > (
    SELECT AVG(e2.salary)
    FROM employees e2
    WHERE e2.department = e1.department
);
```

### Important Difference

Normal subquery:

```text
Outer query
     ↓
Inner query runs independently
```

Correlated subquery:

```text
Outer row
     ↓
Inner query uses outer row
     ↓
Next outer row
     ↓
Inner query runs again
```

---

# 10. Subquery vs JOIN

Both **Subqueries** and **JOINs** can be used to solve similar problems, but they work differently.

### Subquery

```sql
SELECT name
FROM employees
WHERE department_id IN (
    SELECT id
    FROM departments
    WHERE location = 'Delhi'
);
```

### JOIN

```sql
SELECT e.name
FROM employees e
JOIN departments d
ON e.department_id = d.id
WHERE d.location = 'Delhi';
```

### General Difference

| Subquery                         | JOIN                                            |
| -------------------------------- | ----------------------------------------------- |
| Query inside another query       | Combines tables                                 |
| Easy for some filtering problems | Good for combining related data                 |
| Can be easier to read initially  | Often preferred for complex table relationships |
| Can be correlated                | Uses join conditions                            |

### Remember

Don't think:

> Subquery is always better than JOIN.

Instead ask:

> Which approach makes this problem simpler and clearer?

---

# 11. Important Rules

### Rule 1 — Single value subquery

If the subquery returns one value, comparison operators can be used.

```sql
=
>
<
>=
<=
```

Example:

```sql
WHERE salary > (
    SELECT AVG(salary)
    FROM employees
);
```

---

### Rule 2 — Multiple value subquery

If the subquery returns multiple values, use operators such as:

```sql
IN
NOT IN
```

Example:

```sql
WHERE department IN (
    SELECT department
    FROM employees
);
```

---

### Rule 3 — Subquery with aggregate functions

Common examples:

```sql
MAX()
MIN()
AVG()
```

Example:

```sql
WHERE salary = (
    SELECT MAX(salary)
    FROM employees
);
```

---

# 12. How to Think About Subqueries

When you see a question like:

> Find employees earning more than the average salary.

Think in **two steps**.

### Step 1 — Find the value

```sql
SELECT AVG(salary)
FROM employees;
```

### Step 2 — Use that value

```sql
SELECT name, salary
FROM employees
WHERE salary > average_salary;
```

Then combine them:

```sql
SELECT name, salary
FROM employees
WHERE salary > (
    SELECT AVG(salary)
    FROM employees
);
```

### Mental Model

```text
Question
   ↓
What value do I need first?
   ↓
Write inner query
   ↓
Use that result in outer query
```

---


# 14. Quick Revision

| Concept             | Meaning                                |
| ------------------- | -------------------------------------- |
| Subquery            | Query inside another query             |
| `IN`                | Matches any value returned by subquery |
| `NOT IN`            | Does not match returned values         |
| `=`                 | Compare with one returned value        |
| `MAX()`             | Largest value                          |
| `MIN()`             | Smallest value                         |
| `AVG()`             | Average value                          |
| Correlated subquery | Inner query depends on outer query     |
| JOIN                | Combines related tables                |

---

##  Key Takeaways

```text
Subquery = Query inside Query

Single value
→ =, >, <, >=, <=

Multiple values
→ IN, NOT IN

Aggregate
→ MAX(), MIN(), AVG()

Correlated subquery
→ Inner query uses outer query

Subquery vs JOIN
→ Choose the simpler and clearer solution
```


