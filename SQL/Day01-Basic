# SQL Day 01 — Basics

##  What is SQL?

**SQL (Structured Query Language)** is a language used to communicate with a database.

We use SQL to:

- Create databases and tables
- Insert data
- Read data
- Update data
- Delete data

```text
SQL
 ↓
Database
 ↓
Tables
 ↓
Rows + Columns
```

---

##  What is a Database?

A **database** is an organized collection of data.

Example:

```text
College Database
      ↓
   Students Table
      ↓
 ┌────┬────────┬─────┐
 │ ID │ Name   │ Age │
 ├────┼────────┼─────┤
 │ 1  │ Priya  │ 21  │
 │ 2  │ Rahul  │ 22  │
 └────┴────────┴─────┘
```

---

## Table

A **table** stores data in rows and columns.

- **Row** → One complete record.
- **Column** → A specific type/category of data.
- **Primary Key** → Uniquely identifies each row.

Example:

| id | name | age | course |
|---:|------|---:|--------|
| 1 | Priya | 21 | CSE |
| 2 | Rahul | 22 | IT |

Here:

```text
id      → Column
Priya   → Data
1       → Primary Key value
One row → One student record
```

---

## Primary Key

A **Primary Key** is used to uniquely identify each record.

```sql
id INT PRIMARY KEY
```

Rules:

- Must be unique.
- Cannot be `NULL`.
- A table normally has one primary key.

Example:

```text
1 → Priya
2 → Rahul
3 → Aman
```

---

## Basic SQL Data Types

| Data Type | Use | Example |
|---|---|---|
| `INT` | Whole numbers | `21` |
| `VARCHAR` | Text | `'Priya'` |
| `DECIMAL` | Decimal numbers | `85.50` |
| `DATE` | Date | `'2026-08-17'` |

---

#  SQL Commands

## 1. CREATE DATABASE

Creates a new database.

```sql
CREATE DATABASE college;
```

---

## 2. USE

Selects the database that we want to work with.

```sql
USE college;
```

---

## 3. CREATE TABLE

Creates a new table.

```sql
CREATE TABLE students (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    course VARCHAR(50)
);
```

---

## 4. INSERT INTO

Adds records into a table.

```sql
INSERT INTO students (id, name, age, course)
VALUES
(1, 'Priya', 21, 'CSE'),
(2, 'Rahul', 22, 'IT'),
(3, 'Aman', 20, 'CSE');
```

---

## 5. SELECT

Used to retrieve/read data.

### Select all columns

```sql
SELECT * FROM students;
```

`*` means **all columns**.

### Select specific columns

```sql
SELECT name, course
FROM students;
```

---

## 6. UPDATE

Used to modify existing data.

```sql
UPDATE students
SET age = 22
WHERE id = 1;
```

`WHERE` tells SQL **which row should be updated**.

---

## 7. DELETE

Used to delete a record.

```sql
DELETE FROM students
WHERE id = 3;
```

 Always use `WHERE` when you only want to delete specific rows.

---

# SQL Query Structure

Example:

```sql
SELECT name
FROM students
WHERE age > 20;
```

Think of it as:

```text
SELECT → What data do I want?
FROM   → From which table?
WHERE  → Which records?
```

---

# Quick Revision

| Command | Meaning |
|---|---|
| `CREATE DATABASE` | Create database |
| `USE` | Select database |
| `CREATE TABLE` | Create table |
| `INSERT INTO` | Add data |
| `SELECT` | Read data |
| `UPDATE` | Modify data |
| `DELETE` | Remove data |

### Easy Memory Trick

```text
CREATE → Create
INSERT → Add
SELECT → Read
UPDATE → Change
DELETE → Remove
```
