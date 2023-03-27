# pylint: disable=missing-module-docstring
from contact import Contact
class ContactList():
    """module:class:`ContactList()returns a list of contact objects"""
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone_number, email):
        """function: addscontacts into contact [] list"""
        contact = Contact(name, phone_number, email)

        self.contacts.append(contact)

    def view_contacts(self):
        """function: displays contacts from contact [] list"""
        for contact in self.contacts:
            print(contact)

    def edit_contact(self, index, name, phone_number, email):
        """function: edits details in contact [] list"""
        contact = self.contacts[index]
        contact.name = name
        contact.phone_number = phone_number
        contact.email = email
    def delete_contact(self, index):
        """function: deletes elements from contact [] list"""
        del self.contacts[index]

    def sort_contacts(self, sort_by = "name",rev=False):
        """function: sorts contacts from contact [] list"""
        sorted_contacts=sorted(self.contacts,key=lambda contact:getattr(contact,sort_by),rev=rev)
        return sorted_contacts
