'''
wap a menu-driven pyth prog where the user can add items, remove items,view cart,and exit.
'''
l = ["shoes,pen,car"]
while True:
    print("/n1. Add item")
    print("2. Remove item")
    print("3. View item")
    print("4. Exit item")

    choice = int(input("Enter userchoice: "))
    if choice == 1:
        item = input("item_Name: ")
        l.append(item)

    elif choice == 2:
        item = input("Remove_item_Name: ")
        if item in l:
         l.remove(item)
        else:
            print("Item not found")

    elif choice == 3:
        print(l)

    elif choice == 4:
        print("Exit")
        break
    
    else:
        print("Invalid choice")