# Day 09 — File Handling in Python

## 1. What is File Handling?

File handling means **creating, reading, writing, and modifying files using Python**.

Python can work with files like:
- `.txt`
- `.csv`
- `.json`
- `.log`

---

## 2. Opening a File

Python uses the `open()` function to open a file.

```python
open("filename.txt", "mode")
file = open("data.txt", "r")

3. File Modes
Mode	Meaning
r	Read
w	Write
a	Append
x	Create a new file
r — Read

Used to read existing data.

file = open("data.txt", "r")
w — Write

Used to write data.

⚠️ It replaces existing content.

file = open("data.txt", "w")
a — Append

Adds new data at the end.

file = open("data.txt", "a")
4. Reading a File
read()

Reads the complete file.

file = open("data.txt", "r")


data = file.read()


print(data)


file.close()
readline()

Reads one line at a time.

file = open("data.txt", "r")


print(file.readline())
print(file.readline())


file.close()
readlines()

Reads all lines and returns them as a list.

file = open("data.txt", "r")


data = file.readlines()


print(data)


file.close()
5. Writing to a File

Use w mode.

file = open("data.txt", "w")


file.write("Hello Python")


file.close()

⚠️ w mode removes the old content and writes new content.

6. Appending to a File

Use a mode.

file = open("data.txt", "a")


file.write("\nLearning Python")


file.close()

a adds data without removing the existing content.

7. Using with open()

The recommended way to work with files is:

with open("data.txt", "r") as file:
    data = file.read()
    print(data)

Python automatically closes the file.

So we don't need:

file.close()
8. Writing Multiple Lines
with open("data.txt", "w") as file:
    file.write("Python\n")
    file.write("Java\n")
    file.write("SQL\n")

9. Reading Using a Loop
with open("data.txt", "r") as file:
    for line in file:
        print(line)

This is useful when a file contains many lines.

10. File Path

If the file is in the same folder:

open("data.txt", "r")

If the file is inside another folder:

open("data/data.txt", "r")
11. Important Difference
read()

Returns the complete content.

data = file.read()
readline()

Returns one line.

line = file.readline()
readlines()

Returns all lines as a list.

lines = file.readlines()
12. Important Points
open() is used to open a file.
r means read.
w means write and replaces old content.
a means append.
read() reads the complete file.
readline() reads one line.
readlines() returns all lines as a list.
write() writes data into a file.
with open() automatically closes the file.
Always use with open() when possible.
13. Basic Syntax
with open("filename.txt", "mode") as file:
    # file operation

Example:

with open("data.txt", "r") as file:
    print(file.read())
Quick Revision
open()      → Open file
r           → Read
w           → Write / Replace
a           → Append
read()      → Read everything
readline()  → Read one line
readlines() → Read all lines as list
write()     → Write data
with open() → Automatically closes file
