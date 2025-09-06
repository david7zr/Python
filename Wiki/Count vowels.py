def count_vowels(s: str) -> int:
    vowels = "aeiou"
    return sum(s.lower().count(v) for v in vowels)

def run_count_vowels() -> None:
    s = input("Enter a string: ")
    print("Number of vowels:", count_vowels(s))

if __name__ == "__main__":
    run_count_vowels()