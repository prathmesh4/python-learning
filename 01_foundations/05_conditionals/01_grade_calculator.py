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

"""Grade Calculator
if/elif/else chains and input validation
Ask the user for marks out of 100 and print a grade:
• 90–100 -> A
• 75–89  -> B
• 60–74  -> C
• 40–59  -> D
• below 40 -> Fail

Also print whether the student passed (40 or above). If the marks are less than 0 or greater than 100, print an "Invalid input" message instead of a grade.

Example:

Enter marks (0-100): 82
Grade: B
Status: Pass
"""    