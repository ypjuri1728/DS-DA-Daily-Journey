# Day 5 – Lists Practice

# 1. Create a list

numbers = [10, 20, 30, 40, 50]

print(numbers)

# 2. Access elements

print(numbers[0])
print(numbers[2])
print(numbers[-1])

# 3. Change an element

numbers[1] = 25

print(numbers)

# 4. Add element using append()

numbers.append(60)

print(numbers)

# 5. Add element using insert()

numbers.insert(1, 15)

print(numbers)

# 6. Remove a value

numbers.remove(30)

print(numbers)

# 7. Remove using pop()

numbers.pop(2)

print(numbers)

# 8. Find length

print("Length:", len(numbers))

# 9. Check whether element exists

print(50 in numbers)
print(100 in numbers)

# 10. Loop through list

for num in numbers:
print(num)

# 11. Find sum

numbers = [10, 20, 30, 40, 50]

total = 0

for num in numbers:
total = total + num

print("Sum:", total)

# 12. Find maximum

maximum = numbers[0]

for num in numbers:
if num > maximum:
maximum = num

print("Maximum:", maximum)

# 13. Find minimum

minimum = numbers[0]

for num in numbers:
if num < minimum:
minimum = num

print("Minimum:", minimum)

