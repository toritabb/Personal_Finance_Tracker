# standard library
from typing import Any, Optional
import json
import os

# local
import file



class DataManager(dict):
    __slots__ = '_storage_file'

    def __init__(self, storage_file: str = 'user_data.bin') -> None:
        self._storage_file = storage_file

        self._load_data()

    def _load_data(self) -> None:
        '''Load data from storage file if it exists.'''
        if os.path.exists(self._storage_file):
            try:
                with open(self._storage_file, 'r') as f:
                    json_data = file.load(self._storage_file)

                    self._data = json.loads(json_data)

            except json.JSONDecodeError:
                self._data = {}

    def _save_data(self) -> None:
        '''Save current data to storage file.'''
        with open(self._storage_file, 'w') as f:
            json_data = json.dumps(self._data)

            file.save(json_data, self._storage_file)
    


data_manager = DataManager()
