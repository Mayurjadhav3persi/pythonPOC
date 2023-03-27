# pylint: disable=too-few-public-methods
"""Module providingFunction returning  name,phone_number and email address"""

class Contact:
    """module: class:`Contact`
    Class: Contact returns a Contact object
    """
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

    def __str__(self):
        return f"{self.name}, {self.phone_number}, {self.email}"
