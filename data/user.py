# standard library
from typing import Literal, Optional

# local
from .account import Account



__all__ = 'User',



class User:
    __slots__ = 'name', 'email', 'password', 'accounts'

    def __init__(self, name: str, email: str, password: str, accounts: Optional[list[dict]] = None) -> None:
        self.name = name
        self.email = email
        self.password = password

        self.accounts = {account_data['name']: Account(**account_data) for account_data in (accounts or [])}

    def get_save_dict(self) -> dict[str, str | list[dict]]:
        return {
            'name': self.name,
            'email': self.email,
            'password': self.password,
            'accounts': [account.get_save_dict() for account in self.accounts.values()]
        }

    def add_account(self, name: str, type: Literal['checking', 'savings'], balance: int = 0) -> Account:
        '''Create and add a new bank account for this user'''

        account = Account(name=name, type=type, balance=balance)
        self.accounts[name] = account

        return account

