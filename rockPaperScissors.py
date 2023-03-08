# Rock, Paper, Scissors game using random library
import random
user = input("Enter 'r' for Rock, 'p' for Paper or 's' for Scissors: ")
computer = random.choice(['r', 'p', 's'])

# paper is better than rock
# rock is better than scissors
# scissors is better than paper
if user == 'r' and computer == 's':
    print("Computer selected scissors and you won!")
elif user == 'p' and computer == 'r':
    print("Computer selected Rock and you won!")
elif user == 's' and computer == 'p':
    print("Computer selected paper and you won!")
elif user == 'r' and computer == 'r':
    print("Its a tie!")
elif user == 'p' and computer == 'p':
    print("Its a tie!")
elif user == 's' and computer == 's':
    print("Its a tie!")
else:
    print(f"Computer selected {computer} and you lost!")


