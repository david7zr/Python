#Exercise practicing Using list, set and tuples

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy: ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of the {food}: $"))
        foods.append(food)
        prices.append(price)

print("Your cart shopping is: ")
for food in foods:
    print(food)
for price in prices:
    total = total + price
print(f"Your total is: ${total:.2f}")
