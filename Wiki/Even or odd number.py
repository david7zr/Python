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

if __name__ == "__main__":
    run_even_checker()
