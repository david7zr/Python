#2 dimensional list = [list1, list2, list3]

fruits = ["apple", "orange", "banana", "coconut"]
vegetables = ["celery", "carrots", "potatoes"]
meat = ["chicken", "fish", "turkey"]

groceries = [fruits, vegetables, meat]
for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()

