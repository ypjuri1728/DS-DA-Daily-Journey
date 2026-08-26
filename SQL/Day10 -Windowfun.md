# Day 10 —  Window Functions

##  What are Window Functions?

Window Functions perform calculations across a set of related rows **without combining or removing rows**.

They are mainly used for:

* Ranking
* Running totals
* Comparing current and previous rows
* Finding highest/lowest values
* Calculating averages
* Data analysis

### Basic Syntax

```sql
SELECT
    column1,
    column2,
    function_name() OVER (
        PARTITION BY column
        ORDER BY column
    ) AS result
FROM table_name;
```

---

# 1. OVER()

`OVER()` tells SQL that we are using a Window Function.

```sql
SELECT
    name,
    salary,
    AVG(salary) OVER () AS avg_salary
FROM employees;
```

Every row is kept, and the average salary is shown for every employee.

---

# 2. PARTITION BY

`PARTITION BY` divides rows into groups without combining them.

```sql
SELECT
    name,
    department,
    salary,
    AVG(salary) OVER (
        PARTITION BY department
    ) AS department_avg
FROM employees;
```

Each department gets its own average salary.

### Example

```text
department = IT
    ↓
Calculate IT average

department = HR
    ↓
Calculate HR average
```

---

# 3. ORDER BY in Window Functions

`ORDER BY` decides the order in which the window calculation is performed.

```sql
SELECT
    name,
    salary,
    ROW_NUMBER() OVER (
        ORDER BY salary DESC
    ) AS row_num
FROM employees;
```

---

# 4. ROW_NUMBER()

Assigns a unique number to every row.

```sql
SELECT
    name,
    salary,
    ROW_NUMBER() OVER (
        ORDER BY salary DESC
    ) AS row_num
FROM employees;
```

Example:

| Name | Salary | Row Number |
| ---- | -----: | ---------: |
| A    |  80000 |          1 |
| B    |  70000 |          2 |
| C    |  70000 |          3 |
| D    |  60000 |          4 |

Even if salaries are equal, `ROW_NUMBER()` gives different numbers.

---

# 5. RANK()

Assigns the same rank to equal values.

```sql
SELECT
    name,
    salary,
    RANK() OVER (
        ORDER BY salary DESC
    ) AS salary_rank
FROM employees;
```

Example:

| Salary | Rank |
| -----: | ---: |
|  80000 |    1 |
|  70000 |    2 |
|  70000 |    2 |
|  60000 |    4 |

### Important

`RANK()` **skips the next rank** after a tie.

---

# 6. DENSE_RANK()

Similar to `RANK()`, but does not skip ranks.

```sql
SELECT
    name,
    salary,
    DENSE_RANK() OVER (
        ORDER BY salary DESC
    ) AS salary_rank
FROM employees;
```

Example:

| Salary | Dense Rank |
| -----: | ---------: |
|  80000 |          1 |
|  70000 |          2 |
|  70000 |          2 |
|  60000 |          3 |

---

#  ROW_NUMBER vs RANK vs DENSE_RANK

| Function       | Duplicate Values | Gap After Tie |
| -------------- | ---------------- | ------------- |
| `ROW_NUMBER()` | Different number | No            |
| `RANK()`       | Same rank        | Yes           |
| `DENSE_RANK()` | Same rank        | No            |

### Easy Trick

```text
ROW_NUMBER → Always unique

RANK       → Tie + gap

DENSE_RANK → Tie + no gap
```

---

# 7. Window Function with PARTITION BY

Find employee ranking within each department.

```sql
SELECT
    name,
    department,
    salary,
    RANK() OVER (
        PARTITION BY department
        ORDER BY salary DESC
    ) AS department_rank
FROM employees;
```

Each department starts ranking from `1`.

---

# 8. SUM() with Window Function

Window functions can calculate a running total.

```sql
SELECT
    id,
    amount,
    SUM(amount) OVER (
        ORDER BY id
    ) AS running_total
FROM sales;
```

Example:

| Amount | Running Total |
| -----: | ------------: |
|    100 |           100 |
|    200 |           300 |
|    150 |           450 |
|     50 |           500 |

### Running Total

```text
100
100 + 200 = 300
300 + 150 = 450
450 + 50 = 500
```

---

# 9. SUM() with PARTITION BY

Calculate total sales for each category while keeping every row.

```sql
SELECT
    product,
    category,
    amount,
    SUM(amount) OVER (
        PARTITION BY category
    ) AS category_total
FROM sales;
```

---

# 10. AVG() Window Function

Calculate the average without removing individual rows.

```sql
SELECT
    name,
    department,
    salary,
    AVG(salary) OVER (
        PARTITION BY department
    ) AS department_avg
FROM employees;
```

---

# 11. COUNT() Window Function

Count rows within each group.

```sql
SELECT
    name,
    department,
    COUNT(*) OVER (
        PARTITION BY department
    ) AS employee_count
FROM employees;
```

Every employee row will show the number of employees in their department.

---

# 12. MIN() and MAX()

```sql
SELECT
    name,
    salary,
    MIN(salary) OVER () AS minimum_salary,
    MAX(salary) OVER () AS maximum_salary
FROM employees;
```

Every row will contain the overall minimum and maximum salary.

---

# 13. LAG()

`LAG()` gets a value from a **previous row**.

```sql
SELECT
    month,
    sales,
    LAG(sales) OVER (
        ORDER BY month
    ) AS previous_sales
FROM sales;
```

Example:

| Month | Sales | Previous Sales |
| ----- | ----: | -------------: |
| Jan   |   100 |           NULL |
| Feb   |   150 |            100 |
| Mar   |   200 |            150 |

### Easy Trick

```text
LAG → Look backward
```

---

# 14. LEAD()

`LEAD()` gets a value from the **next row**.

```sql
SELECT
    month,
    sales,
    LEAD(sales) OVER (
        ORDER BY month
    ) AS next_sales
FROM sales;
```

Example:

| Month | Sales | Next Sales |
| ----- | ----: | ---------: |
| Jan   |   100 |        150 |
| Feb   |   150 |        200 |
| Mar   |   200 |       NULL |

### Easy Trick

```text
LEAD → Look forward
```

---

#  LAG vs LEAD

| Function | Gets         |
| -------- | ------------ |
| `LAG()`  | Previous row |
| `LEAD()` | Next row     |

---

# 15. Compare Current and Previous Row

One common use of `LAG()` is calculating the difference.

```sql
SELECT
    month,
    sales,
    sales - LAG(sales) OVER (
        ORDER BY month
    ) AS sales_difference
FROM sales;
```

Example:

| Month | Sales | Difference |
| ----- | ----: | ---------: |
| Jan   |   100 |       NULL |
| Feb   |   150 |         50 |
| Mar   |   200 |         50 |

---

# 16. FIRST_VALUE()

Returns the first value in the window.

```sql
SELECT
    name,
    salary,
    FIRST_VALUE(salary) OVER (
        ORDER BY salary DESC
    ) AS highest_salary
FROM employees;
```

---

# 17. LAST_VALUE()

Returns the last value according to the window frame.

```sql
SELECT
    name,
    salary,
    LAST_VALUE(salary) OVER (
        ORDER BY salary
        ROWS BETWEEN UNBOUNDED PRECEDING
        AND UNBOUNDED FOLLOWING
    ) AS lowest_salary
FROM employees;
```

### Important

`LAST_VALUE()` can require an explicit window frame to get the expected result.

---

# 18. Find Highest Salary in Each Department

Use `RANK()` with `PARTITION BY`.

```sql
SELECT *
FROM (
    SELECT
        name,
        department,
        salary,
        RANK() OVER (
            PARTITION BY department
            ORDER BY salary DESC
        ) AS rnk
    FROM employees
) AS temp
WHERE rnk = 1;
```

---

# 19. Find Second Highest Salary

Using `DENSE_RANK()`:

```sql
SELECT *
FROM (
    SELECT
        name,
        salary,
        DENSE_RANK() OVER (
            ORDER BY salary DESC
        ) AS rnk
    FROM employees
) AS temp
WHERE rnk = 2;
```

This returns the **second highest distinct salary**.

---

# 20. Window Functions vs GROUP BY

| GROUP BY                      | Window Functions                     |
| ----------------------------- | ------------------------------------ |
| Groups rows                   | Calculates across rows               |
| Reduces number of rows        | Keeps all rows                       |
| Used with aggregate functions | Uses aggregate and ranking functions |
| Good for summary results      | Good for detailed analysis           |

### GROUP BY

```sql
SELECT
    department,
    AVG(salary) AS avg_salary
FROM employees
GROUP BY department;
```

Result contains one row per department.

### Window Function

```sql
SELECT
    name,
    department,
    salary,
    AVG(salary) OVER (
        PARTITION BY department
    ) AS avg_salary
FROM employees;
```

All employee rows remain.

---

# 21. Window Functions vs CTE

A CTE and Window Function solve different problems.

### CTE

Used to create a temporary named result that can make a complex query easier to organize.

```sql
WITH high_salary AS (
    SELECT *
    FROM employees
    WHERE salary > 50000
)
SELECT *
FROM high_salary;
```

### Window Function

Used to perform calculations across related rows.

```sql
SELECT
    name,
    salary,
    RANK() OVER (
        ORDER BY salary DESC
    ) AS rnk
FROM employees;
```

### They can also be used together

```sql
WITH employee_data AS (
    SELECT *
    FROM employees
)
SELECT
    name,
    salary,
    RANK() OVER (
        ORDER BY salary DESC
    ) AS rnk
FROM employee_data;
```

---

#  Important Window Functions

| Function        | Purpose               |
| --------------- | --------------------- |
| `ROW_NUMBER()`  | Unique row number     |
| `RANK()`        | Ranking with gaps     |
| `DENSE_RANK()`  | Ranking without gaps  |
| `SUM()`         | Total / running total |
| `AVG()`         | Average               |
| `COUNT()`       | Count                 |
| `MIN()`         | Minimum               |
| `MAX()`         | Maximum               |
| `LAG()`         | Previous row          |
| `LEAD()`        | Next row              |
| `FIRST_VALUE()` | First value           |
| `LAST_VALUE()`  | Last value            |

---

# Quick Revision Tricks

```text
OVER()
→ Makes the function a Window Function

PARTITION BY
→ Divide rows into groups

ORDER BY
→ Decide the order

ROW_NUMBER()
→ Unique numbers

RANK()
→ Same rank + gap

DENSE_RANK()
→ Same rank + no gap

LAG()
→ Previous

LEAD()
→ Next

SUM() OVER()
→ Running/Window total
```

---

#  Interview Questions

### 1. What is a Window Function?

A Window Function performs calculations across related rows without reducing the number of rows.

### 2. What is `OVER()`?

`OVER()` defines the window on which the Window Function operates.

### 3. What is `PARTITION BY`?

It divides rows into groups for the Window Function while keeping individual rows.

### 4. Difference between `RANK()` and `DENSE_RANK()`?

`RANK()` leaves gaps after ties, while `DENSE_RANK()` does not.

### 5. Difference between `ROW_NUMBER()` and `RANK()`?

`ROW_NUMBER()` gives every row a unique number, while `RANK()` gives equal values the same rank.

### 6. What does `LAG()` do?

It returns a value from a previous row.

### 7. What does `LEAD()` do?

It returns a value from a following row.

### 8. Can aggregate functions be used as Window Functions?

Yes.

Examples:

```sql
SUM() OVER()
AVG() OVER()
COUNT() OVER()
MIN() OVER()
MAX() OVER()
```

---

