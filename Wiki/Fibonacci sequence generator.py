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

if __name__ == "__main__":
    run_fibonacci()