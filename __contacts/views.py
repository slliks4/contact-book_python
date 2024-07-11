""" Contact class based views """
from __user.views import User


class Contacts:
    def __init__(self, username: str):
        self.__user = User.get_user(username)

    def add_contact(self, name: str, tel: str) -> str:
        contact_id = self.get_last_contact_id() + 1
        if not name or not tel or len(tel) > 15 or len(tel) < 9:
            return "Name must not be empty, tel must not be empty, and the length of tel must be at least 10 characters"

        contact = {
            "id": contact_id,
            "name": name,
            "tel": tel
        }

        self.__user["contacts"].append(contact)

        # Update user data in the database file
        User.action(self.__user)

        return "Contact added successfully"

    def delete_contact(self, contact_id):
        if not contact_id:
            return "Oops, contact_id not given"

        for contact in self.__user["contacts"]:
            if contact["id"] == contact_id:
                self.__user["contacts"].remove(contact)
                User.action(self.__user)
                return f"{contact['name']} deleted successfully"

        return "Contact not found or something went wrong"

    def get_last_contact_id(self) -> int:
        try:
            # Get the ID of the last contact
            return self.__user["contacts"][-1]["id"] if self.__user["contacts"] else 0
        except KeyError:
            return 0

    def total_contacts(self) -> int:
        return len(self.__user["contacts"])

    def load_contacts(self) -> list:
        return self.__user["contacts"]
