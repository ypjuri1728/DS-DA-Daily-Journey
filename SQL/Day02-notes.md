# Day 02 – SQL Notes: WHERE Clause & Operators
---
##1. What is WHERE?

WHERE is used to filter records — 
it picks only the rows that satisfy a given condition. Without WHERE, a query returns all rows from the table.

* Syntax:

sql
SELECT column1, column2
FROM table_name
WHERE condition;

Example:

sql
SELECT * FROM employees
WHERE department = 'Sales';

This returns only the employees who work in the Sales department.

```Note: WHERE comes after FROM and before GROUP BY, ORDER BY.```
---
##2. Comparison Operators

Used to compare a column's value with a given value.

Operator	Meaning	Example
=	Equal to	WHERE age = 25
!= or <>	Not equal to	WHERE age != 25
>	Greater than	WHERE salary > 50000
<	Less than	WHERE salary < 50000
>=	Greater than or equal to	WHERE age >= 18
<=	Less than or equal to	WHERE age <= 60

---
## 3. Logical Operators

Used to combine multiple conditions in WHERE.

### AND

All conditions must be true.

sql
SELECT * FROM employees
WHERE department = 'Sales' AND salary > 40000;

### OR

At least one condition must be true.

sql
SELECT * FROM employees
WHERE department = 'Sales' OR department = 'Marketing';
NOT

Reverses the condition (excludes matching rows).

sql
SELECT * FROM employees
WHERE NOT department = 'Sales';

You can combine AND / OR together, use () to control priority:

sql
SELECT * FROM employees
WHERE (department = 'Sales' OR department = 'Marketing')
AND salary > 40000;
---
## 4. Special Operators (used with WHERE)
BETWEEN

Selects values within a range (inclusive of both ends).

sql
SELECT * FROM employees
WHERE salary BETWEEN 30000 AND 60000;
IN

=>Checks if a value matches any value in a list — shortcut for multiple OR conditions.

sql
SELECT * FROM employees
WHERE department IN ('Sales', 'HR', 'IT');

Same as:

sql
WHERE department = 'Sales' OR department = 'HR' OR department = 'IT';
NOT IN

Opposite of IN — excludes listed values.

sql
SELECT * FROM employees
WHERE department NOT IN ('Sales', 'HR');
LIKE

Used for pattern matching with text (uses wildcards).

% → matches zero or more characters
_ → matches exactly one character
sql
SELECT * FROM employees
WHERE name LIKE 'A%';      -- names starting with A
sql
SELECT * FROM employees
WHERE name LIKE '%a';      -- names ending with a
sql
SELECT * FROM employees
WHERE name LIKE '%an%';    -- names containing 'an'
sql
SELECT * FROM employees
WHERE name LIKE '_avi';    -- 4 letter name ending with 'avi' (e.g. Ravi)
NOT LIKE

Excludes matching pattern.

sql
SELECT * FROM employees
WHERE name NOT LIKE 'A%';
IS NULL / IS NOT NULL

Used to check for NULL (empty/unknown) values. Note: you cannot use = NULL, always use IS NULL.

sql
SELECT * FROM employees
WHERE manager_id IS NULL;
sql
SELECT * FROM employees
WHERE manager_id IS NOT NULL;
---
5. Order of Precedence (important!)

When combining operators, SQL evaluates in this order (higher to lower):

() Parentheses
Comparison operators (=, >, <, etc.)
BETWEEN, IN, LIKE, IS NULL
NOT
AND
OR

Tip: Always use () when mixing AND/OR to avoid confusion and wrong results.
---
6. Quick Practice Examples
sql
-- Employees in IT dept with salary above 50000
SELECT * FROM employees
WHERE department = 'IT' AND salary > 50000;

-- Employees whose name starts with 'S' and age between 25-35
SELECT * FROM employees
WHERE name LIKE 'S%' AND age BETWEEN 25 AND 35;

-- Employees NOT in Sales or HR, with no manager assigned
SELECT * FROM employees
WHERE department NOT IN ('Sales', 'HR') AND manager_id IS NULL;
---
7. Summary
WHERE = filters rows based on condition(s).
Comparison operators → =, !=, >, <, >=, <=
Logical operators → AND, OR, NOT
Special operators → BETWEEN, IN, LIKE, IS NULL
Use () to control order when combining multiple conditions.
NULL values need IS NULL / IS NOT NULL, never =.
