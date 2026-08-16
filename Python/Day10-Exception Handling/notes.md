#  Day 10 — Exception Handling

##  What is Exception Handling?

**Exception Handling** is used to handle errors during program execution without stopping the entire program.

Example:

```python
a = 10
b = 0

print(a / b)
```

This gives:

```text
ZeroDivisionError
```

We can handle it using `try-except`.

---

## 1. `try`

The code that may cause an error is written inside `try`.

```python
try:
    x = 10 / 0
```

---

## 2. `except`

`except` handles the error.

```python
try:
    x = 10 / 0
except:
    print("Something went wrong")
```

Output:

```text
Something went wrong
```

---

## 3. Specific Exception

It is better to specify the type of error.

```python
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
```

---

## 4. Common Exceptions

| Exception           | Meaning                     |
| ------------------- | --------------------------- |
| `ZeroDivisionError` | Division by zero            |
| `ValueError`        | Invalid value               |
| `TypeError`         | Wrong data type             |
| `IndexError`        | Invalid list index          |
| `KeyError`          | Key not found in dictionary |
| `FileNotFoundError` | File does not exist         |

---

## 5. Multiple `except`

We can handle different errors separately.

```python
try:
    num = int(input("Enter number: "))
    result = 10 / num

except ValueError:
    print("Enter a valid number")

except ZeroDivisionError:
    print("Cannot divide by zero")
```

---

## 6. `else`

`else` runs when **no exception occurs**.

```python
try:
    x = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("Division successful")
```

Output:

```text
Division successful
```

---

## 7. `finally`

`finally` always executes, whether an error occurs or not.

```python
try:
    x = 10 / 2
except:
    print("Error")
finally:
    print("Program finished")
```

Output:

```text
Program finished
```

---

## 8. `raise`

`raise` is used to manually create an exception.

```python
age = 15

if age < 18:
    raise ValueError("Age must be 18 or above")
```

---

## 9. `try-except-else-finally`

All four can be used together.

```python
try:
    x = 10 / 2

except ZeroDivisionError:
    print("Cannot divide by zero")

else:
    print("Success")

finally:
    print("Done")
```

---

## 10. `print()` vs Exception Handling

Without exception handling:

```python
num = int(input("Enter number: "))
```

If the user enters:

```text
abc
```

Program crashes with `ValueError`.

With exception handling:

```python
try:
    num = int(input("Enter number: "))
except ValueError:
    print("Invalid input")
```

Program continues safely.

---

##  Important Syntax

```python
try:
    # risky code

except ExceptionType:
    # handle error

else:
    # runs if no error

finally:
    # always runs
```

---

##  Key Points

* `try` → contains risky code
* `except` → handles the error
* `else` → runs when there is no error
* `finally` → always runs
* `raise` → manually raises an exception
* Prefer **specific exceptions** instead of a general `except`
