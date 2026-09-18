# -----------------------------
# 1. Python Print Function
# -----------------------------
def print_numbers(n: int) -> None:
    for i in range(1, n + 1):
        print(i, end=" ")
    print()

def run_print_numbers() -> None:
    while True:
        try:
            n = int(input("Enter a number: "))
            if n <= 0:
                print("Number must be greater than 0.")
                continue
            break
        except ValueError:
            print("Invalid input! Enter an integer.")
    print_numbers(n)

# -----------------------------
# 2. Runner-up Score (Filtered List)
# -----------------------------
def runner_up_score(scores: list[int]) -> int:
    highest = max(scores)
    filtered = [s for s in scores if s != highest]
    return max(filtered) if filtered else highest

def run_runner_up_score() -> None:
    while True:
        try:
            n = int(input("Enter the number of scores: "))
            if n <= 0:
                print("Number must be greater than 0.")
                continue
            scores = list(map(int, input(f"Enter {n} scores separated by space: ").split()))
            if len(scores) != n:
                print(f"Please enter exactly {n} scores.")
                continue
            break
        except ValueError:
            print("Invalid input! Enter integers only.")
    print("Runner-up score:", runner_up_score(scores))

# -----------------------------
# 3. Even or Odd
# -----------------------------
def is_even(number: int) -> bool:
    return number % 2 == 0

def run_even_checker() -> None:
    while True:
        try:
            num = int(input("Enter a number to check if it is even: "))
            break
        except ValueError:
            print("Invalid input! Enter an integer.")
    print(f"{num} is {'even' if is_even(num) else 'odd'}")

# -----------------------------
# 4. Celsius to Fahrenheit
# -----------------------------
def celsius_to_fahrenheit(c: float) -> float:
    return (c * 9 / 5) + 32

def run_temperature_converter() -> None:
    while True:
        try:
            c = float(input("Enter temperature in Celsius: "))
            break
        except ValueError:
            print("Invalid input! Enter a number.")
    print(f"{c}°C is {celsius_to_fahrenheit(c)}°F")

# -----------------------------
# 5. Sum of Two Numbers
# -----------------------------
def sum_two_numbers(a: int, b: int) -> int:
    return a + b

def run_sum_two_numbers() -> None:
    while True:
        try:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            break
        except ValueError:
            print("Invalid input! Enter integers only.")
    print("Sum:", sum_two_numbers(a, b))

# -----------------------------
# 6. Largest of Three Numbers
# -----------------------------
def largest_of_three(a: int, b: int, c: int) -> int:
    return max(a, b, c)

def run_largest_of_three() -> None:
    while True:
        try:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            c = int(input("Enter third number: "))
            break
        except ValueError:
            print("Invalid input! Enter integers only.")
    print("Largest number:", largest_of_three(a, b, c))

# -----------------------------
# 7. Reverse a String
# -----------------------------
def reverse_string(s: str) -> str:
    return s[::-1]

def run_reverse_string() -> None:
    s = input("Enter a string to reverse: ")
    print("Reversed string:", reverse_string(s))

# -----------------------------
# 8. Count Vowels
# -----------------------------
def count_vowels(s: str) -> int:
    vowels = "aeiou"
    return sum(s.lower().count(v) for v in vowels)

def run_count_vowels() -> None:
    s = input("Enter a string: ")
    print("Number of vowels:", count_vowels(s))

# -----------------------------
# 9. Anagram Checker
# -----------------------------
def are_anagrams(s1: str, s2: str) -> bool:
    return sorted(s1.lower()) == sorted(s2.lower())

def run_anagram_checker() -> None:
    str1 = input("Enter first string: ")
    str2 = input("Enter second string: ")
    print(f"Anagrams? {'Yes' if are_anagrams(str1, str2) else 'No'}")

# -----------------------------
# 10. Factorial Calculator
# -----------------------------
import math
def factorial(n: int) -> int:
    return math.factorial(n)

def run_factorial_calculator() -> None:
    while True:
        try:
            n = int(input("Enter a number to calculate factorial: "))
            if n < 0:
                print("Number must be non-negative.")
                continue
            break
        except ValueError:
            print("Invalid input! Enter an integer.")
    print(f"Factorial of {n} is {factorial(n)}")

# -----------------------------
# 11. Multiplication Table
# -----------------------------
def multiplication_table(number: int) -> list[str]:
    return [f"{i} * {number} = {i*number}" for i in range(1, number + 1)]

def run_multiplication_table() -> None:
    while True:
        try:
            n = int(input("Enter a number for multiplication table: "))
            break
        except ValueError:
            print("Invalid input! Enter an integer.")
    for line in multiplication_table(n):
        print(line)

# -----------------------------
# 12. Find Missing Number in a Sequence
# -----------------------------
def find_missing_numbers(numbers: list[int]) -> list[int]:
    numbers.sort()
    missing = []
    for i in range(len(numbers) - 1):
        current = numbers[i]
        next_num = numbers[i + 1]
        if next_num - current > 1:
            missing.extend(range(current + 1, next_num))
    return missing

def run_find_missing_numbers() -> None:
    while True:
        try:
            numbers = list(map(int, input("Enter list of numbers separated by space: ").split()))
            if not numbers:
                print("List cannot be empty.")
                continue
            break
        except ValueError:
            print("Invalid input! Enter integers only.")
    missing = find_missing_numbers(numbers)
    if missing:
        print("Missing numbers:", missing)
    else:
        print("No numbers are missing")

# -----------------------------
# 13. Find Maximum in a List
# -----------------------------
def find_max(numbers: list[int]) -> int:
    return max(numbers)

def run_find_max() -> None:
    while True:
        try:
            numbers = list(map(int, input("Enter list of numbers separated by space: ").split()))
            if not numbers:
                print("List cannot be empty.")
                continue
            break
        except ValueError:
            print("Invalid input! Enter integers only.")
    print("Maximum number is:", find_max(numbers))

# -----------------------------
# 14. Fibonacci Sequence Generator
# -----------------------------
def fibonacci(n: int) -> list[int]:
    seq = []
    a, b = 0, 1
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq

def run_fibonacci() -> None:
    while True:
        try:
            n = int(input("Enter how many Fibonacci terms: "))
            if n <= 0:
                print("Number must be greater than 0.")
                continue
            break
        except ValueError:
            print("Invalid input! Enter an integer.")
    print("Fibonacci sequence:", fibonacci(n))

# -----------------------------
# 15. Password Strength Checker
# -----------------------------



def main_menu() -> None:
    exercises = {
        "1": ("Print Numbers", run_print_numbers),
        "2": ("Runner-up Score", run_runner_up_score),
        "3": ("Even or Odd", run_even_checker),
        "4": ("Celsius to Fahrenheit", run_temperature_converter),
        "5": ("Sum of Two Numbers", run_sum_two_numbers),
        "6": ("Largest of Three Numbers", run_largest_of_three),
        "7": ("Reverse a String", run_reverse_string),
        "8": ("Count Vowels", run_count_vowels),
        "9": ("Anagram Checker", run_anagram_checker),
        "10": ("Factorial Calculator", run_factorial_calculator),
        "11": ("Multiplication Table", run_multiplication_table),
        "12": ("Find Missing Numbers", run_find_missing_numbers),
        "13": ("Find Maximum in a List", run_find_max),
        "14": ("Fibonacci Sequence Generator", run_fibonacci),
        "0": ("Exit", None)
    }

    while True:
        print("\n--- HackerRank Python Exercises ---")
        for key, (name, _) in exercises.items():
            print(f"{key}. {name}")
        choice = input("Select an exercise by number (0 to exit): ").strip()

        if choice == "0":
            print("Exiting program. Goodbye!")
            break
        elif choice in exercises:
            _, func = exercises[choice]
            print(f"\n--- Running: {exercises[choice][0]} ---\n")
            func()  # call the selected function
        else:
            print("Invalid choice! Please select a valid exercise number.")

if __name__ == "__main__":
    main_menu()
