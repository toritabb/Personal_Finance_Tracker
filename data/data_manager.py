# standard library
import json
import os

# local
import file
from .account import *



__all__ = 'DataManager', 'data_manager'



class DataManager:
    __slots__ = 'username', 'password', 'accounts'

    def __init__(self) -> None:
        self.username = ''
        self.accounts = []

    def load(self, username: str, password: str) -> None:
        if not os.path.exists(file.get_global_path(f'data/data/{username}.bin')):
            self.username = username
            self.password = password
            self.accounts: list[Account] = []

            self.save()

        self.accounts: list[Account] = []
        try:
<<<<<<< HEAD
            json_data = json.loads(file.load(self._storage_file))
            
            for account_data in json_data.get('accounts', []):
                if 'username' not in account_data or 'password' not in account_data:
                    account_data['username'] = account_data.get('name', 'default_user')
                    account_data['password'] = 'default_password'
                
                self.accounts.append(Account(**account_data))
=======
            json_data = json.loads(file.load(f'data/data/{username}.bin', password))
>>>>>>> 6bd7b7102724f695dc80602601980d9e84cd3dd7

            self.username = json_data['username']
            self.password = json_data['password']
            self.accounts = [Account(**account_data) for account_data in json_data['accounts']]

        except:
            print('Invalid Password')

    def save(self) -> None:
        json_data = json.dumps(self.get_save_dict(), indent=4)

        file.save(json_data, f'data/data/{self.username}.bin', self.password)
        file.save_plaintext(json_data, f'data/data/{self.username}.json')

    def get_save_dict(self) -> dict:
        return {
            'username': self.username,
            'password': self.password,
            'accounts': [account.get_save_dict() for account in self.accounts]
        }



data_manager = DataManager()

