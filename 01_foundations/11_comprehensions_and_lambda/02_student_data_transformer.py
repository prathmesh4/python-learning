students = [
    {'name': 'A', 'city': 'Delhi',  'marks': 82, 'department': 'CS'},
    {'name': 'B', 'city': 'Mumbai', 'marks': 91, 'department': 'CS'},
    {'name': 'C', 'city': 'Delhi',  'marks': 75, 'department': 'IT'},
    {'name': 'D', 'city': 'Mumbai', 'marks': 68, 'department': 'IT'},
    {'name': 'E', 'city': 'Delhi',  'marks': 95, 'department': 'CS'},
    {'name': 'F', 'city': 'Mumbai', 'marks': 80, 'department': 'IT'}
]
grades = {
    s['name']: (
        'A' if s['marks'] >= 90 else
        'B' if s['marks'] >= 80 else
        'C' if s['marks'] >= 70 else
        'D'
    )
    for s in students
}
print(grades)

selected = [
    s['name']
    for s in students
    if s['city'] == 'Delhi' and s['marks'] > 80
]
print(selected)

city = 'Delhi'
cutoff = 80
selected = [
    s['name'] for s in students
    if s['city'] == city and s['marks'] > cutoff
]

by_marks = [
    s['name']
    for s in sorted(students, key=lambda s: s['marks'], reverse=True)
]
print(by_marks)

departments = {s['department'] for s in students}
dept_avg = {
    d: round(
        sum(s['marks'] for s in students if s['department'] == d)
        / sum(1 for s in students if s['department'] == d),
        2
    )
    for d in {s['department'] for s in students}
}
print(dept_avg)

"""Student Data Transformer
Dict comprehensions and filtering
Given a list of student dictionaries (each with name, city, marks, department), produce — using ONLY comprehensions:
• a {name: grade} dictionary
• a filtered list of students from a given city whose marks are above a cutoff
• a list of names sorted by marks (highest first)
• a {department: average_marks} dictionary

Example:

students = [
  {'name':'A','city':'Delhi','marks':82,'department':'CS'},
  {'name':'B','city':'Mumbai','marks':91,'department':'CS'},
  ...
]

name -> grade: {'A':'B', 'B':'A', ...}
Delhi & marks>80: ['A']
By marks: ['B', 'A', ...]
dept avg: {'CS': 86.5, ...}
"""