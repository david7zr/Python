def reverse_string(s: str) -> str:
    return s[::-1]

def run_reverse_string() -> None:
    s = input("Enter a string to reverse: ")
    print("Reversed string:", reverse_string(s))

if __name__ == "__main__":
    run_reverse_string()