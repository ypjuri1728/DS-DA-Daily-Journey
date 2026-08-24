# SQL Day 08 — UNION & UNION ALL

## 1. UNION

`UNION` is used to combine the result of two or more `SELECT` queries.

- Removes duplicate rows.
- Both queries must have the same number of columns.
- Columns should have compatible data types.
- Column names come from the first `SELECT`.

### Syntax

    SELECT column1, column2
    FROM table1
    UNION
    SELECT column1, column2
    FROM table2;

### Example

    SELECT name FROM students
    UNION
    SELECT name FROM teachers;

---

## 2. UNION ALL

`UNION ALL` also combines results of multiple `SELECT` queries.

- Keeps duplicate rows.
- Generally faster than `UNION`.

### Syntax

    SELECT column1, column2
    FROM table1
    UNION ALL
    SELECT column1, column2
    FROM table2;

### Example

    SELECT name FROM students
    UNION ALL
    SELECT name FROM teachers;

---

## 3. UNION vs UNION ALL

| UNION | UNION ALL |
|---|---|
| Removes duplicates | Keeps duplicates |
| Generally slower | Generally faster |
| Performs duplicate removal | Does not remove duplicates |
| Used for unique results | Used when all records are needed |

### Easy Trick

    UNION     → Unique
    UNION ALL → All

---

## 4. Rules of UNION

For `UNION` and `UNION ALL`:

1. Same number of columns.
2. Compatible data types.
3. Columns should be in the same logical order.

### Example

    SELECT name, age
    FROM students

    UNION

    SELECT name, age
    FROM teachers;

---

## 5. Different Column Names

Column names do not have to be the same.

    SELECT student_name, age
    FROM students

    UNION

    SELECT teacher_name, age
    FROM teachers;

The final result uses the column names from the **first SELECT**.

---

## 6. UNION with WHERE

    SELECT name
    FROM students
    WHERE age > 18

    UNION

    SELECT name
    FROM teachers
    WHERE age > 30;

Each `SELECT` can have its own `WHERE` condition.

---

## 7. UNION with ORDER BY

`ORDER BY` is written at the end of the complete UNION query.

    SELECT name, age
    FROM students

    UNION

    SELECT name, age
    FROM teachers

    ORDER BY age;

---

## 8. UNION with Multiple Queries

We can combine more than two queries.

    SELECT name FROM students

    UNION

    SELECT name FROM teachers

    UNION

    SELECT name FROM employees;

---

## 9. UNION vs JOIN

### UNION

Combines **rows** from different queries.

    Table A
       ↓
     UNION
       ↓
    Table B
       ↓
    Combined Rows

### JOIN

Combines **columns** from related tables.

    Table A + Table B
           ↓
          JOIN
           ↓
      More Columns

### Remember

    UNION → combines rows
    JOIN  → combines columns

---

## 10. When to Use UNION

### Use UNION when:

- You need unique records.
- You want to combine similar results.
- Duplicate records should be removed.

### Use UNION ALL when:

- You need every record.
- Duplicate records are meaningful.
- You don't need duplicate removal.
- Better performance is preferred.

---

# Interview Questions

### Q1. What is UNION?

`UNION` combines the results of multiple `SELECT` queries and removes duplicate rows.

### Q2. Difference between UNION and UNION ALL?

`UNION` removes duplicates, while `UNION ALL` keeps duplicates.

### Q3. Which is faster: UNION or UNION ALL?

`UNION ALL` is generally faster because it does not perform duplicate elimination.

### Q4. Can UNION combine queries having different numbers of columns?

No. Both queries must return the same number of columns.

### Q5. Difference between UNION and JOIN?

`UNION` combines rows, while `JOIN` combines columns from related tables.

---

# Quick Revision

    UNION
    → Combines results
    → Removes duplicates

    UNION ALL
    → Combines results
    → Keeps duplicates

    UNION Rules
    → Same number of columns
    → Compatible data types
    → Same logical order

    ORDER BY
    → Write at the end

    UNION → Rows
    JOIN  → Columns
