import random

# Define
arr = ['r', 'p', 's']
U_score = 0
C_score = 0

for i in range(1, 4):
    # User
    User = str(input("Whats your choice ? "
                     "'r' for rock, 'p' for paper, 's' for scissor\n-->"))

    # Computer
    Computer = random.choice(arr)

    # Conditions
    # tie
    if User == Computer:
        print("You and the computer have been chosen", User, ". It's tie\n")

    # User win
    elif User == 'r' and Computer == 's':
        print("You have chosen", User, "and the computer has chosen", Computer, ". You won :)\n")
        U_score += 1
    elif User == 's' and Computer == 'p':
        print("You have chosen", User, "and the computer has chosen", Computer, ". You won :)\n")
        U_score += 1
    elif User == 'p' and Computer == 'r':
        print("You have chosen", User, "and the computer has chosen", Computer, ". You won :)\n")
        U_score += 1

    # Computer win
    elif Computer == 'r' and User == 's':
        print("You have chosen", User, "and the computer has chosen", Computer, ". You lost :(\n")
        C_score += 1
    elif Computer == 's' and User == 'p':
        print("You have chosen", User, "and the computer has chosen", Computer, ". You lost :(\n")
        C_score += 1
    elif Computer == 'p' and User == 'r':
        print("You have chosen", User, "and the computer has chosen", Computer, ". You lost :(\n")
        C_score += 1

if U_score > C_score:
    print("Congratulations, You have won the best of 3 games. Good ;)")
elif U_score < C_score:
    print("Unfortunately, Computer has won the best of 3 games. Better luck next time! :(")
elif U_score == C_score:
    print("Draw")