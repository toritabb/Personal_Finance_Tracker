# standard library
import json
import os

# local
import file
from .user import User
from .account import Account



__all__ = 'DataManager', 'data_manager'



class DataManager:
    __slots__ = ('users', '_storage_file', '_current_user')
    _current_user: User | None

    def __init__(self) -> None:
        self.users = {}  # Dictionary with username as key, User object as value

        self._storage_file = file.get_global_path('data/data/users.json')
        self._current_user = None

        self.load()

    def load(self) -> None:
        try:
            data_str = file.load(self._storage_file, 'password123')

            data = json.loads(data_str)

            self.users = {
                user_data['username']: User(**user_data)
                for user_data in data.get('users', [])
            }

        except:
            self.users = {}  # Start with empty users dict

    def authenticate_user(self, username: str, password: str) -> User | None:
        '''Authenticate a user with username and password.
        Returns the User if credentials are valid, None otherwise.'''

        user = self.users.get(username)

        if user and user.password == password:
            return user

        return None

    def get_current_user(self) -> User | None:
        '''Get the currently logged in user.'''

        return getattr(self, '_current_user', None)

    def set_current_user(self, user: User | None) -> None:
        '''Set the currently logged in user.'''

        self._current_user = user

    def user_exists(self, username: str) -> bool:
        '''Check if a username already exists.'''

        return username in self.users

    def create_user(self, username: str, password: str) -> User:
        '''Create a new user with a default checking account.'''

        user = User(username=username, password=password)
        user.add_account("My Checking", "checking")

        self.users[username] = user

        self.save()

        return user

    def save(self) -> None:
        '''Save current data to storage file.'''

        data = self.get_save_dict()

        data_str = json.dumps(data)

        file.save(data_str, self._storage_file, 'password123')

        # with open(self._storage_file, 'w') as f:
        #     json.dump(data, f, indent=2)

    def get_save_dict(self) -> dict:
        return {
            'users': [user.get_save_dict() for user in self.users.values()]
        }

    def export_current_user_data(self, filepath: str) -> bool:
        '''Export current user's data to a readable JSON file.
        Returns True if successful, False otherwise.'''

        if not self._current_user:
            return False
            
        try:
            # Ensure the directory exists
            export_dir = file.get_global_path('data/exports')
            os.makedirs(export_dir, exist_ok=True)
            
            # Export the data
            user_data = self._current_user.get_save_dict()

            with open(filepath, 'w') as f:
                json.dump(user_data, f, indent=4)

            return True

        except Exception as e:
            print(f"Error exporting data: {e}")

            return False



data_manager = DataManager()

