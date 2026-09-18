def most_frequent_word(text):
    words = text.lower().split()
    d = {}
    for i in words:
        if i not in d.keys():
            d[i] = 0
        d[i] += 1

    most_frequent = max(d, key=d.get)
    return most_frequent


if __name__ == "__main__":
    text = input("Enter a sentence: ")
    print(most_frequent_word(text))