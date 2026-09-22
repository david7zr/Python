import random

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}

def get_num_of_dice():
    while True:
        raw = input("How many dice?: ").strip()
        if not raw.lstrip("-").isdigit():
            print("Please enter a whole number (e.g. 3, max 6).")
            continue
        num = int(raw)
        if num <= 0:
            print("Please enter a number greater than 0.")
            continue
        if num > 6:
            print("That's a lot of dice — please enter 6 or fewer.")
            continue
        return num

num_of_dice = get_num_of_dice()

dice = [random.randint(1, 6) for _ in range(num_of_dice)]

for line in range(5):
    for die in dice:
        print(dice_art[die][line], end="")
    print()

total = sum(dice)
print(f"total: {total}")