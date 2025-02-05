# standard library
import json

# local
import file
from .user import User
from .account import Account



__all__ = 'DataManager', 'data_manager'



class DataManager:
    __slots__ = 'users', '_storage_file', '_current_user'

    def __init__(self, storage_file: str = 'user_data.bin') -> None:
        self._storage_file = file.get_global_path(f'data/data/{storage_file}')
        self._current_user: User | None = None
        self.users: list[User] = []
        try:
            json_data = json.loads(file.load(self._storage_file))
            
            # Handle old format data migration
            if 'accounts' in json_data:
                # Migrate old accounts to new user structure
                for account_data in json_data['accounts']:
                    username = account_data.get('username', account_data.get('name', 'default_user'))
                    password = account_data.get('password', 'default_password')
                    
                    # Create new user
                    user = User(username=username, password=password)
                    # Create bank account for user
                    user.add_account(
                        name=account_data.get('name', f"{username}'s Account"),
                        type=account_data.get('type', 'checking'),
                        balance=account_data.get('balance', 0)
                    )
                    self.users.append(user)
            else:
                # Load new format
                self.users = [User(**user_data) for user_data in json_data.get('users', [])]

        except (json.JSONDecodeError, FileNotFoundError):
            pass  # Start with empty accounts list

    def authenticate_user(self, username: str, password: str) -> User | None:
        '''Authenticate a user with username and password.
        Returns the User if credentials are valid, None otherwise.'''
        for user in self.users:
            if user.username == username and user.password == password:
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
        return any(user.username == username for user in self.users)

    def create_user(self, username: str, password: str) -> User:
        '''Create a new user.'''
        user = User(username=username, password=password)
        self.users.append(user)
        self.save()
        return user

    def save(self) -> None:
        '''Save current data to storage file.'''
        with open(self._storage_file, 'w') as f:
            json_data = json.dumps(self.get_save_dict())
            file.save(json_data, self._storage_file)

    def get_save_dict(self) -> dict:
        return {
            'users': [user.get_save_dict() for user in self.users]
        }



data_manager = DataManager()

