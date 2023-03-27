import pytest
from contact_management_system import contact, contact_list

@pytest.fixture
def contact_list():
    return ContactList()

def test_add_contact(contact_list):
    contact = Contact(name="John Smith", phone="123-456-7890", email="john.smith@example.com")
    contact_list.add_contact(contact)
    assert len(contact_list.contacts) == 1
    assert contact_list.contacts[0] == contact

def test_edit_contact(contact_list):
    contact = Contact(name="John Smith", phone="123-456-7890", email="john.smith@example.com")
    contact_list.add_contact(contact)
    contact.email = "johnsmith@example.com"
    contact_list.edit_contact(contact)
    assert len(contact_list.contacts) == 1
    assert contact_list.contacts[0].email == "johnsmith@example.com"

def test_delete_contact(contact_list):
    contact = Contact(name="John Smith", phone="123-456-7890", email="john.smith@example.com")
    contact_list.add_contact(contact)
    contact_list.delete_contact(contact)
    assert len(contact_list.contacts) == 0

def test_search_contact(contact_list):
    contact1 = Contact(name="John Smith", phone="123-456-7890", email="john.smith@example.com")
    contact2 = Contact(name="Jane Doe", phone="234-567-8901", email="jane.doe@example.com")
    contact_list.add_contact(contact1)
    contact_list.add_contact(contact2)
    results = contact_list.search_contact("John")
    assert len(results) == 1
    assert results[0] == contact1

def test_export_contacts(contact_list):
    contact1 = Contact(name="John Smith", phone="123-456-7890", email="john.smith@example.com")
    contact2 = Contact(name="Jane Doe", phone="234-567-8901", email="jane.doe@example.com")
    contact_list.add_contact(contact1)
    contact_list.add_contact(contact2)
    filename = "contacts.csv"
    contact_list.export_contacts(filename)
    with open(filename, "r") as f:
        content = f.read()
        assert "John Smith,123-456-7890,john.smith@example.com" in content
        assert "Jane Doe,234-567-8901,jane.doe@example.com" in content

def test_import_contacts(contact_list):
    filename = "contacts.csv"
    with open(filename, "w") as f:
        f.write("John Smith,123-456-7890,john.smith@example.com\n")
        f.write("Jane Doe,234-567-8901,jane.doe@example.com\n")
    contact_list.import_contacts(filename)
    assert len(contact_list.contacts) == 2

def test_sort_contacts(contact_list):
    contact1 = Contact(name="John Smith", phone="123-456-7890", email="john.smith@example.com")
    contact2 = Contact(name="Jane Doe", phone="234-567-8901", email="jane.doe@example.com")
    contact_list.add_contact(contact1)
    contact_list.add_contact(contact2)
    contact_list.sort_contacts("name")
    assert contact_list.contacts == [contact2, contact1]
    contact_list.sort_contacts("date_added")
    assert contact_list.contacts == [contact1, contact2]
