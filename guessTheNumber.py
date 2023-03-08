# Game to guess the random number
import random
computer = random.randint(1, 9)
guess = False
counter = 0
while not guess:
    usernum = int(input("Enter a number between 1 and 9: "))
    counter = counter + 1
    if usernum == computer:
        guess = True
    elif usernum < computer:
        print("Too low!")
    else:
        print("Too high!")

    if counter > 2:
        print("Too many guesses!!")
        break

if guess:
    print("You guessed it right!")
else:
    print("You lost!")

