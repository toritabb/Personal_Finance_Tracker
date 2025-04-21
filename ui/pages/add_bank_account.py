# standard library
from typing import Optional

# local
import ui
from data import Account, data_manager
from .page import Page, PageManagerBase
from .header import HeaderPage



class AddBankAccountPage(Page):
    STR = 'add_account'

    def __init__(self, parent: ui.Canvas, manager: PageManagerBase) -> None:
        super().__init__(parent, manager)

        # go to log in page if no user is logges in
        current_user = data_manager.user

        if current_user is None:
            print('Error: No user logged in')

            manager.go_to('login')

            return

        #########
        # Title #
        #########

        title_label = ui.Text(
            self,
            (50, 50),
            f'Add new bank account',
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

        name_ptr = ui.Pointer('My Account')
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

        balance_ptr = ui.Pointer(0.0)
        balance_text_ptr = ui.Pointer('$0.00')

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
            (0, name_box.bottom + 90),
            f'Account type',
            ('Nunito', 25)
        )

        checking_label = ui.Text(
            self,
            (type_label.left + 20, type_label.bottom + 15),
            f'Checking',
            ('Nunito', 20)
        )

        checking_ptr = ui.Pointer(True)
        checking_toggle = ui.Toggle(
            self,
            (checking_label.right + 10, checking_label.centery - 10),
            21,
            checking_ptr,
        )

        savings_label = ui.Text(
            self,
            (checking_label.left + 5, checking_label.bottom + 10),
            f'Savings',
            ('Nunito', 20)
        )

        savings_ptr = ui.Pointer(False)
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

        #################
        # Create button #
        #################

        def save_changes() -> None:
            name = name_ptr.get()
            type = 'savings' if savings_ptr.get() else 'checking'
            starting_balance = balance_ptr.get()

            current_user.add_account(name, type, starting_balance)

            # go back
            manager.back()

        create_button = ui.TextButton(
            self,
            'Create Account',
            ('Nunito', 25),
            (0, savings_label.bottom + 90),
            command=lambda: save_changes(),
            padding=(25, 10),
            border_thickness=0,
            colors='button_accent'
        )

        ui.center(create_button)

        ###############
        # Back button #
        ###############

        back_button = ui.TextButton(
            self,
            'Back',
            ('Nunito', 20),
            (25, 660),
            command=lambda: manager.back(),
            padding=(15, 7)
        )

