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

if __name__ == "__main__":
    run_find_max()