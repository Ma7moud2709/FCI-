import random
flag = True

User = int(input("Enter a number between 1 and 10: "))          # Let user choose a number.

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]               # Define the array

while flag:

    for i in range(1, 4):
        Computer = random.choice(arr)       # Let compute guess the number

        print("Is ", Computer, "too high (H), Too low (L), Or correct (C)??")

        User_answer = str(input())      # Let user determine whether true or false

        # True
        if User_answer == 'C' or User_answer == 'c':
            print("Yey! The computer guessed your number,", Computer, ",Correctly ;)")
            flag = False        # To stop while loop.
            break               # To break for loop.
        # False
        if User_answer == 'H' or User_answer == 'h':
            for j in range(Computer, arr[len(arr)-1]+1):
                arr.remove(j)       # Remove numbers from the last element to computer is choice
        if User_answer == 'L' or User_answer == 'l':
            for k in range(arr[0], Computer + 1):
                arr.remove(k)       # Remove elements from the first element to computer choice
        if i == 3:
            print("Hard luck my beautiful computer :) :) ")
            flag = False
        print(arr)
