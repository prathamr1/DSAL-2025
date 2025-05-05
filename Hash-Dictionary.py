#Telephone Book Db using Hash Table (with two Hash Collisions Handliong techniques)

class TelephoneBook:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(self.size)] 

    def _hash(self, key):
        return sum(ord(c) for c in key) % self.size

    def add_client(self, name, number):
        index = self._hash(name)
        for client in self.table[index]:
            if client[0] == name:
                print("Client already exists.")
                return
        self.table[index].append((name, number))
        print("Client added successfully.")

    def lookup_client(self, name):
        index = self._hash(name)
        for client in self.table[index]:
            if client[0] == name:
                return client[1]
        return None

    def delete_client(self, name):
        index = self._hash(name)
        for i, client in enumerate(self.table[index]):
            if client[0] == name:
                del self.table[index][i]
                print("Client deleted successfully.")
                return
        print("Client not found.")

    def display_all_clients(self):
        found_clients = False
        for i in range(self.size):
            for client in self.table[i]:
                print(f"{client[0]}: {client[1]}")
                found_clients = True
        if not found_clients:
            print("Telephone book is empty.")


def display_menu():
    print("\nTelephone Book Menu")
    print("1. Add Client")
    print("2. Lookup Client")
    print("3. Display All Clients")
    print("4. Delete Client")
    print("5. Exit")


def main():
    telephone_book = TelephoneBook()

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter client's name: ").strip()
            number = input("Enter telephone number: ").strip()
            telephone_book.add_client(name, number)

        elif choice == '2':
            name = input("Enter client's name to lookup: ").strip()
            number = telephone_book.lookup_client(name)
            if number:
                print(f"{name}'s telephone number is: {number}")
            else:
                print("Client not found.")

        elif choice == '3':
            telephone_book.display_all_clients()

        elif choice == '4':
            name = input("Enter the name of the client to delete: ").strip()
            telephone_book.delete_client(name)

        elif choice == '5':
            print("Exiting the Telephone Book.")
            break

        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
