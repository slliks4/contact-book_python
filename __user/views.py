import json
import os


class UserNotFoundError(Exception):
    pass


""" Users Class based view """


class User:
    DATABASE = os.path.join(os.path.dirname(__file__), '..', 'db', 'database.json')

    @staticmethod
    def create_user(username: str) -> str:
        if not username:
            return "Username must not be blank"

        user = {
            "username": username.strip(),
            "contacts": []
        }

        # Load existing user data
        users = User.load_users()

        # Check if username already exists
        for existing_user in users:
            if existing_user["username"] == user["username"]:
                return f"User with username '{username}' already exists"

        # Add the new user to the list
        users.append(user)

        # Write back to the database file
        with open(User.DATABASE, 'w') as file:
            json.dump(users, file, indent=4)

        return f"User with username '{username}' created successfully"

    @staticmethod
    def load_users() -> list:
        """
        Reads the user data from the database file.

        Returns:
            list: The list of users.
        """
        try:
            with open(User.DATABASE, 'r') as file:
                data = json.load(file)
                # Check if data is empty, if so, return an empty dictionary
                if not data:
                    return []
                return data
        except FileNotFoundError:
            return []  # Return an empty dictionary if file doesn't exist
        except json.JSONDecodeError:
            return []  # Return an empty dictionary if JSON decoding fails

    @staticmethod
    def action(user_dic: dict) -> str:
        """
        Writes the updated user data to the database file.

        Args:
            user_dic (dict): Updated user dictionary to be written to the database file.

        Returns:
            str: Confirmation message.
        """
        # Load existing user data
        users = User.load_users()

        # Find and update the user's data
        for index, user in enumerate(users):
            if user['username'] == user_dic['username']:
                users[index] = user_dic  # Update user data in the list
                break

        # Write back to the database file
        with open(User.DATABASE, 'w') as file:
            json.dump(users, file, indent=4)

        return "User data updated successfully"

    @staticmethod
    def get_user(username: str) -> dict:
        users = User.load_users()

        for user in users:
            if user['username'] == username:
                return user

        raise UserNotFoundError(f"User '{username}' not found")
