contacts = {}


def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")

    contacts[name] = phone
    print("Contact added successfully!")


def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        print("\n===== CONTACT LIST =====")
        for name, phone in contacts.items():
            print(f"{name} : {phone}")


def search_contact():
    name = input("Enter Name to Search: ")

    if name in contacts:
        print(f"{name} : {contacts[name]}")
    else:
        print("Contact not found.")


def update_contact():
    name = input("Enter Name to Update: ")

    if name in contacts:
        new_phone = input("Enter New Phone Number: ")
        contacts[name] = new_phone
        print("Contact updated successfully!")
    else:
        print("Contact not found.")


def delete_contact():
    name = input("Enter Name to Delete: ")

    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")


while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")