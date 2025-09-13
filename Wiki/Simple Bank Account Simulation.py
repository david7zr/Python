# Bank Account Simulation

def show_menu() -> None:
    """Display the menu options."""
    print("\n--- Bank Menu ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check balance")
    print("4. Exit")

def deposit(balance: float) -> float:
    """Handle deposit transactions."""
    try:
        amount = float(input("Enter deposit amount: "))
        if amount > 0:
            balance += amount
            print(f"Deposited: {amount:.2f}")
        else:
            print("Deposit must be greater than 0.")
    except ValueError:
        print("Invalid input. Please enter a number.")
    return balance

def withdraw(balance: float) -> float:
    """Handle withdrawal transactions."""
    try:
        amount = float(input("Enter withdrawal amount: "))
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > balance:
            print("Insufficient funds.")
        else:
            balance -= amount
            print(f"Withdrawn: {amount:.2f}")
    except ValueError:
        print("Invalid input. Please enter a number.")
    return balance

def print_balance(balance: float) -> None:
    """Print current balance."""
    print(f" Your current balance is: {balance:.2f}")

def main() -> None:
    balance = 0.0
    while True:
        show_menu()
        try:
            choice = int(input("Choose an option: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1-4.")
            continue

        if choice == 1:
            balance = deposit(balance)
        elif choice == 2:
            balance = withdraw(balance)
        elif choice == 3:
            print_balance(balance)
        elif choice == 4:
            print("See you next time!")
            break
        else:
            print("Invalid option. Please select between 1-4.")

if __name__ == "__main__":
    main()
