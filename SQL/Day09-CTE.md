# Day 09 — SQL CTE (Common Table Expressions)

##  What is a CTE?

**CTE = Common Table Expression**

A CTE is a temporary result set that we can use inside a SQL query.

It makes complex queries **shorter, cleaner, and easier to understand**.

### Basic Syntax

```sql
WITH cte_name AS (
    SELECT column1, column2
    FROM table_name
    WHERE condition
)
SELECT *
FROM cte_name;
```

---

# 1. Simple CTE

```sql
WITH employee_data AS (
    SELECT name, salary
    FROM employees
)
SELECT *
FROM employee_data;
```

The CTE `employee_data` stores the result of the first query and the main query uses it.

---

# 2. CTE with WHERE

```sql
WITH high_salary AS (
    SELECT name, salary
    FROM employees
    WHERE salary > 50000
)
SELECT *
FROM high_salary;
```

### Result

Only employees whose salary is greater than `50000`.

---

# 3. CTE with Aggregate Functions

```sql
WITH salary_data AS (
    SELECT department, AVG(salary) AS avg_salary
    FROM employees
    GROUP BY department
)
SELECT *
FROM salary_data;
```

This calculates the average salary for each department.

---

# 4. CTE with ORDER BY

```sql
WITH employee_data AS (
    SELECT name, salary
    FROM employees
)
SELECT *
FROM employee_data
ORDER BY salary DESC;
```

---

# 5. CTE with Multiple Columns

```sql
WITH employee_data AS (
    SELECT 
        id,
        name,
        department,
        salary
    FROM employees
)
SELECT *
FROM employee_data;
```

A CTE can contain multiple columns.

---

# 6. Multiple CTEs

We can create more than one CTE using commas.

```sql
WITH
high_salary AS (
    SELECT name, salary
    FROM employees
    WHERE salary > 50000
),
sales_team AS (
    SELECT name, department
    FROM employees
    WHERE department = 'Sales'
)
SELECT *
FROM high_salary;
```

---

# 7. Using One CTE Inside Another

```sql
WITH employee_data AS (
    SELECT *
    FROM employees
    WHERE salary > 50000
),
sales_data AS (
    SELECT *
    FROM employee_data
    WHERE department = 'Sales'
)
SELECT *
FROM sales_data;
```

Here:

```text
employees
    ↓
employee_data
    ↓
sales_data
    ↓
Final Result
```

---

# 8. CTE with JOIN

```sql
WITH employee_data AS (
    SELECT id, name, department
    FROM employees
)
SELECT 
    employee_data.name,
    departments.department_name
FROM employee_data
JOIN departments
ON employee_data.department = departments.id;
```

CTEs can be used with `JOIN`.

---

# 9. CTE with GROUP BY and HAVING

```sql
WITH department_salary AS (
    SELECT 
        department,
        AVG(salary) AS avg_salary
    FROM employees
    GROUP BY department
)
SELECT *
FROM department_salary
WHERE avg_salary > 50000;
```

---

# CTE vs Subquery

| CTE                        | Subquery                     |
| -------------------------- | ---------------------------- |
| Uses `WITH`                | Uses nested `SELECT`         |
| Easier to read             | Can become difficult to read |
| Can define multiple CTEs   | Usually nested inside query  |
| Good for complex queries   | Good for smaller queries     |
| Can be reused in the query | Usually used once            |

### Subquery

```sql
SELECT *
FROM (
    SELECT name, salary
    FROM employees
    WHERE salary > 50000
) AS temp;
```

### CTE

```sql
WITH high_salary AS (
    SELECT name, salary
    FROM employees
    WHERE salary > 50000
)
SELECT *
FROM high_salary;
```

Both can produce the same result.

---

# 10. CTE vs Temporary Table

| CTE                          | Temporary Table                        |
| ---------------------------- | -------------------------------------- |
| Exists only during the query | Can exist for a session                |
| Created using `WITH`         | Created using `CREATE TEMPORARY TABLE` |
| No separate table creation   | Creates a temporary table              |
| Good for query organization  | Good for storing intermediate data     |

---

# 11. Recursive CTE

A **Recursive CTE** is a CTE that refers to itself.

It is useful for hierarchical data such as:

* Employee → Manager
* Parent → Child
* Folder structures
* Organization hierarchy

### Basic Structure

```sql
WITH RECURSIVE cte_name AS (

    -- Anchor query
    SELECT ...

    UNION ALL

    -- Recursive query
    SELECT ...
    FROM cte_name
    WHERE condition
)

SELECT *
FROM cte_name;
```

### Simple Example

```sql
WITH RECURSIVE numbers AS (
    SELECT 1 AS num

    UNION ALL

    SELECT num + 1
    FROM numbers
    WHERE num < 5
)
SELECT *
FROM numbers;
```

### Output

```text
1
2
3
4
5
```

### Important

Recursive CTE usually has two parts:

```text
Anchor Query
     ↓
UNION ALL
     ↓
Recursive Query
```

---

# 12. CTE with UPDATE

CTEs can also be used with `UPDATE` in databases that support this syntax.

```sql
WITH high_salary AS (
    SELECT id
    FROM employees
    WHERE salary > 80000
)
UPDATE employees
SET bonus = 5000
WHERE id IN (
    SELECT id
    FROM high_salary
);
```

---

# 13. CTE with DELETE

```sql
WITH old_employees AS (
    SELECT id
    FROM employees
    WHERE joining_year < 2020
)
DELETE FROM employees
WHERE id IN (
    SELECT id
    FROM old_employees
);
```

---

#  Important CTE Syntax

```sql
WITH cte_name AS (
    SELECT ...
)
SELECT *
FROM cte_name;
```

### Multiple CTEs

```sql
WITH cte1 AS (
    SELECT ...
),
cte2 AS (
    SELECT ...
)
SELECT *
FROM cte2;
```

---

#  Easy Trick

Remember:

```text
WITH → Create CTE
AS   → Define query
SELECT → Use CTE
```

Example:

```sql
WITH data AS (
    SELECT *
    FROM employees
)
SELECT *
FROM data;
```

---

# 🔥 Important Interview Questions

### Q1. What is a CTE?

A CTE is a temporary named result set created using the `WITH` keyword and used within a SQL query.

### Q2. What does CTE stand for?

**Common Table Expression**

### Q3. Which keyword is used to create a CTE?

`WITH`

### Q4. Can we create multiple CTEs?

Yes.

```sql
WITH cte1 AS (...),
cte2 AS (...)
SELECT ...;
```

### Q5. What is the main advantage of CTE?

CTEs make complex SQL queries **more readable, organized, and easier to maintain**.

### Q6. What is a Recursive CTE?

A Recursive CTE is a CTE that refers to itself and is commonly used for hierarchical data.

### Q7. CTE vs Subquery?

A CTE is defined separately using `WITH`, making complex queries easier to read. A subquery is generally written directly inside another query.

---

# 🎯 Practice Questions

### Q1. Find employees earning more than 60000.

```sql
WITH high_salary AS (
    SELECT name, salary
    FROM employees
    WHERE salary > 60000
)
SELECT *
FROM high_salary;
```

### Q2. Find average salary by department.

```sql
WITH department_avg AS (
    SELECT 
        department,
        AVG(salary) AS avg_salary
    FROM employees
    GROUP BY department
)
SELECT *
FROM department_avg;
```

### Q3. Find departments where average salary is greater than 50000.

```sql
WITH department_avg AS (
    SELECT 
        department,
        AVG(salary) AS avg_salary
    FROM employees
    GROUP BY department
)
SELECT *
FROM department_avg
WHERE avg_salary > 50000;
```

### Q4. Create two CTEs.

```sql
WITH
high_salary AS (
    SELECT *
    FROM employees
    WHERE salary > 60000
),
sales_employees AS (
    SELECT *
    FROM high_salary
    WHERE department = 'Sales'
)
SELECT *
FROM sales_employees;
```

---

#  CTE Quick Revision

| Concept           | Key Point                                              |
| ----------------- | ------------------------------------------------------ |
| CTE               | Temporary named result                                 |
| Keyword           | `WITH`                                                 |
| Definition        | `AS (...)`                                             |
| Multiple CTE      | Separate using comma                                   |
| Recursive CTE     | CTE refers to itself                                   |
| Main benefit      | Readability                                            |
| CTE vs Subquery   | CTE is easier for complex queries                      |
| CTE vs Temp Table | CTE is query-level; temp table can persist for session |

---

#  One-Minute Revision

```text
CTE
 ↓
WITH
 ↓
CTE Name
 ↓
AS (SELECT ...)
 ↓
Main SELECT

Multiple CTE:
WITH cte1 AS (...),
     cte2 AS (...)
SELECT ...

Recursive CTE:
WITH RECURSIVE
     ↓
Anchor Query
     ↓
UNION ALL
     ↓
Recursive Query
```

---


