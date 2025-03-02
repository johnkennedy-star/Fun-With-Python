import random

nm = random.randint(1,10)
attempts = 0

while True:
    attempts +=1
    guess=int(input("Enter a number between 1 and 10:"))
    if guess != nm:
        print("Wrong number, please try again")
    else:
        print("Congratulation, You Guessed right!")
        break