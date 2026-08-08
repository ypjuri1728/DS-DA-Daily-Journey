# Day 02 — Python Loops & Functions

#1. Loops

A loop is used to **repeat a block of code** multiple times.

Python mainly has:

* `for` loop
* `while` loop

---

## 2. `for` Loop

Used when we want to iterate over a sequence or when we know the range of repetition.

### Syntax

```python
for variable in sequence:
    # code
```

### Example

```python
for i in range(1, 6):
    print(i)
```

Output:

```text
1
2
3
4
5
```

### `range()`

```python
range(start, stop, step)
```

Important: **stop is not included.**

```python
range(1, 6)       # 1 2 3 4 5
range(5)          # 0 1 2 3 4
range(1, 10, 2)   # 1 3 5 7 9
```

---

## 3. `while` Loop

Used when we want to repeat code **while a condition is true**.

### Syntax

```python
while condition:
    # code
```

### Example

```python
i = 1

while i <= 5:
    print(i)
    i += 1
```

### Important

In a `while` loop, make sure the condition eventually becomes `False`.

Otherwise, you can create an **infinite loop**.

---

## 4. `break`

`break` immediately stops the loop.

```python
for i in range(1, 10):
    if i == 5:
        break
    print(i)
```

Output:

```text
1
2
3
4
```

---

## 5. `continue`

`continue` skips the **current iteration** and moves to the next iteration.

```python
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
```

Output:

```text
1
2
4
5
```

### `break` vs `continue`

| `break`                   | `continue`                |
| ------------------------- | ------------------------- |
| Stops the entire loop     | Skips current iteration   |
| Loop ends                 | Loop continues            |
| Used when we want to exit | Used when we want to skip |

---

# 6. Functions

A function is a **reusable block of code** designed to perform a particular task.

### Why use functions?

* Avoid repeating code
* Make code organized
* Improve readability
* Make debugging easier
* Reuse the same logic

---

## 7. Creating a Function

Use the `def` keyword.

```python
def function_name():
    # code
```

Example:

```python
def greet():
    print("Hello!")

greet()
```

---

## 8. Parameters and Arguments

A **parameter** is the variable written when defining a function.

An **argument** is the actual value passed when calling it.

```python
def greet(name):       # name = parameter
    print("Hello", name)

greet("Priyanshi")     # "Priyanshi" = argument
```

---

## 9. Multiple Parameters

```python
def add(a, b):
    print(a + b)

add(10, 20)
```

Output:

```text
30
```

---

## 10. `return`

`return` sends a value back from the function.

```python
def add(a, b):
    return a + b

result = add(10, 20)
print(result)
```

Output:

```text
30
```

### `print()` vs `return`

**`print()`** → displays something on the screen.

**`return`** → gives the result back so we can store/use it later.

```python
def add(a, b):
    return a + b

answer = add(5, 10)
print(answer)
```

---

## 11. Function Without vs With Return

### Without `return`

```python
def square(n):
    print(n * n)
```

The function only displays the result.

### With `return`

```python
def square(n):
    return n * n

result = square(5)
print(result)
```

Now the returned value can be stored and used.

---

# 12. Function with Condition

Functions can contain other logic such as `if/else`.

```python
def check_even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(check_even_odd(10))
```

Output:

```text
Even
```

---

# 13. Important Concepts to Remember

```text
for       → repeat over a sequence/range
while     → repeat while condition is true
break     → completely stop loop
continue  → skip current iteration
def       → create a function
parameter → variable in function definition
argument  → actual value passed to function
return    → send value back from function
```

---

## Key Takeaway

> **Loops help us repeat logic. Functions help us reuse logic.**
