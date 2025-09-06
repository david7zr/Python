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

if __name__ == "__main__":
    run_multiplication_table()