class Contact:
    """Represents an individual contact with name, phone, email, and city."""

    def __init__(self, name: str, phone: str, email: str, city: str):
        self.name = name
        self.phone = phone
        self.email = email
        self.city = city


class AddressBook:
    """Manages a collection of contacts and search functionalities."""

    def __init__(self):
        self.contacts = []

    def add_contact(self, name: str, phone: str, email: str, city: str) -> None:
        """Adds a new contact to the address book."""
        new_contact = Contact(name, phone, email, city)
        self.contacts.append(new_contact)
        print(f"Contact '{name}' added successfully.")

    def search_by_name(self, name: str) -> None:
        """Searches for contacts matching a given name (case-insensitive partial match)."""
        results = [c for c in self.contacts if name.lower() in c.name.lower()]
        
        if not results:
            print(f"No contacts found matching '{name}'.")
            return

        print(f"\n--- Search Results for '{name}' ---")
        for contact in results:
            print(f"Name  : {contact.name}")
            print(f"Phone : {contact.phone}")
            print(f"Email : {contact.email}")
            print(f"City  : {contact.city}")
            print("-" * 25)

    def display_all(self) -> None:
        """Displays all saved contacts."""
        if not self.contacts:
            print("Your address book is empty.")
            return

        print("\n--- All Contacts ---")
        for index, contact in enumerate(self.contacts, start=1):
            print(f"{index}. {contact.name} | {contact.phone} | {contact.email} | {contact.city}")


# --- Example Usage ---
if __name__ == "__main__":
    my_directory = AddressBook()

    # Add sample contacts
    my_directory.add_contact("Rahul Sharma", "9876543210", "rahul@example.com", "Bengaluru")
    my_directory.add_contact("Priya Patel", "9123456789", "priya@example.com", "Mumbai")

    # Display all contacts
    my_directory.display_all()

    # Search contact by name
    my_directory.search_by_name("Rahul")
