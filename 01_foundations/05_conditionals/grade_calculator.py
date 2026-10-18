marks=float(input("Enter marks (0-100): "))

if marks < 0 or marks > 100:
    print("Invalid Marks")
elif marks >= 90:   
    print("Grade: A")
    print("Status: Pass") 
elif marks >= 70:   
    print("Grade: B")
    print("Status: Pass") 
elif marks >= 60:   
    print("Grade: C")
    print("Status: Pass") 
elif marks >= 40:   
    print("Grade: D")
    print("Status: Pass")             
else:
    print("Grade: Fail")    
    print("Status: Fail")    