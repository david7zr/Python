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

if __name__ == "__main__":
    run_find_missing_numbers()