# Day 4 – Functions Practice

# 1. Simple Function

def greet():
print("Hello, Python!")

greet()

# 2. Function with Parameter

def greet_user(name):
print("Hello", name)

greet_user("Priyanshi")

# 3. Function with Two Parameters

def add(a, b):
print(a + b)

add(10, 20)

# 4. Function with Return

def multiply(a, b):
return a * b

result = multiply(5, 4)
print("Multiplication:", result)

# 5. Even or Odd

def check_even_odd(num):
if num % 2 == 0:
return "Even"
else:
return "Odd"

print(check_even_odd(10))
print(check_even_odd(7))

# 6. Find Maximum of Two Numbers

def find_max(a, b):
if a > b:
return a
else:
return b

print("Maximum:", find_max(15, 25))

# 7. Default Parameter

def welcome(name="User"):
print("Welcome", name)

welcome()
welcome("Priyanshi")

# 8. Square of a Number

def square(num):
return num * num

print("Square:", square(6))

# 9. Check Positive / Negative

def check_number(num):
if num > 0:
return "Positive"
elif num < 0:
return "Negative"
else:
return "Zero"

print(check_number(10))
print(check_number(-5))
print(check_number(0))

