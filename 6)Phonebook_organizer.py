def add_contact(phonebook):
    name = input("Enter the name:")
    number = input("Enter the phone number:")
    phonebook[name] = number
    print(f"Contact {name} added successfully.")

def search_contact(phonebook):
    name = input("Enter the name to search:")
    if name in phonebook:
        print(f"Phone number for {name}: {phonebook[name]}")
    else:
        print(f"{name} not found in the phonebook.")

def update_contact(phonebook):
    name = input("Enter the name to update:")
    if name in phonebook:
        number = input("Enter the new phone number:")
        phonebook[name] = number
        print(f"Contact {name} updated successfully.")
    else:
        print(f"{name} not found in the phonebook.")

phonebook = {}

while True:
    print("\nPhonebook Organizer")
    print("1. Add Contact")
    print("2. search Contact")
    print("3. Update Contact")
    print("4. Quit")
    choice = input("Enter your choice:")

    if choice == "1":
        add_contact(phonebook)
    elif choice == "2":
        search_contact(phonebook)
    elif choice == "3":
        update_contact(phonebook)
    elif choice == "4":
        break
    else:
        print("Invalid choice. please try again.")