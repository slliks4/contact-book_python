from __contacts.views import Contacts
from __user.views import User, UserNotFoundError


def face1():
    print("   .-~~~-.")
    print("  /       \\")
    print(" |  O   O  |")
    print(" |    ∆    |")
    print("  \\  ___  /")
    print("   `-----'")
    print("\n   Invalid Operation\n")


def first_action():
    print(
        """
        Your Personalized Contact Book

        Choose an operation:

        1. Login as existing user
        2. Create new user
        """
    )

    while True:
        try:
            first_input = int(input("Enter action: "))
            if first_input not in [1, 2]:
                raise ValueError("Invalid input. Please enter 1 or 2.")
            break
        except ValueError as e:
            print(e)
            face1()

    if first_input == 1:
        username = input("Enter your username to continue: ").strip()

        try:
            contacts_instance = Contacts(username)
            print(f"Welcome, {username}")
            third_action(contacts_instance)

        except UserNotFoundError as e:
            print(e)
            first_action()

    elif first_input == 2:
        username = input("Enter your desired username to continue: ").strip()

        try:
            result = User.create_user(username=username)
            print(result)
            contacts_instance = Contacts(username)
            third_action(contacts_instance)

        except Exception as e:
            print(e)
            first_action()


def third_action(contacts_instance):
    print(
        """
        Choose an operation:

        1. Add new contact
        2. List contacts
        3. Delete contact
        4. Close application
        """
    )

    while True:
        try:
            action = int(input("Enter action: "))
            if action not in [1, 2, 3, 4]:
                raise ValueError("Invalid input. Please enter a number between 1 and 4.")
            break
        except ValueError as e:
            print(e)
            face1()

    if action == 1:
        name = input("Enter contact name: ")
        tel = input("Enter contact telephone: ")
        result = contacts_instance.add_contact(name, tel)
        print(result)
        third_action(contacts_instance)

    elif action == 2:
        contacts = contacts_instance.load_contacts()
        if not contacts:
            print("No contacts found.")
        else:
            for contact in contacts:
                print(f"ID: {contact['id']}, Name: {contact['name']}, Tel: {contact['tel']}")
        third_action(contacts_instance)

    elif action == 3:
        contact_id = int(input("Enter contact ID to delete: "))
        result = contacts_instance.delete_contact(contact_id)
        print(result)
        third_action(contacts_instance)

    elif action == 4:
        print("Closing application...")

    else:
        face1()
        third_action(contacts_instance)


first_action()
