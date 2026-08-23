# Day 07 — SQL CASE Statement

## 1. What is CASE?

`CASE` is used in SQL to apply **if-else logic**.

It allows us to return different values based on conditions.

### Basic Syntax

```sql
SELECT column_name,
       CASE
           WHEN condition THEN result
           WHEN condition THEN result
           ELSE result
       END AS new_column
FROM table_name;
```

Think of it like:

```text
IF condition → result
ELSE IF condition → result
ELSE → result
```

---

## 2. Simple Example

Suppose we have a `students` table:

| name  | marks |
| ----- | ----: |
| Ravi  |    95 |
| Priya |    82 |
| Aman  |    65 |
| Rahul |    40 |

Query:

```sql
SELECT name,
       marks,
       CASE
           WHEN marks >= 90 THEN 'A'
           WHEN marks >= 75 THEN 'B'
           WHEN marks >= 50 THEN 'C'
           ELSE 'Fail'
       END AS grade
FROM students;
```

### Output

| name  | marks | grade |
| ----- | ----: | ----- |
| Ravi  |    95 | A     |
| Priya |    82 | B     |
| Aman  |    65 | C     |
| Rahul |    40 | Fail  |

---

# 3. CASE with ELSE

`ELSE` is used when **none of the conditions are true**.

```sql
SELECT name,
       CASE
           WHEN marks >= 50 THEN 'Pass'
           ELSE 'Fail'
       END AS result
FROM students;
```

If `marks = 70`:

```text
70 >= 50 → TRUE → Pass
```

If `marks = 40`:

```text
40 >= 50 → FALSE → Fail
```

---

# 4. Multiple WHEN Conditions

We can use multiple `WHEN` conditions.

```sql
SELECT name,
       marks,
       CASE
           WHEN marks >= 90 THEN 'Excellent'
           WHEN marks >= 75 THEN 'Good'
           WHEN marks >= 50 THEN 'Average'
           ELSE 'Poor'
       END AS performance
FROM students;
```

### Important

SQL checks the conditions **from top to bottom**.

For example:

```text
marks = 95

95 >= 90 → TRUE
```

So SQL returns:

```text
Excellent
```

It does not check the remaining conditions.

---

# 5. CASE Without ELSE

`ELSE` is optional.

```sql
SELECT name,
       CASE
           WHEN marks >= 50 THEN 'Pass'
       END AS result
FROM students;
```

If no condition matches, SQL returns:

```text
NULL
```

---

# 6. CASE with Comparison Operators

We can use:

```text
>
<
>=
<=
=
<>
```

Example:

```sql
SELECT name,
       salary,
       CASE
           WHEN salary >= 50000 THEN 'High'
           WHEN salary >= 30000 THEN 'Medium'
           ELSE 'Low'
       END AS salary_level
FROM employees;
```

---

# 7. CASE with AND

We can use multiple conditions with `AND`.

```sql
SELECT name,
       marks,
       attendance,
       CASE
           WHEN marks >= 50 AND attendance >= 75 THEN 'Pass'
           ELSE 'Fail'
       END AS result
FROM students;
```

Both conditions must be true.

```text
marks >= 50
AND
attendance >= 75
```

---

# 8. CASE with OR

We can also use `OR`.

```sql
SELECT name,
       marks,
       CASE
           WHEN marks >= 90 OR marks <= 40 THEN 'Special'
           ELSE 'Normal'
       END AS category
FROM students;
```

Only one condition needs to be true.

---

# 9. CASE with IN

`IN` can also be used inside `CASE`.

```sql
SELECT name,
       department,
       CASE
           WHEN department IN ('IT', 'CSE') THEN 'Technical'
           ELSE 'Non-Technical'
       END AS category
FROM employees;
```

---

# 10. CASE with BETWEEN

```sql
SELECT name,
       marks,
       CASE
           WHEN marks BETWEEN 90 AND 100 THEN 'A'
           WHEN marks BETWEEN 75 AND 89 THEN 'B'
           WHEN marks BETWEEN 50 AND 74 THEN 'C'
           ELSE 'Fail'
       END AS grade
FROM students;
```

---

# 11. CASE with ORDER BY

`CASE` can be used to create a custom sorting order.

Example:

```sql
SELECT name, department
FROM employees
ORDER BY
    CASE
        WHEN department = 'IT' THEN 1
        WHEN department = 'HR' THEN 2
        ELSE 3
    END;
```

This gives priority:

```text
IT
HR
Other departments
```

---

# 12. CASE with Aggregate Functions

We can use `CASE` inside functions such as `SUM()`.

Example:

```sql
SELECT
    SUM(
        CASE
            WHEN marks >= 50 THEN 1
            ELSE 0
        END
    ) AS passed_students
FROM students;
```

### How it works

For every student:

```text
Pass → 1
Fail → 0
```

Then:

```text
SUM(1 + 1 + 0 + 1 ...)
```

gives the total number of passed students.

---

# 13. CASE with GROUP BY

Example:

```sql
SELECT
    CASE
        WHEN salary >= 50000 THEN 'High Salary'
        ELSE 'Low Salary'
    END AS salary_group,
    COUNT(*) AS total
FROM employees
GROUP BY
    CASE
        WHEN salary >= 50000 THEN 'High Salary'
        ELSE 'Low Salary'
    END;
```

This groups employees into:

```text
High Salary
Low Salary
```

---

# 14. CASE with NULL

We can check for `NULL` using `IS NULL`.

```sql
SELECT name,
       CASE
           WHEN phone IS NULL THEN 'Not Available'
           ELSE 'Available'
       END AS phone_status
FROM students;
```

### Important

Do NOT write:

```sql
phone = NULL
```

Use:

```sql
phone IS NULL
```

---

# 15. Simple CASE vs Searched CASE

## Simple CASE

It compares one column with different values.

```sql
SELECT name,
       CASE department
           WHEN 'IT' THEN 'Technical'
           WHEN 'HR' THEN 'Management'
           ELSE 'Other'
       END AS category
FROM employees;
```

Here:

```text
CASE department
```

means SQL checks the value of `department`.

---

# 16. Important CASE Rules

### Rule 1

Always close `CASE` with:

```sql
END
```

### Rule 2

Conditions are checked from **top to bottom**.

### Rule 3

The first matching `WHEN` is returned.

### Rule 4

`ELSE` is optional.

### Rule 5

Use `AS` to give the calculated column a name.

```sql
END AS grade
```

---

# Dry Run

Query:

```sql
SELECT name,
       marks,
       CASE
           WHEN marks >= 90 THEN 'A'
           WHEN marks >= 75 THEN 'B'
           WHEN marks >= 50 THEN 'C'
           ELSE 'Fail'
       END AS grade
FROM students;
```

Suppose:

```text
name = Priya
marks = 82
```

SQL checks:

```text
82 >= 90
NO

82 >= 75
YES
```

So:

```text
grade = B
```

It stops checking after the first true condition.

---

# Real-Life Understanding

Think of `CASE` like an `if-else` statement in programming.

### Java

```java
if (marks >= 90) {
    grade = "A";
}
else if (marks >= 75) {
    grade = "B";
}
else {
    grade = "Fail";
}
```

### SQL

```sql
CASE
    WHEN marks >= 90 THEN 'A'
    WHEN marks >= 75 THEN 'B'
    ELSE 'Fail'
END
```

So remember:

```text
Java if
      ↓
SQL WHEN

Java else if
      ↓
SQL WHEN

Java else
      ↓
SQL ELSE
```

---



#  Quick Revision

| Concept       | Meaning                        |
| ------------- | ------------------------------ |
| `CASE`        | SQL if-else                    |
| `WHEN`        | Condition                      |
| `THEN`        | Result if condition is true    |
| `ELSE`        | Result if no condition matches |
| `END`         | Ends CASE                      |
| `AS`          | Gives alias/name               |
| Simple CASE   | Compares one value             |
| Searched CASE | Checks conditions              |

### Most Important Pattern

```sql
CASE
    WHEN condition THEN result
    WHEN condition THEN result
    ELSE result
END
```

### Remember

```text
CASE = IF / ELSE IF / ELSE
```

---

## Day 07 Summary

Today we learned how to use `CASE` to:

* Apply conditional logic
* Categorize data
* Create grades/statuses
* Use `AND`, `OR`, `IN`, and `BETWEEN`
* Handle `NULL`
* Create custom sorting with `ORDER BY`
* Combine `CASE` with aggregate functions
* Use `CASE` with `GROUP BY`
* Understand Simple CASE and Searched CASE
