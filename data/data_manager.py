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

        try:
            json_data = json.loads(file.load(self._storage_file))

            self.accounts = [Account(**account_data) for account_data in json_data['accounts']]

        except json.JSONDecodeError:
            self.accounts: list[Account] = []

    def save(self) -> None:
        json_data = json.dumps(self.get_save_dict(), indent=4)

        file.save(json_data, self._storage_file)
        file.save_plaintext(json_data, self._storage_file_json)

    def get_save_dict(self) -> dict:
        return {
            'accounts': [account.get_save_dict() for account in self.accounts]
        }



data_manager = DataManager()

