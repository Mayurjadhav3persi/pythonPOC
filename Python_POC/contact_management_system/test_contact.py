# pylint: disable=missing-module-docstring
import pytest
from contact import Contact
from contact_list import ContactList


@pytest.fixture
def contact_list():
    """returns a list of contacts[]"""
    return ContactList()

def test_add_contact(contact_list):
    """function: this module tests adding a contact_list into the contacts[] has all the data"""
    contact_list.add_contact(name="John", phone_number="1234567890", email="john@example.com")
    assert len(contact_list.contacts) == 1
    assert contact_list.contacts[0].name == "John Smith"
    assert contact_list.contacts[0].phone_number == "123-456-7890"
    assert contact_list.contacts[0].email == "john.smith@example.com"



def test_edit_contact(contact_list):
    contact_list.add_contact(name="John", phone_number="1234567890", email="john@example.com")
    contact_list.edit_contact(0,name="Shalu", phone_number="986723478", email="shalu@gmail.com")
    #contact_list.edit_contact(contact)
    assert len(contact_list.contacts) == 1
    assert contact_list.contacts[0].name == "Shalu Mishra"
    assert contact_list.contacts[0].phone_number == "986723478"
    assert contact_list.contacts[0].email == "shalu_mishra@gmail.com"
    print(contact_list)


def test_delete_contact(contact_list):
    """
    module: function that tests deleting a contact.
    parameter:
        contact_list (any): contact list
    """
    contact_list.add_contact(name="John", phone_number="1234567890", email="john@example.com")
    contact_list.add_contact(name="Mayur", phone_number="6756289700", email="mayur@example.com")

    contact_list.delete_contact(0)
    assert len(contact_list.contacts) == 1



def test_sort_contacts(contact_list):
    contact1 = Contact(name="John", phone_number="1234567890", email="john@example.com")
    contact2 = Contact(name="Jane Doe", phone_number="234-567-8901", email="jane.doe@example.com")
    contact_list.add_contact(contact1)
    contact_list.add_contact(contact2)
    contact_list.sort_contacts("name")
    assert contact_list.contacts == [contact2, contact1]
    contact_list.sort_contacts("date_added")
    assert contact_list.contacts == [contact1, contact2]
