# Day 7 – Sets Practice

# 1. Create a Set

numbers = {10, 20, 30, 40}

print(numbers)

# 2. Duplicate values

numbers = {10, 20, 20, 30, 30, 40}

print(numbers)

# 3. Add an element

numbers.add(50)

print(numbers)

# 4. Add multiple elements

numbers.update([60, 70])

print(numbers)

# 5. Remove an element

numbers.remove(20)

print(numbers)

# 6. Check an element

print(30 in numbers)
print(100 in numbers)

# 7. Loop through Set

for num in numbers:
print(num)

# 8. Union

a = {1, 2, 3}
b = {3, 4, 5}

print("Union:", a.union(b))

# 9. Intersection

a = {1, 2, 3}
b = {2, 3, 4}

print("Intersection:", a.intersection(b))

# 10. Difference

a = {1, 2, 3}
b = {2, 3, 4}

print("Difference:", a.difference(b))

# 11. Find unique values

numbers = [10, 20, 20, 30, 30, 40, 40]

unique_numbers = set(numbers)

print("Unique values:", unique_numbers)

