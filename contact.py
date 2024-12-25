class Contact:
    """
    Represents a single contact in the contact book.
    """
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}\nPhone: {self.phone}\nEmail: {self.email}\nAddress: {self.address}"


class ContactManager:
    """
    Manages the operations for adding, viewing, searching, updating, and deleting contacts.
    """
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        self.contacts.append(Contact(name, phone, email, address))
        print("\nContact added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("\nNo contacts found!")
            return

        print("\nContact List:")
        for idx, contact in enumerate(self.contacts, start=1):
            print(f"{idx}. {contact.name} - {contact.phone}")

    def search_contact(self, keyword):
        results = [contact for contact in self.contacts if keyword.lower() in contact.name.lower() or keyword in contact.phone]
        
        if not results:
            print("\nNo matching contacts found!")
            return

        print("\nSearch Results:")
        for contact in results:
            print(contact)
            print("-" * 30)

    def update_contact(self, search_name):
        for contact in self.contacts:
            if contact.name.lower() == search_name.lower():
                print("\nUpdating contact details:")
                contact.name = input("Enter new name: ").strip() or contact.name
                contact.phone = input("Enter new phone number: ").strip() or contact.phone
                contact.email = input("Enter new email: ").strip() or contact.email
                contact.address = input("Enter new address: ").strip() or contact.address
                print("\nContact updated successfully!")
                return
        
        print("\nNo contact found with that name!")

    def delete_contact(self, search_name):
        for contact in self.contacts:
            if contact.name.lower() == search_name.lower():
                self.contacts.remove(contact)
                print("\nContact deleted successfully!")
                return

        print("\nNo contact found with that name!")


def main():
    """
    Main function to provide a user interface for managing contacts.
    """
    manager = ContactManager()
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        try:
            choice = int(input("\nEnter your choice: ").strip())
            if choice == 1:
                name = input("Enter name: ").strip()
                phone = input("Enter phone number: ").strip()
                email = input("Enter email: ").strip()
                address = input("Enter address: ").strip()
                manager.add_contact(name, phone, email, address)
            elif choice == 2:
                manager.view_contacts()
            elif choice == 3:
                keyword = input("Enter name or phone number to search: ").strip()
                manager.search_contact(keyword)
            elif choice == 4:
                search_name = input("Enter the name of the contact to update: ").strip()
                manager.update_contact(search_name)
            elif choice == 5:
                search_name = input("Enter the name of the contact to delete: ").strip()
                manager.delete_contact(search_name)
            elif choice == 6:
                print("\nThank you for using the Contact Management System. Goodbye!")
                break
            else:
                print("\nInvalid choice! Please select a valid option.")
        except ValueError:
            print("\nInvalid input! Please enter a number.")

if __name__ == "__main__":
    main()
