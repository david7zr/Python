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

if __name__ == "__main__":
    run_largest_of_three()