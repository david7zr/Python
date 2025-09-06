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

if __name__ == "__main__":
    run_factorial_calculator()