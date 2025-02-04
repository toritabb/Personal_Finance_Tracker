# local
from ui import Canvas
from .page import Page, PageManagerBase

# pages
from .accounts import AccountsPage
from .add_bank import AddBankPage
from .add_expense import AddExpensePage
from .add_income import AddIncomePage
from .contact import ContactPage
from .create_account import CreateAccountPage
from .example import ExamplePage
from .faq import FAQPage
from .income_expenses import IncomeExpensesPage
from .login import LoginPage
from .more import MorePage
from .settings import SettingsPage
from .snapshot import SnapshotPage
from .welcome import WelcomePage
from .legal import LegalPage



__all__ = 'Page', 'PageManager'



class PageManager(PageManagerBase):
    def __init__(self, parent: Canvas) -> None:
        super().__init__(parent, 'example', AccountsPage, AddBankPage, AddExpensePage, AddIncomePage, ContactPage, CreateAccountPage, ExamplePage, FAQPage, IncomeExpensesPage, LoginPage, MorePage, SettingsPage, SnapshotPage, WelcomePage, LegalPage)

