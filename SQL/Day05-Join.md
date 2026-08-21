# SQL Day 05 — JOINS

## 1. What is JOIN?

`JOIN` is used to combine data from **two or more tables** using a related column.

### Basic Syntax

```sql
SELECT columns
FROM table1
JOIN table2
ON table1.column = table2.column;
```

---

## 2. INNER JOIN

Returns only the rows that have a **matching value in both tables**.

```sql
SELECT s.name, f.name
FROM student s
INNER JOIN faculty f
ON s.advisor = f.employee_id;
```

**Think:**

> Give me only matching records.

---

## 3. LEFT JOIN

Returns **all rows from the left table** and matching rows from the right table.

If there is no match, the right-side columns become `NULL`.

```sql
SELECT s.name, f.name
FROM student s
LEFT JOIN faculty f
ON s.advisor = f.employee_id;
```

**Think:**

> Keep everything from the left table.

---

## 4. RIGHT JOIN

Returns **all rows from the right table** and matching rows from the left table.

```sql
SELECT s.name, f.name
FROM student s
RIGHT JOIN faculty f
ON s.advisor = f.employee_id;
```

**Think:**

> Keep everything from the right table.

---

## 5. FULL OUTER JOIN

Returns **all rows from both tables**.

Matching rows are combined. Non-matching rows contain `NULL`.

```sql
SELECT s.name, f.name
FROM student s
FULL OUTER JOIN faculty f
ON s.advisor = f.employee_id;
```

**Note:** MySQL does not directly support `FULL OUTER JOIN`.

---

## 6. SELF JOIN

A table is joined with **itself**.

```sql
SELECT e1.name AS employee,
       e2.name AS manager
FROM employee e1
JOIN employee e2
ON e1.manager_id = e2.employee_id;
```

**Think:**

> Same table, two different roles.

---

## 7. CROSS JOIN

Returns **every possible combination** of rows from both tables.

```sql
SELECT s.name, c.course_name
FROM student s
CROSS JOIN course c;
```

If:

* Students = 3 rows
* Courses = 4 rows

Result = `3 × 4 = 12` rows.

---

# 8. JOIN + WHERE

First combine related tables, then filter the result.

```sql
SELECT s.name, f.name
FROM student s
JOIN faculty f
ON s.advisor = f.employee_id
WHERE f.salary > 50000;
```

---

# 9. JOIN + GROUP BY

JOIN tables and then group the result.

```sql
SELECT f.name, COUNT(s.student_id) AS total_students
FROM faculty f
JOIN student s
ON f.employee_id = s.advisor
GROUP BY f.name;
```

---

# 10. JOIN + GROUP BY + HAVING

```sql
SELECT f.name, COUNT(s.student_id) AS total_students
FROM faculty f
JOIN student s
ON f.employee_id = s.advisor
GROUP BY f.name
HAVING COUNT(s.student_id) > 5;
```

---

# 11. JOIN + ORDER BY

```sql
SELECT s.name, f.name, f.salary
FROM student s
JOIN faculty f
ON s.advisor = f.employee_id
ORDER BY f.salary DESC;
```

---

# 12. WHERE vs ON

### ON

Defines **how two tables are connected**.

```sql
ON s.advisor = f.employee_id
```

### WHERE

Filters the final result.

```sql
WHERE f.salary > 50000
```

---

# 13. Most Important JOIN Pattern

When solving SQL questions, think:

```text
1. What tables do I need?
        ↓
2. How are they connected?
        ↓
3. Which JOIN?
        ↓
4. What columns should I SELECT?
        ↓
5. Do I need WHERE?
        ↓
6. Do I need GROUP BY?
        ↓
7. Do I need HAVING?
        ↓
8. Do I need ORDER BY?
```

---

# 14. Quick JOIN Cheat Sheet

| JOIN              | What it returns            |
| ----------------- | -------------------------- |
| `INNER JOIN`      | Matching rows from both    |
| `LEFT JOIN`       | All left + matching right  |
| `RIGHT JOIN`      | All right + matching left  |
| `FULL OUTER JOIN` | Everything from both       |
| `SELF JOIN`       | Table joined with itself   |
| `CROSS JOIN`      | Every possible combination |

### ⭐ Remember

```text
INNER → only matching
LEFT  → keep left
RIGHT → keep right
FULL  → keep both
SELF  → same table
CROSS → every combination
```

---

## 15. Basic JOIN Template

```sql
SELECT columns
FROM table1
JOIN table2
ON table1.common_column = table2.common_column
WHERE condition
GROUP BY column
HAVING condition
ORDER BY column;
```

### ⭐ Main Goal

Don't memorize JOIN queries.

Learn to identify:

**Tables → Relationship → JOIN type → Filter → Group → Sort**
