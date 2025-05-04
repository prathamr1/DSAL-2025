# Telephone Book using Hash Table (Python Dictionary)

def display_menu():
    print("\nTelephone Book Menu")
    print("1. Add Client")
    print("2. Lookup Client")
    print("3. Display All Clients")
    print("4. Delete Client")
    print("5. Exit")

def main():
    telephone_book = {}  # Hash table

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter client's name: ").strip()
            if name in telephone_book:
                print("Client already exists.")
            else:
                number = input("Enter telephone number: ").strip()
                telephone_book[name] = number
                print("Client added successfully.")

        elif choice == '2':
            name = input("Enter client's name to lookup: ").strip()
            number = telephone_book.get(name)
            if number:
                print(f"{name}'s telephone number is: {number}")
            else:
                print("Client not found.")

        elif choice == '3':
            if not telephone_book:
                print("Telephone book is empty.")
            else:
                print("\n--- Telephone Book ---")
                for name, number in telephone_book.items():
                    print(f"{name}: {number}")

        elif choice == '4':
            name = input("Enter the name of the client to delete: ").strip()
            if name in telephone_book:
                del telephone_book[name]
                print("Client deleted successfully.")
            else:
                print("Client not found.")

        elif choice == '5':
            print("Exiting the Telephone Book.")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
