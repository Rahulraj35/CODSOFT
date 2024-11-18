import json

class ContactBook:
    def __init__(self):
        self.contacts = {}
        self.load_contacts()

    def load_contacts(self):
        """Load contacts from a file if it exists."""
        try:
            with open("contacts.json", "r") as file:
                self.contacts = json.load(file)
        except FileNotFoundError:
            self.contacts = {}

    def save_contacts(self):
        """Save contacts to a file."""
        with open("contacts.json", "w") as file:
            json.dump(self.contacts, file, indent=4)

    def add_contact(self):
        """Add a new contact."""
        print("\n--- Add New Contact ---")
        name = input("Enter name: ").strip()
        phone = input("Enter phone number: ").strip()
        email = input("Enter email: ").strip()
        address = input("Enter address: ").strip()
        
        if name in self.contacts:
            print(f"Contact for {name} already exists.")
        else:
            self.contacts[name] = {
                'phone': phone,
                'email': email,
                'address': address
            }
            print(f"Contact for {name} added successfully.")
        self.save_contacts()

    def view_contacts(self):
        """View all contacts."""
        print("\n--- View All Contacts ---")
        if self.contacts:
            for name, info in self.contacts.items():
                print(f"\nName: {name}")
                print(f"Phone: {info['phone']}")
                print(f"Email: {info['email']}")
                print(f"Address: {info['address']}")
        else:
            print("No contacts found.")

    def search_contact(self):
        """Search for a contact by name."""
        print("\n--- Search Contact ---")
        name = input("Enter name to search: ").strip()
        if name in self.contacts:
            info = self.contacts[name]
            print(f"\nName: {name}")
            print(f"Phone: {info['phone']}")
            print(f"Email: {info['email']}")
            print(f"Address: {info['address']}")
        else:
            print(f"Contact for {name} not found.")

    def update_contact(self):
        """Update an existing contact."""
        print("\n--- Update Contact ---")
        name = input("Enter name of contact to update: ").strip()
        if name in self.contacts:
            print("Leave fields blank if you don't want to update them.")
            phone = input(f"Enter new phone number ({self.contacts[name]['phone']}): ").strip()
            email = input(f"Enter new email ({self.contacts[name]['email']}): ").strip()
            address = input(f"Enter new address ({self.contacts[name]['address']}): ").strip()

            if phone:
                self.contacts[name]['phone'] = phone
            if email:
                self.contacts[name]['email'] = email
            if address:
                self.contacts[name]['address'] = address

            print(f"Contact for {name} updated successfully.")
            self.save_contacts()
        else:
            print(f"Contact for {name} not found.")

    def delete_contact(self):
        """Delete a contact."""
        print("\n--- Delete Contact ---")
        name = input("Enter name of contact to delete: ").strip()
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact for {name} deleted successfully.")
            self.save_contacts()
        else:
            print(f"Contact for {name} not found.")

    def main_menu(self):
        """Display the main menu and process user input."""
        while True:
            print("\n--- Contact Book ---")
            print("1. Add Contact")
            print("2. View All Contacts")
            print("3. Search Contact")
            print("4. Update Contact")
            print("5. Delete Contact")
            print("6. Exit")
            
            choice = input("Enter your choice: ").strip()

            if choice == '1':
                self.add_contact()
            elif choice == '2':
                self.view_contacts()
            elif choice == '3':
                self.search_contact()
            elif choice == '4':
                self.update_contact()
            elif choice == '5':
                self.delete_contact()
            elif choice == '6':
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    contact_book = ContactBook()
    contact_book.main_menu()
