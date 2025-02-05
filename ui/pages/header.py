# local
import ui
from data import data_manager
from .page import Page, PageManagerBase



class HeaderPage(Page):
    STR = 'header'

    def __init__(self, parent: ui.Canvas, manager: PageManagerBase) -> None:
        super().__init__(parent, manager, height=125, fill_color=ui.HEADER)

        padding = (30, 10)

        snapshot = ui.TextButton(
            self,
            'Snapshot',
            ('Nunito', 40, True, False),
            (0, 25),
            lambda: manager.go_to('snapshot'),
            padding=padding,
            corner_radius=15,
            colors='button_accent'
        )
        accounts = ui.TextButton(
            self,
            'Accounts',
            ('Nunito', 40, True, False),
            (snapshot.right + 50, 25),
            lambda: manager.go_to('accounts'),
            padding=padding,
            corner_radius=15,
            colors='button_accent'
        )
        income_expenses = ui.TextButton(
            self,
            'Income/Expenses',
            ('Nunito', 40, True, False),
            (accounts.right + 50, 25),
            lambda: manager.go_to('income_expenses'),
            padding=padding,
            corner_radius=15,
            colors='button_accent'
        )
        more = ui.TextButton(
            self,
            'More',
            ('Nunito', 40, True, False),
            (income_expenses.right + 50, 25),
            lambda: manager.go_to('more'),
            padding=padding,
            corner_radius=15,
            colors='button_accent'
        )
        ui.center(snapshot, accounts, income_expenses, more, axis='xy')

