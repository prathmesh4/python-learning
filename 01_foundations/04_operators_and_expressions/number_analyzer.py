num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))

if num1>num2:
    larger=num1
    smaller=num2
elif num2>num1:
    larger=num2
    smaller=num1
else:
    larger=num1
    smaller=num2
        
print(f"Larger: {larger}")

if  smaller!=0:
    print(f"Reminder of {larger} / {smaller} : {larger % smaller} ")    
else:
    print("can not calculate reminder (Devision by zero).")
    
if num1%2==0 and num2 %2 ==0:
    print("Both even")
elif num1%2!=0 and num2%2!=0:
    print("Both ood")
else:
    print("Mixed")