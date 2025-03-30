# standard library
import json
import os
from typing import Optional

# local
import encryption
import file
from .user import User



__all__ = 'DataManager', 'data_manager'



class DataManager:
    __slots__ = 'user'

    def __init__(self) -> None:
        self.user: Optional[User] = None

        # self.load()

    def __del__(self) -> None:
        if self.user is not None:
            self.save_user_data(self.user)

    @staticmethod
    def _get_user_data_path(email: str) -> str:
        filename = encryption.get_hash(email)

        user_data_path = file.get_global_path(f'data/data/users/{filename}.save')

        return user_data_path

    def load_user_data(self, email: str, password: str) -> User | None:
        '''
        Load a user's data and return a `User` object.
        '''

        try:
            user_data_path = self._get_user_data_path(email)

            json_data = file.load(user_data_path, password)

            user_data = json.loads(json_data)

            return User(**user_data)

        except Exception as e:
            print(f'Something failed when loading user "{email}"\n{e}')

    def save_user_data(self, user: User) -> None:
        '''
        Save a user's data.
        '''

        user_data = user.get_save_dict()

        json_data = json.dumps(user_data)

        user_data_path = self._get_user_data_path(user.email)

        file.save(json_data, user_data_path, user.password)

    def login_user(self, email: str, password: str) -> bool:
        '''
        Authenticate a user with username and password and log them in.

        Returns the `True` if credentials are valid, `False` otherwise.
        '''

        if self.user is not None:
            print('Another user is already logged in!')

            return False

        if not self.user_exists(email):
            print(f'User "{email}" doesn\'t exist')

            return False

        user = self.load_user_data(email, password)

        if user is None: return False

        self.user = user

        return True

    def logout_user(self) -> None:
        '''
        Logs out the current user. Does nothing if there is no user logged in.
        '''

        if self.user is None:
            return
        
        self.save_user_data(self.user)

        del self.user

        self.user = None

    def user_exists(self, email: str) -> bool:
        '''
        Check if a user with the given `email` already exists.
        '''

        user_data_path = self._get_user_data_path(email)
        
        return file.path_exists(user_data_path)

    def create_user(self, name: str, email: str, password: str) -> None:
        '''
        Create a new user with default checking and savings accounts.
        '''

        # create user
        user = User(name, email, password)

        # add default checking and savings accounts for the user
        user.add_account(name='My Checking', type='checking')
        user.add_account(name='My Savings', type='savings')

        # create a file for the user
        self.save_user_data(user)

    def export_current_user_data(self, filepath: str) -> bool:
        '''
        Export current user's data to a readable JSON file.

        Returns `True` if successful, `False` otherwise.
        '''

        if self.user is None:
            return False

        try:
            # Ensure the directory exists
            export_dir = file.get_global_path('data/exports')
            os.makedirs(export_dir, exist_ok=True)

            # Export the data
            user_data = self.user.get_save_dict()

            with open(filepath, 'w') as f:
                json.dump(user_data, f, indent=4)

            return True

        except Exception as e:
            print(f'Error exporting data: {e}')

            return False



data_manager = DataManager()

