word = "APPLE"
word = word.lower()

letter = input("Guess a letter in the secret word: ")
letter = letter.lower()

while len(letter) != 1 or not letter.isalpha():
    print("Please enter exactly one letter from the alphabet.")
    letter = input("Guess a letter in the secret word: ")
    letter = letter.lower()

if letter in word:
    print("Your letter is in the secret word")
else:
    print("Your letter is not in the secret word")