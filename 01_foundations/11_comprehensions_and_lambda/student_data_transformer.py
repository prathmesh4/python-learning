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