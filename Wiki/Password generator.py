import random
import os

# Character pools
lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = lowercase.upper()
digits = "0123456789"
symbols = "!@#$%^&*()-_=+[]{};:,.<>?/"

def clear_screen():
    """Clear the terminal screen (works on Windows, Linux, Mac)."""
    os.system('cls' if os.name == 'nt' else 'clear')

def shuffle_string(s):
    """Shuffle the characters in a string and return the shuffled string."""
    s_list = list(s)
    random.shuffle(s_list)
    return "".join(s_list)

def beginner_password():
    """Generate a beginner password: 8 characters, lowercase + digits."""
    combined = lowercase + digits
    password = "".join(random.choice(combined) for _ in range(8))
    return shuffle_string(password)

def intermediate_password():
    """Generate an intermediate password: 10–12 characters, lowercase + uppercase + digits."""
    combined = lowercase + uppercase + digits
    length = random.randint(10, 12)
    password = "".join(random.choice(combined) for _ in range(length))
    return shuffle_string(password)

def advanced_password():
    """Generate an advanced password: 14–20 characters, includes lowercase, uppercase, digits, and symbols."""
    # Guaranteed characters
    password_chars = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Remaining characters
    total_length = random.randint(14, 20)
    remaining_length = total_length - 4
    combined = lowercase + uppercase + digits + symbols
    password_chars += [random.choice(combined) for _ in range(remaining_length)]

    # Shuffle all characters
    random.shuffle(password_chars)
    return "".join(password_chars)

def show_menu():
    """Display the password generator menu."""
    print("\nWelcome to the Password Generator!")
    print("1. Beginner password generator")
    print("2. Intermediate password generator")
    print("3. Advanced password generator")
    print("4. Exit")

def main():
    """Main program loop."""
    while True:
        show_menu()
        try:
            choice = int(input("Choose an option (1-4): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1-4.")
            continue

        if choice == 1:
            clear_screen()
            print("Your password is: " + beginner_password())
            input("\npress enter to continue...")
            clear_screen()
        elif choice == 2:
            clear_screen()
            print("Your password is: " + intermediate_password())
            input("\npress enter to continue...")
            clear_screen()
        elif choice == 3:
            clear_screen()
            print("Your password is: " + advanced_password())
            input("\npress enter to continue...")
            clear_screen()
        elif choice == 4:
            clear_screen()
            break
        else:
            print("Invalid option. Please select between 1-4.")

if __name__ == "__main__":
    main()
