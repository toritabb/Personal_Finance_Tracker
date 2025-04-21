# standard library
from typing import Optional

# local
import ui
from data import data_manager
from ui.theme import DESERT_TAN
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
        # Account Name #
        ################

        name_label = ui.Text(
            self,
            (0, title_label.bottom + 90),
            f'Account name',
            ('Nunito', 25)
        )

        name_ptr = ui.Pointer(account.name)
        name_box = ui.Textbox(
            self,
            name_ptr,
            ('Nunito', 20),
            (name_label.left, name_label.bottom + 10),
            (300, -1),
            padding=5,
            corner_radius=5
        )

        ####################
        # Starting Balance #
        ####################

        balance_title = ui.Text(
            self,
            (name_box.right + 75, name_label.top),
            'Starting balance',
            ('Nunito', 25)
        )

        def balance_validation(text: str) -> Optional[str]:
            try:
                num = text[1:].replace(',', '').replace('.', '').rjust(3, '0')

                decimal = num[:-2] + '.' + num[-2:]

                value = float(decimal)

                balance_ptr.set(value)

                return f'${value:,.2f}'

            except:
                return None

        balance_ptr = ui.Pointer(account.starting_balance)
        balance_text_ptr = ui.Pointer(f'${account.starting_balance:,.2f}')

        balance_textbox = ui.Textbox(
            self,
            balance_text_ptr,
            ('Nunito', 20),
            (balance_title.left, balance_title.bottom + 10),
            (150, -1),
            validation_function=balance_validation,
            padding=5,
            corner_radius=5
        )

        ################
        # Account Type #
        ################

        type_label = ui.Text(
            self,
            (0, name_box.bottom + 70),
            f'Account type',
            ('Nunito', 25)
        )

        checking_label = ui.Text(
            self,
            (type_label.left, type_label.bottom + 15),
            f'Checking',
            ('Nunito', 20)
        )

        checking_ptr = ui.Pointer(account.type == 'checking')
        checking_toggle = ui.Toggle(
            self,
            (checking_label.right + 10, checking_label.centery - 10),
            21,
            checking_ptr,
        )

        savings_label = ui.Text(
            self,
            (type_label.left, checking_label.bottom + 10),
            f'Savings',
            ('Nunito', 20)
        )

        savings_ptr = ui.Pointer(account.type == 'savings')
        savings_toggle = ui.Toggle(
            self,
            (savings_label.right + 10, savings_label.centery - 10),
            21,
            savings_ptr,
        )

        checking_ptr.listen(lambda pp: savings_ptr.set_no_listen(not pp.get()))
        savings_ptr.listen(lambda pp: checking_ptr.set_no_listen(not pp.get()))

        ui.center(name_label, name_box, balance_title, balance_textbox)
        ui.center(type_label, checking_label, checking_toggle, savings_label, savings_toggle)

        ###############
        # Save button #
        ###############

        def save_changes() -> None:
            new_name = name_ptr.get()

            # if name has changed
            if new_name != account_name:
                current_user.accounts.pop(account_name)

                account.rename(new_name)

                current_user.accounts[new_name] = account

            # if type has changed
            account.type = 'checking' if checking_ptr.get() else 'savings' if savings_ptr.get() else account.type

            # if starting balance has changed
            account.starting_balance = balance_ptr.get()

            # go back
            manager.back()

        save_button = ui.TextButton(
            self,
            'Save Changes',
            ('Nunito', 25),
            (0, savings_label.bottom + 105),
            command=lambda: save_changes(),
            padding=(25, 10),
            border_thickness=0,
            colors='button_accent'
        )

        ui.center(save_button)

        #################
        # Delete button #
        #################

        def delete_account():
            # delete
            current_user.remove_account(account.name)

            # go back
            manager.back()

        def confirm_delete():
            confirm_page = ui.Canvas(self, (0, 0, 450, 200), DESERT_TAN)

            ui.center(confirm_page, axis='xy')

            are_you_sure_text = ui.Text(
                confirm_page,
                (0, 22),
                f'Are you sure you want\nto delete "{account_name}"',
                ('Nunito', 30, True, False)
            )

            ui.center(are_you_sure_text)

            delete_button = ui.TextButton(
                confirm_page,
                'Delete',
                ('Nunito', 25),
                (0, are_you_sure_text.bottom + 40),
                command=lambda: delete_account(),
                padding=(20, 10),
                border_thickness=0,
                colors='button_accent'
            )

            cancel_button = ui.TextButton(
                confirm_page,
                'Cancel',
                ('Nunito', 25),
                (delete_button.right + 50, delete_button.top),
                command=lambda: confirm_page.close(),
                padding=(20, 10),
                border_thickness=0,
                colors='button_accent'
            )

            ui.center(delete_button, cancel_button)

        delete_button = ui.TextButton(
            self,
            'Delete Account',
            ('Nunito', 20),
            (0, save_button.bottom + 60),
            command=lambda: confirm_delete(),
            padding=(25, 10),
            border_thickness=0,
            colors='button_accent'
        )

        ui.center(delete_button)

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


