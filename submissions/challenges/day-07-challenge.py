shoppingList = []
userChoice = 0

while True:
    print("\n Options \n 1. Add item to shopping list \n 2. View Shopping list \n 3. Remove item from the shopping list \n 4. Quit")
    userChoice = (input("Enter the number of your choice: "))

    if userChoice == '1':
        item = input("Enter the item you want to add: ")
        print(f"{item} has been added to the shopping list.")
        shoppingList.append(item)
        continue

    elif userChoice == '2':
        print("Your shopping list: ")
        for i in range(len(shoppingList)):
            print(f"{i + 1}. {shoppingList[i]}")
        continue

    elif userChoice == '3':
        item = input("Enter the item you want to remove: ")
        print(f"{item} has been removed from the shopping list.")
        shoppingList.remove(item)
        continue
    
    elif userChoice == '4':
        print("Goodbye !")
        break

    else:
        print("\n Please enter a valid choice.")
        continue
