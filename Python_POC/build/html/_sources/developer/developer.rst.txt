

=============
Code
=============

.. code-block:: 

    #contact.py

    class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

    
    def __str__(self):
        return f"{self.name}: {self.phone_number}, {self.email}"
    

.. code-block:: 

    #contact_list.py
    
    from contact import Contact

    class ContactList:
        def __init__(self):
            self.contacts = []

        def add_contact(self, name, phone_number, email):
            contact = Contact(name, phone_number, email)
            self.contacts.append(contact)

        def view_contacts(self):
            for contact in self.contacts:
                print(contact)
        
        def edit_contact(self, index, name, phone_number, email):
            contact = self.contacts[index]
            contact.name = name
            contact.phone_number = phone_number
            contact.email = email

        def delete_contact(self, index):
            del self.contacts[index]
        
        def sort_contacts(self, sort_by = "name",reverse=False):
            sorted_contacts = sorted(self.contacts, key=lambda contact: getattr(contact, sort_by), reverse=reverse)
            return sorted_contacts
        

