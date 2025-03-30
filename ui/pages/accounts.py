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

        # go to log in page if no user is logges in
        current_user = data_manager.user

        if current_user is None:
            print('Error: No user logged in')

            manager.go_to('login')

            return

        # update all of the balances
        for account in current_user.accounts.values():
            account.update_balance()

        # Page title with username
        title = ui.Text(
            self,
            (25, header.bottom + 25),
            f'Welcome, {current_user.name}!',
            ('Nunito', 40, True, False)
        )

        # Show user's accounts
        account_y = title.bottom + 50

        for i, account in enumerate(current_user.get_accounts()):
            account_text = ui.Text(
                self,
                (50, account_y + 100 * i),
                f'{account.name} ({account.type})',
                ('Nunito', 24, True, False)
            )

            balance_text = ui.Text(
                self,
                (50, account_text.bottom + 10),
                f'Balance: ${account.balance:,.2f}',
                ('Nunito', 20)
            )

            edit_account_button = ui.Button(
                self,
                (account_text.right + 10, account_text.centery - 14),
                (28, 28),
                lambda acc=account.name: manager.go_to('edit_account', account_name=acc),
                corner_radius=4
            )

            edit_pencil_image = ui.Image(
                self,
                (edit_account_button.left + 4, edit_account_button.top + 4),
                'edit.png',
            )

        # Add Account button
        add_account_button = ui.TextButton(
            self,
            'Add Account',
            ('Nunito', 25),
            (25, self.bottom - 36 - 20),
            command=lambda: manager.go_to('add_account'),
            padding=(20, 7),
            border_thickness=0,
            colors='button_accent',
        )


