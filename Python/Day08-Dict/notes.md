Day 08 — Dictionary (dict) — notes.md
# Python Dictionary


## 1. What is Dictionary?
A dictionary is a collection of data stored in **key-value pairs**.


Syntax:
```python
dictionary = {
    "key": "value"
}
---
Example:

student = {
    "name": "Priyanshi",
    "age": 21,
    "course": "Python"
}
2. Key-Value Pair
"name": "Priyanshi"
"name" → Key
"Priyanshi" → Value

We access values using their keys.

print(student["name"])
---
3. Properties of Dictionary
Stores data in key-value pairs
Keys must be unique
Keys should be immutable (string, number, tuple, etc.)
Values can be of any data type
Dictionary is mutable
Dictionary maintains insertion order in modern Python
Dictionary is written using {}

---
4. Creating Dictionary
student = {
    "name": "Priyanshi",
    "age": 21,
    "city": "Ahmedabad"
}

Empty dictionary:
student = {}


5. Accessing Values

Using key:
print(student["name"])

Using get():
print(student.get("name"))
---
Difference:

student["marks"]       # gives KeyError if key doesn't exist
student.get("marks")   # gives None if key doesn't exist
6. Add New Key-Value
student["marks"] = 90
7. Update Value
student["marks"] = 95

If the key already exists → value is updated.

If the key doesn't exist → new key-value pair is added.

8. Delete Data

Using del:

del student["age"]

Using pop():

student.pop("age")

Remove all items:

student.clear()

9. Important Dictionary Methods
Method	Use
get()	Get value
keys()	Get all keys
values()	Get all values
items()	Get key-value pairs
update()	Add/update key-value pairs
pop()	Remove a key
clear()	Remove all items

10. keys()

Returns all keys.
student.keys()

11. values()
Returns all values.
student.values()

12. items()
Returns key-value pairs.
student.items()

Example:
for key, value in student.items():
    print(key, value)

13. update()
Used to add or update data.
student.update({"marks": 90})

14. Checking Key
Use in:

if "name" in student:
    print("Name exists")

15. Loop Through Dictionary
Only keys:
for key in student:
    print(key)

Only values:

for value in student.values():
    print(value)

Both key and value:

for key, value in student.items():
    print(key, value)

16. Nested Dictionary
A dictionary can contain another dictionary.

students = {
    "student1": {
        "name": "Priyanshi",
        "age": 21
    },
    "student2": {
        "name": "Rahul",
        "age": 22
    }
}

---
Access:

print(students["student1"]["name"])
17. Dictionary vs Other Collections
List → index based
Tuple → index based
Set → unordered collection with no indexing
Dictionary → key-value based
---
Example:

student = {"name": "Priyanshi"}
print(student["name"])

Here "name" is used instead of an index.

18. Important Interview Points
Can dictionary have duplicate keys?

No.

If duplicate keys are used, the latest value replaces the previous value.

data = {
    "name": "A",
    "name": "B"
}

Result:

{"name": "B"}
Can dictionary values be duplicate?

Yes.

data = {
    "a": 10,
    "b": 10
}
Can a dictionary key be a list?

No, because list is mutable.

# Invalid
data = {
    [1, 2]: "value"
}
Quick Revision

Dictionary = Key + Value

data = {
    "name": "Priyanshi",
    "age": 21
}

Access:
data["name"]

Add:
data["city"] = "Ahmedabad"

Update:
data["age"] = 22

Delete:
data.pop("age")
---
Important methods:

get()
keys()
values()
items()
update()
pop()
clear()
