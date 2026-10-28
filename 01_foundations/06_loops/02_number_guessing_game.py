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
        
"""Number Guessing Game
while loops, break, and tracking state
The program picks a secret number between 1 and 100 (use the random module). The user guesses repeatedly. After each guess, say "Too high" or "Too low". When they get it right, congratulate them, report how many attempts it took, and add a comment on their performance (e.g. 5 or fewer = excellent, 8 or fewer = good, otherwise keep practicing).

Example:

I'm thinking of a number between 1 and 100.
Your guess: 50  -> Too high
Your guess: 25  -> Too low
Your guess: 37  -> Correct!
You got it in 3 attempts. Excellent!

Use a while loop that keeps going until the guess is correct.
"""       