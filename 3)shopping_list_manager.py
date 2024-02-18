def main():
    shopping_list = []

    while True:
        print("\nOptions:")
        print("1. Add item")
        print("2. Remove item")
        print("3. Check off item")
        print("4. Display list")
        print("5. Quit")

        choice = input("Enter your choice (1-5):")

        if choice == "1":
            item = input("Enter item to add:")
            shopping_list.append(item)
        elif choice == "2":
            item = input("Enter item to remove:")
            if item in shopping_list:
                shopping_list.remove(item)
            else:
                print("item not found in the shopping list.")
        elif choice == "3":
            item = input("Enter item to check off:")
            if item in shopping_list:
                print(f"checked off: {item}")
            else:
                print("Item not found in the shopping list.")
        elif choice == "4":
            print("Shopping list:")
            for item in shopping_list:
                print(f"-{item}")
        elif choice == "5":
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__=="__main__":
    main()
