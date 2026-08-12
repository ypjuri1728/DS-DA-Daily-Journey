# Day 6 – Tuple Practice

# 1. Create a tuple

numbers = (10, 20, 30, 40, 50)

print(numbers)

# 2. Access elements

print(numbers[0])
print(numbers[2])
print(numbers[-1])

# 3. Find length

print("Length:", len(numbers))

# 4. Loop through tuple

for num in numbers:
print(num)

# 5. Check element

print(30 in numbers)
print(100 in numbers)

# 6. Count an element

values = (10, 20, 20, 30, 20, 40)

print("Count:", values.count(20))

# 7. Find index

print("Index:", values.index(30))

# 8. Tuple with different data types

data = (10, "Python", 3.5, True)

print(data)

# 9. Find sum

numbers = (10, 20, 30, 40)

total = 0

for num in numbers:
total = total + num

print("Sum:", total)

# 10. Find maximum

numbers = (10, 50, 20, 40, 30)

maximum = numbers[0]

for num in numbers:
if num > maximum:
maximum = num

print("Maximum:", maximum)

