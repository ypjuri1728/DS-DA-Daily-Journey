# Day 10 - Exception Handling

# 1. Basic try-except

try:
print(10 / 0)
except:
print("Something went wrong")

# 2. ZeroDivisionError

try:
result = 10 / 0
except ZeroDivisionError:
print("Cannot divide by zero")

# 3. ValueError

try:
num = int(input("Enter a number: "))
print(num)
except ValueError:
print("Please enter a valid number")

# 4. TypeError

try:
result = "10" + 5
except TypeError:
print("Cannot add string and integer")

# 5. IndexError

try:
numbers = [10, 20, 30]
print(numbers[5])
except IndexError:
print("Index does not exist")

# 6. KeyError

try:
student = {"name": "Rahul", "age": 20}
print(student["marks"])
except KeyError:
print("Key does not exist")

# 7. Multiple except

try:
num = int(input("Enter number: "))
result = 100 / num
print(result)

except ValueError:
print("Enter a valid number")

except ZeroDivisionError:
print("Cannot divide by zero")

# 8. else

try:
num = 10 / 2

except ZeroDivisionError:
print("Cannot divide by zero")

else:
print("Division successful")

# 9. finally

try:
num = 10 / 2

except ZeroDivisionError:
print("Error")

finally:
print("Program finished")

# 10. try-except-else-finally

try:
num = int(input("Enter number: "))
result = 100 / num

except ValueError:
print("Invalid number")

except ZeroDivisionError:
print("Cannot divide by zero")

else:
print("Result:", result)

finally:
print("Execution completed")

# 11. raise

age = 15

try:
if age < 18:
raise ValueError("Age must be 18 or above")

except ValueError as e:
print(e)

# 12. Practical Example - Login

correct_password = "python123"

try:
password = input("Enter password: ")

```
if password != correct_password:
    raise ValueError("Wrong password")

print("Login successful")
```

except ValueError as e:
print(e)

# 13. Practical Example - Safe Division

try:
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

```
print("Result:", a / b)
```

except ValueError:
print("Enter numbers only")

except ZeroDivisionError:
print("Cannot divide by zero")

# 14. Practice - Positive Number

try:
number = int(input("Enter a positive number: "))

```
if number < 0:
    raise ValueError("Number must be positive")

print("Number:", number)
```

except ValueError as e:
print(e)
