def add_expense(expenses, category, amount):
    if category in expenses:
        expenses[category] += amount
    else:
        expenses[category] = amount

def display_expenses(expenses):
    print("Travel Expenses:")
    for category, amount in expenses.items():
        print(f"{category}: ${amount:.2f}")

if __name__ == "__main__":
    travel_expenses = {}

    while True:
        print("\n1. Add Expense")
        print("2. Display Expenses")
        print("3. Exit")
        choice = input("Enter your choice:")

        if choice == "1":
            category = input("Enter the expense category:")
            amount = float(input("Enter the expense amount:"))
            add_expense(travel_expenses, category, amount)
            print("Expense added successfully.")
        elif choice == "2":
            display_expenses(travel_expenses)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter enter 1, 2, or 3.")