# standard library
import json

# local
import file
from .account import *



__all__ = 'DataManager', 'data_manager'



class DataManager:
    __slots__ = 'accounts', '_storage_file', '_storage_file_json'

    def __init__(self, storage_file: str = 'user_data') -> None:
        self._storage_file = file.get_global_path(f'data/data/{storage_file}.bin')
        self._storage_file_json = file.get_global_path(f'data/data/{storage_file}.json')

        self.accounts: list[Account] = []
        try:
            json_data = json.loads(file.load(self._storage_file))
            
            for account_data in json_data.get('accounts', []):
                # Handle old format accounts by adding default username/password
                if 'username' not in account_data or 'password' not in account_data:
                    account_data['username'] = account_data.get('name', 'default_user')
                    account_data['password'] = 'default_password'
                
                self.accounts.append(Account(**account_data))

        except (json.JSONDecodeError, FileNotFoundError):
            pass  # Start with empty accounts list

    def authenticate_user(self, username: str, password: str) -> bool:
        '''Authenticate a user with username and password.'''
        for account in self.accounts:
            if account.username == username and account.password == password:
                return True
        return False

    def user_exists(self, username: str) -> bool:
        '''Check if a username already exists.'''
        return any(account.username == username for account in self.accounts)

    def create_user(self, username: str, password: str) -> Account:
        '''Create a new user account.'''
        account = Account(username=username, password=password)
        self.accounts.append(account)
        self.save()
        return account

    def save(self) -> None:
        '''Save current data to storage file.'''
        with open(self._storage_file, 'w') as f:
            json_data = json.dumps(self.get_save_dict())
            file.save(json_data, self._storage_file)
        json_data = json.dumps(self.get_save_dict(), indent=4)

        file.save(json_data, self._storage_file)
        file.save_plaintext(json_data, self._storage_file_json)

    def get_save_dict(self) -> dict:
        return {
            'accounts': [account.get_save_dict() for account in self.accounts]
        }



data_manager = DataManager()

