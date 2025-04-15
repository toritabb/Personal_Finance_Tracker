# local
import ui
from data import data_manager
from .page import Page, PageManagerBase



class EditAccountPage(Page):
    STR = 'edit_account'

    def __init__(self, parent: ui.Canvas, manager: PageManagerBase, account_name: str) -> None:
        super().__init__(parent, manager)

        # go to log in page if no user is logges in
        current_user = data_manager.user

        if current_user is None:
            print('Error: No user logged in')

            manager.go_to('login')

            return

        account = current_user.accounts[account_name]

        #########
        # Title #
        #########

        title_label = ui.Text(
            self,
            (50, 50),
            f'Edit "{account.name}"',
            ('Nunito', 40, True, False)
        )

        ui.center(title_label)

        ################
        # Account name #
        ################

        name_label = ui.Text(
            self,
            (150, title_label.bottom + 50),
            f'Account name',
            ('Nunito', 25)
        )

        name_ptr = ui.Pointer(account.name)
        name_box = ui.Textbox(
            self,
            name_ptr,
            ('Nunito', 20),
            (name_label.left, name_label.bottom + 7),
            (300, -1),
            padding=5,
            corner_radius=5
        )

        ###############
        # Save button #
        ###############

        def save_changes() -> None:
            new_name = name_ptr.get()

            # if name has changed
            if new_name != account_name:
                account = current_user.accounts.pop(account_name)

                account.rename(new_name)

                current_user.accounts[new_name] = account

            # go back
            manager.back()

        save_button = ui.TextButton(
            self,
            'Save Changes',
            ('Nunito', 25),
            (0, 550),
            command=lambda: save_changes(),
            padding=(25, 10),
            border_thickness=0,
            colors='button_accent'
        )

        ui.center(save_button)

        #################
        # Cancel button #
        #################

        cancel_button = ui.TextButton(
            self,
            'Cancel',
            ('Nunito', 20),
            (25, 660),
            command=lambda: manager.back(),
            padding=(15, 7)
        )


