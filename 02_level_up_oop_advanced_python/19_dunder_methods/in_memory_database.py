import json

class Database:
    def __init__(self, name, filename=None):
        self.name = name
        self.filename = filename
        self.rows = []
    def add(self, row_dict):
        if not isinstance(row_dict, dict):
            raise TypeError("Row must be a dictionary")
        if self.rows and row_dict.keys() != self.rows[0].keys():
            raise ValueError("All rows must have the same keys")
        self.rows.append(row_dict.copy())
    def remove(self, index):
        del self.rows[index]
    def __len__(self):
        return len(self.rows)
    def __getitem__(self, index):
        return self.rows[index]
    def __setitem__(self, index, row_dict):
        if not isinstance(row_dict, dict):
            raise TypeError("Row must be a dictionary")
        if self.rows and row_dict.keys() != self.rows[0].keys():
            raise ValueError("All rows must have the same keys")
        self.rows[index] = row_dict.copy()
    def __contains__(self, value):
        return any(
            value == cell
            for row in self.rows
            for cell in row.values()
        )
    def __iter__(self):
        return iter(self.rows)
    def __str__(self):
        if not self.rows:
            return f"Database: {self.name} (0 rows)\n(empty)"
        headers = list(self.rows[0].keys())
        widths = {
            key: max(
                len(str(key)),
                *(len(str(row[key])) for row in self.rows)
            )
            for key in headers
        }
        lines = [f"Database: {self.name} ({len(self)} rows)"]
        lines.append(
            "  ".join(str(key).ljust(widths[key]) for key in headers)
        )
        for row in self.rows:
            lines.append(
                "  ".join(
                    str(row[key]).ljust(widths[key])
                    for key in headers
                )
            )
        return "\n".join(lines)
    def __repr__(self):
        return f"Database({self.name!r}, rows={len(self)})"
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        if self.filename:
            with open(self.filename, "w", encoding="utf-8") as file:
                json.dump(self.rows, file, indent=4)
            print(f"Database saved to {self.filename}")
        return False
with Database("students", "students.json") as db:
    db.add({"name": "Prathmesh", "marks": 95, "city": "Mumbai"})
    db.add({"name": "Pranav", "marks": 92, "city": "Mumbai"})
    db.add({"name": "Rahul", "marks": 67, "city": "Delhi"})
    db.add({"name": "Sara", "marks": 78, "city": "Pune"})
    db.add({"name": "Karan", "marks": 85, "city": "Pune"})
    print(db)
    print("\ndb[0] =", db[0])
    print("db[1:3] =", db[1:3])
    print('\n"Prathmesh" in db:', "Prathmesh" in db)
    print('"Unknown" in db:', "Unknown" in db)
    print("\nIterating through database:")
    for row in db:
        print(row)
    db[0] = {"name": "Prathmesh", "marks": 98, "city": "Pune"}
    print("\nAfter updating the first row:")
    print(db)
    print("\nlen(db):", len(db))
print("\nUsing context manager:")
with open("students.json", "r", encoding="utf-8") as file:
    saved_data = json.load(file)
print("\nSaved JSON contents:")
print(json.dumps(saved_data, indent=4))

"""
In-Memory Database
You'll practice
Container dunders and context manager — making a custom class behave like a built-in collection
Create a Database class — a simple in-memory table that behaves like a Python built-in.

Constructor: Takes a name (string) and an optional filename (for persistence).

Data storage: Internally holds a list of dicts (rows). Each row is a dict with the same keys.

Methods:
- add(row_dict) — adds a row. Validates that keys match existing rows (if any exist).
- remove(index) — removes row at index.

Dunder methods:
- __len__ — number of rows
- __getitem__ — db[0] returns row 0 (dict). db[1:3] returns a list of rows (slicing support).
- __setitem__ — db[0] = {"name": "Updated", ...} replaces row 0
- __contains__ — "Amit" in db returns True if "Amit" appears as a VALUE in any row, any column
- __iter__ — iterate through all rows with a for loop
- __str__ — prints a formatted table with headers and aligned columns
- __repr__ — returns "Database('name', rows=5)"
- __enter__ / __exit__ — context manager. On exit, if filename was provided, save all data to a JSON file. Print "Database saved to {filename}" on exit.

Demonstrate:
1. Add 5 rows of student data (name, marks, city)
2. Print the database (formatted table)
3. Access row by index and by slice
4. Check membership: "Amit" in db
5. Iterate with a for loop
6. Update a row with db[0] = {...}
7. Print len
8. Use as context manager — data should be saved to file on exit
9. Open the saved JSON file and print its contents to verify

Example output:
 
Database: students (5 rows)
name       marks  city  
Prathmesh  95     Mumbai
Pranav     92     Mumbai
Rahul      67     Delhi 
Sara       78     Pune  
Karan      85     Pune  

db[0] = {'name': 'Prathmesh', 'marks': 95, 'city': 'Mumbai'}
db[1:3] = [{'name': 'Pranav', 'marks': 92, 'city': 'Mumbai'}, {'name': 'Rahul', 'marks': 67, 'city': 'Delhi'}]

"Prathmesh" in db: True
"Unknown" in db: False

Iterating through database:
{'name': 'Prathmesh', 'marks': 95, 'city': 'Mumbai'}
{'name': 'Pranav', 'marks': 92, 'city': 'Mumbai'}
{'name': 'Rahul', 'marks': 67, 'city': 'Delhi'}
{'name': 'Sara', 'marks': 78, 'city': 'Pune'}
{'name': 'Karan', 'marks': 85, 'city': 'Pune'}

After updating the first row:
Database: students (5 rows)
name       marks  city  
Prathmesh  98     Pune  
Pranav     92     Mumbai
Rahul      67     Delhi 
Sara       78     Pune  
Karan      85     Pune  

len(db): 5
Database saved to students.json

Using context manager:

Saved JSON contents:
[
    {
        "name": "Prathmesh",
        "marks": 98,
        "city": "Pune"
    },
    {
        "name": "Pranav",
        "marks": 92,
        "city": "Mumbai"
    },
    {
        "name": "Rahul",
        "marks": 67,
        "city": "Delhi"
    },
    {
        "name": "Sara",
        "marks": 78,
        "city": "Pune"
    },
    {
        "name": "Karan",
        "marks": 85,
        "city": "Pune"
    }
]
"""