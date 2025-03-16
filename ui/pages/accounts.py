# local
import ui
from data import data_manager
from .page import Page, PageManagerBase
from .header import HeaderPage



class AccountsPage(Page):
    STR = 'accounts'

    def __init__(self, parent: ui.Canvas, manager: PageManagerBase) -> None:
        super().__init__(parent, manager)

        header = HeaderPage(self, manager)

        # Get current user
        current_user = data_manager.get_current_user()
        if not current_user:
            print("Error: No user logged in")
            manager.go_to('login')
            return

        # Page title with username
        title = ui.Text(
            self,
            (25, header.bottom + 25),
            f"Welcome, {current_user.username}!",
            ('Nunito', 40, True, False)
        )

        # Show user's accounts
        account_y = title.bottom + 50
        for account_name, bank_account in current_user.accounts.items():
            # Account container
            account_text = ui.Text(
                self,
                (50, account_y),
                f"{account_name} ({bank_account.type})",
                ('Nunito', 24, True, False)
            )
            
            # Balance
            ui.Text(
                self,
                (50, account_y + 40),
                f"Balance: ${bank_account.balance/100:.2f}",  # Convert cents to dollars
                ('Nunito', 20)
            )
            
            account_y += 100  # Space for next account

        # # Add Account button
        # ui.TextButton(
        #     self,
        #     'Add Account',
        #     ('Nunito', 24),
        #     (25, account_y + 20),
        #     command=lambda: manager.go_to('add_bank'),
        #     padding=(20, 10),
        #     border_thickness=3,
        #     corner_radius=8
        # )

