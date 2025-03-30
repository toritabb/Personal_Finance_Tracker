# local
import ui
from data import data_manager
from .page import Page, PageManagerBase
from .header import HeaderPage



class AddBankAccountPage(Page):
    STR = 'add_account'

    def __init__(self, parent: ui.Canvas, manager: PageManagerBase) -> None:
        super().__init__(parent, manager)

        # Get current user
        current_user = data_manager.user

        if current_user is None:
            print("Error: No user logged in")
            manager.go_to('login')
            return

        # Page title with username
        title = ui.Text(
            self,
            (0, 75),
            'Add Account',
            ('Nunito', 50, True, False)
        )
        ui.center(title)

        # Cancel/back button
        cancel_button = ui.TextButton(
            self,
            'Cancel',
            ('Nunito', 20),
            (25, 660),
            command=lambda: manager.back(),
            padding=(15, 7)
        )

