import csv

students=[]
for i in range(5):
    print(f"Enter details for students {i + 1}: ")
    name=input("Name: ")
    age=int(input("Age: "))
    grade=input("Grade: ")
    students.append([name,age,grade])
    
with open("students.csv","w",newline="") as file:
    writer=csv.writer(file)
    writer.writerow(["name","age","grade"])
    writer.writerows(students)
    
print("student data saved to students.csv")        
with open("students.csv","r",newline="") as file:
    reader=csv.reader(file)
    rows=list(reader)

print("{:<15} {:<8} {:<10}".format("Name","Age","Grade"))
print("-" * 33)

for row in rows[1:]:
    print("{:<15} {:<8} {:<10}".format(row[0],row[1],row[2]))