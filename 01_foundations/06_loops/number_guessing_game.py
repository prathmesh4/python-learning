import random

secret_num = random.randint(1,100)
attempts = 0

print("I am thonking of a number between 1 to 100")

while True:
    guess = int(input("Your guess: "))
    attempts +=1
    
    if guess < secret_num:
        print("Too low!")
    elif guess > secret_num:
        print("Too high!")    
    else:
        print("Correct!")
        break    

print(f"You get it in {attempts} attempts.")

if attempts < 5:
    print("Excellent!")
elif attempts <= 8:
    print("Good!")            
else:
    print("Keep practicing!")
        