# Day 4 – Python Functions

## 1. What is a Function?

A function is a reusable block of code that performs a specific task.

We use functions to:

* Avoid repeating code
* Make code easier to understand
* Organize a program
* Reuse the same logic multiple times

---

## 2. Creating a Function

Syntax:

```python
def function_name():
    # code
```

Example:

```python
def greet():
    print("Hello")
```

---

## 3. Calling a Function

Creating a function does not execute it.

We need to call it:

```python
greet()
```

Output:

```text
Hello
```

---

## 4. Function with Parameters

Parameters are values received by a function.

```python
def greet(name):
    print("Hello", name)

greet("Priyanshi")
```

Output:

```text
Hello Priyanshi
```

---

## 5. Multiple Parameters

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

## 6. `return`

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

---

## 7. `print()` vs `return`

### print()

Displays the result.

```python
def add(a, b):
    print(a + b)
```

### return

Sends the result back so we can store/use it.

```python
def add(a, b):
    return a + b

x = add(10, 20)
```

**Remember:**

`print()` → shows the result
`return` → gives the result back

---

## 8. Default Parameter

A parameter can have a default value.

```python
def greet(name="User"):
    print("Hello", name)

greet()
greet("Priyanshi")
```

Output:

```text
Hello User
Hello Priyanshi
```

---

## 9. Local Variable

A variable created inside a function normally works only inside that function.

```python
def test():
    x = 10
    print(x)

test()
```

---

## 10. Global Variable

A variable created outside a function is global.

```python
x = 10

def test():
    print(x)

test()
```

---

## 11. Function with Return + Condition

```python
def check_even(num):
    if num % 2 == 0:
        return True
    return False

print(check_even(10))
```

Output:

```text
True
```

---

## Important Points

* `def` is used to create a function.
* A function runs when we call it.
* Parameters receive values.
* Arguments are the actual values passed to a function.
* `return` sends a value back.
* `print()` only displays a value.
* Functions help us reuse code.
* Default parameters have a predefined value.

## Basic Syntax

```python
def function_name(parameters):
    # code
    return value
```
