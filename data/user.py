# standard library
from typing import Literal, Optional

# local
from .account import Account



__all__ = 'User',



class User:
    __slots__ = 'name', 'email', 'password', 'accounts', 'settings'

    def __init__(self, name: str, email: str, password: str, accounts: Optional[list[dict]] = None, settings: Optional[dict[str, bool]] = None) -> None:
        self.name = name
        self.email = email
        self.password = password

        self.accounts: dict[str, Account] = {account_data['name']: Account(**account_data) for account_data in (accounts or [])}

        self.settings = Settings(**(settings if settings else {}))

    def get_save_dict(self) -> dict[str, str | dict | list[dict]]:
        return {
            'name': self.name,
            'email': self.email,
            'password': self.password,
            'accounts': [account.get_save_dict() for account in self.accounts.values()],
            'settings': self.settings.get_save_dict()
        }

    def add_account(
            self,
            name: str,
            type: Literal['checking', 'savings'],
            starting_balance: float = 0.0
        ) -> Account:

        '''Create and add a new bank account for this user'''

        account = Account(name=name, type=type, balance=starting_balance, starting_balance=starting_balance, index=len(self.accounts))
        self.accounts[name] = account

        return account

    def remove_account(
            self,
            name: str
        ) -> None:

        '''Remove a bank account from this user'''

        self.accounts.pop(name, None)
    
    def get_accounts(self) -> list[Account]:
        return sorted([account for account in self.accounts.values()], key=lambda a: a.index)



class Settings:
    def __init__(self, **settings) -> None:
        if 'dark_mode' in settings:
            self.dark_mode = settings['dark_mode']

        else:
            self.dark_mode = False
            
        if 'notifications' in settings:
            self.notifications = settings['notifications']

        else:
            self.notifications = True

    def set(self, setting: str, value: bool) -> None:
        match setting:
            case 'dark_mode':
                self.dark_mode = value
                
            case 'notifications':
                self.notifications = value

    def get_save_dict(self) -> dict[str, bool]:
        return {
            'dark_mode': self.dark_mode,
            'notifications': self.notifications,
        }

