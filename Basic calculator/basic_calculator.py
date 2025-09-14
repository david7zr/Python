# Basic calculator

def addition():
    """Handle addition."""
    try:
        print("Selected Add")
        first_number = int(input("Enter first number: "))
        second_number = int(input("Enter second number: "))
        return first_number + second_number
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None

def subtract():
    """Handle subtraction."""
    try:
        print("Selected Subtract")
        first_number = int(input("Enter first number: "))
        second_number = int(input("Enter second number: "))
        return first_number - second_number
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None

def multiply():
    """Handle multiplication."""
    try:
        print("Selected Multiply")
        first_number = int(input("Enter first number: "))
        second_number = int(input("Enter second number: "))
        return first_number * second_number
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None

def divide():
    """Handle division."""
    try:
        print("Selected Divide")
        first_number = int(input("Enter first number: "))
        second_number = int(input("Enter second number: "))
        if second_number == 0:
            print("Error: Division by zero is not allowed.")
            return None
        return first_number / second_number
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None

def show_menu():
    """Show menu."""
    print("\nBasic Calculator")
    print("1. Addition")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

def main():
    """Run main function."""
    while True:
        show_menu()
        try:
            choice = int(input("Input your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1-5.")
            continue

        result = None
        if choice == 1:
            result = addition()
        elif choice == 2:
            result = subtract()
        elif choice == 3:
            result = multiply()
        elif choice == 4:
            result = divide()
        elif choice == 5:
            print("Thank you for using this program")
            break
        else:
            print("Invalid option. Please try again.")

        if result is not None:
            print("Result:", result)

if __name__ == "__main__":
    main()
