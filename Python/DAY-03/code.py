# Day 03 — Python Collections

# code.py

# =========================

# 1. LIST
# =========================

numbers = [10, 20, 30, 40, 50]

print("List:", numbers)
print("First element:", numbers[0])
print("Last element:", numbers[-1])

numbers[1] = 25
print("After update:", numbers)

numbers.append(60)
numbers.insert(1, 15)
numbers.extend([70, 80])

print("After adding:", numbers)

numbers.remove(25)
numbers.pop()

print("After removing:", numbers)

print("Slicing:", numbers[1:4])
print("Length:", len(numbers))

numbers.sort()
print("Sorted:", numbers)

numbers.reverse()
print("Reversed:", numbers)

# =========================

# 2. LIST METHODS

# =========================

marks = [80, 90, 75, 90, 85]

print("\nMarks:", marks)
print("Highest:", max(marks))
print("Lowest:", min(marks))
print("Total:", sum(marks))
print("Count of 90:", marks.count(90))
print("Index of 75:", marks.index(75))

# =========================

# 3. TUPLE

# =========================

student = ("Priyanshi", 21, "Data Science")

print("\nTuple:", student)
print("Name:", student[0])
print("Age:", student[1])
print("Course:", student[2])

numbers_tuple = (10, 20, 20, 30, 40, 20)

print("Count of 20:", numbers_tuple.count(20))
print("Index of 30:", numbers_tuple.index(30))

# =========================

# 4. SET

# =========================

numbers_set = {10, 20, 30, 20, 10, 40}

print("\nSet:", numbers_set)

numbers_set.add(50)
print("After add:", numbers_set)

numbers_set.discard(100)
print("After discard:", numbers_set)

# =========================

# 5. SET OPERATIONS

# =========================

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("\nA:", A)
print("B:", B)

print("Union:", A | B)
print("Intersection:", A & B)
print("Difference:", A - B)
print("Symmetric Difference:", A ^ B)

# =========================

# 6. DICTIONARY

# =========================

student = {
"name": "Priyanshi",
"age": 21,
"course": "Data Science",
"marks": 90
}

print("\nDictionary:", student)

print("Name:", student["name"])
print("Marks:", student.get("marks"))

student["city"] = "Surat"
student["marks"] = 95

print("Updated dictionary:", student)

print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

# =========================

# 7. DICTIONARY LOOP

# =========================

print("\nDictionary Loop:")

for key, value in student.items():
print(key, ":", value)

# =========================

# 8. LIST LOOP

# =========================

print("\nList Loop:")

fruits = ["Apple", "Mango", "Banana", "Orange"]

for fruit in fruits:
print(fruit)

# =========================

# 9. REMOVE DUPLICATES

# =========================

numbers = [1, 2, 2, 3, 4, 4, 5, 5]

unique_numbers = list(set(numbers))

print("\nOriginal:", numbers)
print("Without duplicates:", unique_numbers)

# =========================

# 10. NESTED LIST

# =========================

matrix = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]

print("\nMatrix:")
print(matrix)

print("Element:", matrix[1][2])

# =========================

# 11. LIST OF DICTIONARIES

# =========================

students = [
{"name": "Priyanshi", "marks": 90},
{"name": "Rahul", "marks": 85},
{"name": "Aman", "marks": 78}
]

print("\nStudents:")

for student in students:
print(student["name"], "->", student["marks"])

# =========================

# 12. PRACTICE

# =========================

# Q1. Find largest number

numbers = [10, 45, 23, 67, 12, 89]

print("\nLargest:", max(numbers))

# Q2. Find smallest number

print("Smallest:", min(numbers))

# Q3. Find sum

print("Sum:", sum(numbers))

# Q4. Count even numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

even_count = 0

for num in numbers:
if num % 2 == 0:
even_count += 1

print("Even count:", even_count)

# Q5. Remove duplicates

numbers = [1, 2, 2, 3, 4, 4, 5]

unique = list(set(numbers))

print("Unique:", unique)

# Q6. Find common elements

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

common = set(list1) & set(list2)

print("Common elements:", common)

# Q7. Dictionary

student = {
"name": "Priyanshi",
"age": 21,
"marks": 90
}

print("Student:", student)

# Q8. Student with highest marks

students = {
"Priyanshi": 90,
"Rahul": 85,
"Aman": 95
}

top_student = max(students, key=students.get)

print("Top student:", top_student)
print("Marks:", students[top_student])
