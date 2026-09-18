def get_evens(numbers):
    evens = []
    for i in numbers:
        if i % 2 == 0:
            evens.append(i)
    return evens

if __name__ == '__main__':
    count = int(input("How many numbers are in your list? "))
    numbers = []

    for i in range(count):
        num = int(input("Insert number: "))
        numbers.append(num)

    result = get_evens(numbers)
    print("Even numbers:", result)