# Python — Loops & Functions

## Loops

Loop = used to execute the same block of code repeatedly.

### 1. for loop

Used when we want to iterate over a sequence or a known range.

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

### range()

```python
range(start, stop, step)
```

* `start` → starting value
* `stop` → ending limit, **not included**
* `step` → how much to increase/decrease

```python
range(5)        # 0 1 2 3 4
range(1, 6)     # 1 2 3 4 5
range(1, 10, 2) # 1 3 5 7 9
```

---

### 2. while loop

Runs as long as the condition is `True`.

```python
i = 1

while i <= 5:
    print(i)
    i += 1
```

⚠️ Always update the variable in a `while` loop when necessary, otherwise it can become an infinite loop.

---

### 3. break

Stops the entire loop.

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

### 4. continue

Skips the current iteration and continues with the next one.

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

### break vs continue

`break` → completely exits the loop

`continue` → skips only the current iteration

---

# Functions

Function = reusable block of code used to perform a specific task.

### Why functions?

* Reuse code
* Avoid repetition
* Make code easier to understand
* Make large programs easier to manage

### Creating a function

```python
def function_name():
    # code
```

Example:

```python
def greet():
    print("Hello")

greet()
```

---

### Parameters and Arguments

```python
def greet(name):
    print("Hello", name)

greet("Priyanshi")
```

`name` → parameter

`"Priyanshi"` → argument

---

### Multiple parameters

```python
def add(a, b):
    return a + b

print(add(10, 20))
```

---

### return

`return` sends a value back from the function.

```python
def square(n):
    return n * n

ans = square(5)
print(ans)
```

Output:

```text
25
```

### print vs return

`print()` → displays the value

`return` → sends the value back so it can be stored or used elsewhere

```python
def add(a, b):
    return a + b

result = add(5, 10)
```

Here `result` stores the returned value.

---

### Function with condition

```python
def check_even(n):
    if n % 2 == 0:
        return True
    return False
```

---

## Important Syntax to Remember

```text
for       → repeat over a sequence/range
while     → repeat while condition is True
break     → stop loop
continue  → skip current iteration

def       → create function
parameter → variable in function definition
argument  → value passed to function
return    → send value back
```

## Practice

* Print numbers from 1 to 100
* Print even numbers from 1 to 50
* Find sum from 1 to n
* Print multiplication table
* Find factorial
* Check prime number
* Function to find maximum of two numbers
* Function to check even/odd
