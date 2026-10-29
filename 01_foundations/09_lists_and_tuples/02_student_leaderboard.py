students=[]
n=int(input("Enter no of student: "))

for i in range(n):
    name=input("Enter name : ")
    marks=float(input("Enter marks: "))
    students.append([name,marks])

leaderboard=sorted(students, key=lambda s:s[1],reverse=True)

total=0
for s in students:
    total +=s[1]
        
average=total/n

print("Top 3 students: ")
for s in leaderboard[:3]:
    print(s[0] , "-", s[1])        
    
print("Bottom 3 students: ")
for s in leaderboard[-3:]:
    print(s[0] , "-", s[1])            
    
above_average=[]    
below_average=[] 

for s in students:
    if s[1]>average:
        above_average.append(s[0])
    elif s[1]<average:
        below_average.append(s[0])
               
print("Class average:", round(average,2))               
print("Above average: ",", ".join(above_average))
print("Below Average: ",",".join(below_average))

print("Full Leaderboard: ")
for s , student in enumerate(leaderboard,start=1):
    print(f"{s}.  {student[0]} - {student[1]}")
    
"""Student Leaderboard
Lists of lists and sorting with a key
Take n students, each stored as [name, marks], into a list of lists. Then produce:
• The top 3 and bottom 3 students by marks
• Students above and below the class average
• The full leaderboard sorted from highest to lowest

Example:

Leaderboard:
1. Neha    - 95
2. Arjun   - 88
3. Sara    - 76
...
Class average: 79.5
Above average: Neha, Arjun
Below average: Sara, ...

Hint: sorted(students, key=lambda s: s[1], reverse=True) sorts by marks.
"""    