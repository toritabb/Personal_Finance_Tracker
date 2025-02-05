from __future__ import annotations
from typing import Literal

from .account import Account


class User:
    __slots__ = 'username', 'password', 'accounts'

    def __init__(self, username: str, password: str, accounts: list[dict] | None = None) -> None:
        self.username = username
        self.password = password
        self.accounts = {
            account_data['name']: Account(**account_data)
            for account_data in (accounts or [])
        }

    def get_save_dict(self) -> dict:
        return {
            'username': self.username,
            'password': self.password,
            'accounts': [account.get_save_dict() for account in self.accounts.values()]
        }

    def add_account(self, name: str, type: Literal['checking', 'savings'] = 'checking', balance: int = 0) -> Account:
        '''Create and add a new bank account for this user'''
        account = Account(name=name, type=type, balance=balance)
        self.accounts[name] = account
        return account
