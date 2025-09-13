#Banc Account Simulation
import sys

balance = 0

while True:
    try:
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check balance")
        print("4. Exit")
        user_input = int(input("Enter a number: "))
    except ValueError:
        print("ERROR: Invalid number format!")
        continue  # only retry if input was invalid

    if user_input == 1:
        print("Deposit")
        deposit = float(input("How much will be your deposit?"))
        if deposit > 0:
            balance = balance + deposit
        else:
            print("ERROR: Invalid deposit!")
    elif user_input == 2:
        print("Withdraw")
        withdraw = float(input("How much will be your withdrawal?"))
        if withdraw > balance:
            print("Insufficient funds!")
        elif withdraw <= 0:
            print("Your withdrawal amount must be positive!")
        else:
            balance = balance - withdraw
    elif user_input == 3:
        print("Check balance")
        print("Your balance is: ", balance)
    elif user_input == 4:
        print("See you next time!")
        break
    else:
        print("Invalid option, try again.")
