import random
flag = True

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]               # Define the array
Computer = random.choice(arr)       # Let computer guess the number
while flag:

    for i in range(1, 5):

        User = int(input("Guess a number between 1 and 10: "))  # Let user choose a number.

        if User == Computer:        # Correct
            print("Yey, Congrats. You have guessed the number", Computer, "Correctly ;)")
            flag = False        # To stop while loop.
            break               # To break for loop.

        if User > Computer:         # High
            print("sorry, Guess again. Too high.")
        if User < Computer:         # Low
            print("sorry, Guess again. Too low.")
        if i == 4:
            print("Hard luck :(")
            flag = False
