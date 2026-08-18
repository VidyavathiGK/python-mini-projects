def add_contact(contacts):
    """Adds a new contact to the dictionary."""
    first_name = input("Enter contact's first name: ").strip()
    last_name = input("Enter contact's last name: ").strip()
    full_name = f"{first_name} {last_name}"
    
    if full_name in contacts:
        print("A contact with this name already exists.")
        return
    
    phone = input("Enter contact's phone number: ").strip()
    email = input("Enter contact's email address: ").strip()
    
    contacts[full_name] = {'phone': phone, 'email': email}
    print(f"Contact '{full_name}' added successfully!")

def view_contacts(contacts):
    """Displays all saved contacts."""
    print("\n--- Your Contacts ---")
    if not contacts:
        print("Your contact book is empty.")
    else:
        for name in sorted(contacts.keys()):
            details = contacts[name]
            print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}")
    print("---------------------")

def search_contact(contacts):
    """Searches for a contact by their full name."""
    search_term = input("Enter the name of the contact to search for: ").strip()
    
    # Try for an exact match first
    if search_term in contacts:
        details = contacts[search_term]
        print("\n--- Contact Found ---")
        print(f"Name: {search_term}, Phone: {details['phone']}, Email: {details['email']}")
        print("---------------------")
        return

    # If no exact match, try a partial search
    found_contacts = {name: details for name, details in contacts.items() if search_term.lower() in name.lower()}
    if found_contacts:
        print("\n--- Search Results (contacts matching your search) ---")
        for name, details in found_contacts.items():
            print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}")
        print("----------------------------------------------------")
    else:
        print(f"No contact found matching '{search_term}'.")

def update_contact(contacts):
    """Updates an existing contact's information."""
    name_to_update = input("Enter the full name of the contact to update: ").strip()
    
    if name_to_update in contacts:
        print(f"Updating contact: {name_to_update}")
        new_phone = input(f"Enter new phone number (or press Enter to keep '{contacts[name_to_update]['phone']}'): ").strip()
        new_email = input(f"Enter new email address (or press Enter to keep '{contacts[name_to_update]['email']}'): ").strip()
        
        if new_phone:
            contacts[name_to_update]['phone'] = new_phone
        if new_email:
            contacts[name_to_update]['email'] = new_email
            
        print("Contact updated successfully!")
    else:
        print("Contact not found.")

def delete_contact(contacts):
    """Deletes a contact from the book."""
    name_to_delete = input("Enter the full name of the contact to delete: ").strip()
    
    if name_to_delete in contacts:
        confirm = input(f"Are you sure you want to delete {name_to_delete}? (yes/no): ").strip().lower()
        if confirm == 'yes':
            del contacts[name_to_delete]
            print("Contact deleted successfully!")
        else:
            print("Deletion cancelled.")
    else:
        print("Contact not found.")

def main():
    """Main function to run the Contact Book application."""
    contacts = {}
    
    print("--- Welcome to your Simple Contact Book ---")
    
    while True:
        print("\n--- Main Menu ---")
        print("1. Add a new contact")
        print("2. View all contacts")
        print("3. Search for a contact")
        print("4. Update a contact")
        print("5. Delete a contact")
        print("6. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()
