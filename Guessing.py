import random

secret_number = random.randint(1, 10)
ans = int(input("Enter your guess here: "))

if ans > secret_number:
    print("Too high")
    
elif ans < secret_number:
    print("Too low")
        #ans = int(input("Enter your guess here: "))
else:
    print("You won")
    