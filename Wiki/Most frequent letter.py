def most_common_letter(word):
    d = {}

    if word == "":
        return None
    else:
        for char in word:
            if char in d.keys():
                d[char] += 1
            else:
                d[char] = 1

        most_frequent = max(d, key=d.get)
    return most_frequent


if __name__ == "__main__":
    word = "bookkeeper"
    print(most_common_letter(word))