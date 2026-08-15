
---

## 💻 Section 2 — `code.py`

```python
# ==========================================
# DAY 09 — FILE HANDLING
# ==========================================


# ------------------------------------------
# 1. OPENING AND READING A FILE
# ------------------------------------------

file = open("data.txt", "r")

data = file.read()

print(data)

file.close()


# ------------------------------------------
# 2. READLINE()
# ------------------------------------------

file = open("data.txt", "r")

print(file.readline())
print(file.readline())

file.close()


# ------------------------------------------
# 3. READLINES()
# ------------------------------------------

file = open("data.txt", "r")

lines = file.readlines()

print(lines)

file.close()


# ------------------------------------------
# 4. WRITING TO A FILE
# ------------------------------------------

file = open("data.txt", "w")

file.write("Hello Python")

file.close()


# ------------------------------------------
# 5. WRITING MULTIPLE LINES
# ------------------------------------------

file = open("data.txt", "w")

file.write("Python\n")
file.write("Java\n")
file.write("SQL\n")

file.close()


# ------------------------------------------
# 6. APPENDING TO A FILE
# ------------------------------------------

file = open("data.txt", "a")

file.write("Data Science\n")

file.close()


# ------------------------------------------
# 7. USING with open()
# ------------------------------------------

with open("data.txt", "r") as file:
    data = file.read()
    print(data)


# ------------------------------------------
# 8. READING LINE BY LINE
# ------------------------------------------

with open("data.txt", "r") as file:

    for line in file:
        print(line)


# ------------------------------------------
# 9. SIMPLE FILE PROGRAM
# ------------------------------------------

with open("data.txt", "w") as file:

    file.write("Priyanshi\n")
    file.write("Python\n")
    file.write("Data Science\n")


with open("data.txt", "r") as file:

    data = file.read()

    print("\nFile Data:")
    print(data)


# ------------------------------------------
# 10. COUNT NUMBER OF LINES
# ------------------------------------------

with open("data.txt", "r") as file:

    lines = file.readlines()

    print("Number of lines:", len(lines))
