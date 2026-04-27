# Contact Book Application

contacts = []

def show_menu():
    print("\n===== CONTACT BOOK MENU =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def add_contact():
    print("\n--- Add New Contact ---")
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(contact)
    print("Contact added successfully!")

def view_contacts():
    if not contacts:
        print("\nNo contacts found.")
        return
    
    print("\n--- Contact List ---")
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact['name']} - {contact['phone']}")

def search_contact():
    query = input("\nEnter name or phone to search: ").lower()
    found = False

    for contact in contacts:
        if query in contact['name'].lower() or query in contact['phone']:
            print("\nContact Found:")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")
            found = True

    if not found:
        print("No matching contact found.")

def update_contact():
    view_contacts()
    try:
        index = int(input("\nEnter contact number to update: ")) - 1

        if 0 <= index < len(contacts):
            print("\nEnter new details (leave blank to keep old value):")
            
            name = input("New name: ")
            phone = input("New phone: ")
            email = input("New email: ")
            address = input("New address: ")

            if name:
                contacts[index]['name'] = name
            if phone:
                contacts[index]['phone'] = phone
            if email:
                contacts[index]['email'] = email
            if address:
                contacts[index]['address'] = address

            print("Contact updated successfully!")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_contact():
    view_contacts()
    try:
        index = int(input("\nEnter contact number to delete: ")) - 1

        if 0 <= index < len(contacts):
            removed = contacts.pop(index)
            print(f"Deleted contact: {removed['name']}")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Please enter a valid number.")

# Main loop
while True:
    show_menu()
    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        print("Exiting Contact Book. Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")