def are_anagrams(s1: str, s2: str) -> bool:
    return sorted(s1.lower()) == sorted(s2.lower())

def run_anagram_checker() -> None:
    str1 = input("Enter first string: ")
    str2 = input("Enter second string: ")
    print(f"Anagrams? {'Yes' if are_anagrams(str1, str2) else 'No'}")

if __name__ == "__main__":
    run_anagram_checker()