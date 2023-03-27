# pylint: disable=missing-module-docstring
import re
from contact_list import ContactList
def menu():
    """menu : contains list of options"""
    print("1. Add contact")
    print("2. View contacts")
    print("3. Edit contact")
    print("4. Delete contact")
    print("5. Exit")

def main():
    """main : displays contact list"""
    contact_list = ContactList()

    while True:
        menu()
        choice = int(input("Enter your choice: "))

        if choice == 1:
            name = input("Enter name: ")
            pattern = re.compile(r"^[a-zA-Z]")
            if not pattern.match(name):
                raise ValueError("invalid Name: Enter valid name using a-z/A_Z instead")
            phone_number =input("Enter phone number: ")
            pattern = re.compile(r"^\d{10}$")
            if not pattern.match(phone_number):
                raise ValueError("Invalid phone number format")
            try :
                len(phone_number)!=10
            except ValueError:
                raise ValueError("Please enter 10 digit Phone Number")
                """"""
            email = input("Enter email: ")
            pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
            if not pattern.match(email):
                raise ValueError("Invalid email format")
            contact_list.add_contact(name, phone_number, email)

        elif choice == 2:
            contact_list.view_contacts()
        elif choice == 3:
            index = int(input("Enter index of contact to edit: "))
            name = input("Enter new name: ")
            phone_number = input("Enter new phone number: ")
            email = input("Enter new email: ")
            contact_list.edit_contact(index, name, phone_number, email)
        elif choice == 4:
            index = int(input("Enter index of contact to delete: "))
            contact_list.delete_contact(index)
        elif choice == 5:
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
