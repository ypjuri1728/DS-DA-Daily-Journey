# Day 09 — File Handling in Python

## 1. What is File Handling?

File Handling means **creating, reading, writing, and modifying files using Python**.

Python can work with different types of files:

- `.txt`
- `.csv`
- `.json`
- `.log`

---

## 2. Opening a File

Python uses the `open()` function to open a file.

### Syntax

    open("filename", "mode")

### Example

    file = open("data.txt", "r")

---

## 3. File Modes

| Mode | Meaning |
|------|---------|
| `r` | Read the file |
| `w` | Write to the file |
| `a` | Append data to the file |
| `x` | Create a new file |

### `r` — Read

Used to read an existing file.

    file = open("data.txt", "r")

### `w` — Write

Used to write data into a file.

-->>> Existing content will be replaced.

    file = open("data.txt", "w")

### `a` — Append

Adds new data at the end of the file.

    file = open("data.txt", "a")

### `x` — Create

Creates a new file.

    file = open("newfile.txt", "x")

---

## 5. Reading a File

### `read()`

Reads the complete file.

    with open("data.txt", "r") as file:
        data = file.read()
        print(data)

### `readline()`

Reads one line at a time.

    with open("data.txt", "r") as file:
        print(file.readline())
        print(file.readline())

### `readlines()`

Reads all lines and returns them as a list.

    with open("data.txt", "r") as file:
        lines = file.readlines()
        print(lines)

---

## 6. Writing to a File

Use `write()` with `w` mode.

    with open("data.txt", "w") as file:
        file.write("Hello Python")

-->> `w` mode removes the old content before writing.

---

## 6. Appending to a File

Use `a` mode to add content without deleting existing content.

    with open("data.txt", "a") as file:
        file.write("\nLearning Python")

---

## 7. Writing Multiple Lines

Use `\n` to create a new line.

    with open("data.txt", "w") as file:
        file.write("Python\n")
        file.write("Java\n")
        file.write("SQL\n")

---

## 8. Using `with open()`

The recommended way to work with files is:

    with open("data.txt", "r") as file:
        data = file.read()
        print(data)

The file is automatically closed after the `with` block.

### Without `with`

    file = open("data.txt", "r")

    data = file.read()

    print(data)

    file.close()

### With `with`

    with open("data.txt", "r") as file:
        print(file.read())

`with open()` is safer and easier because Python automatically closes the file.

---

## 9. Reading File Line by Line

We can use a `for` loop to read each line.

    with open("data.txt", "r") as file:
        for line in file:
            print(line)

This is useful when working with large files.

---

## 10. File Path

### File in the same folder

    open("data.txt", "r")

### File inside another folder

    open("data/data.txt", "r")

---

## 11. `read()` vs `readline()` vs `readlines()`
| Function | Purpose | Returns |
|----------|---------|---------|
| `read()` | Reads complete file | String |
| `readline()` | Reads one line | String |
| `readlines()` | Reads all lines | List |

---

## 12. `w` vs `a`

| Mode | Existing Data | New Data |
|------|---------------|----------|
| `w` | Replaced ❌ | Written ✅ |
| `a` | Kept ✅ | Added at end ✅ |

---

## 13. Example

Suppose `data.txt` contains:

    Priyanshi
    Python
    Data Science

Python code:

    with open("data.txt", "r") as file:
        data = file.read()

    print(data)

Output:

    Priyanshi
    Python
    Data Science

---

## Important Points

- `open()` is used to open a file.
- `r` is used for reading.
- `w` is used for writing and replacing content.
- `a` is used for appending.
- `x` is used to create a new file.
- `read()` reads the complete file.
- `readline()` reads one line.
- `readlines()` returns all lines as a list.
- `write()` writes data into a file.
- `with open()` automatically closes the file.
- `\n` creates a new line.

---

##  Quick Revision

| Function / Mode | Use |
|-----------------|-----|
| `open()` | Open a file |
| `r` | Read |
| `w` | Write / Replace |
| `a` | Append |
| `x` | Create |
| `read()` | Read everything |
| `readline()` | Read one line |
| `readlines()` | Read all lines |
| `write()` | Write data |
| `with open()` | Safe file handling |

---

##  Why File Handling is Important?

File handling is important because programs often need to work with external data.

Later, this will help when working with:

- CSV files
- JSON files
- Excel files
- Datasets
- Logs
- Data Science projects

### Basic Flow

    File
      ↓
    open()
      ↓
    Read / Write / Append
      ↓
    Process Data
