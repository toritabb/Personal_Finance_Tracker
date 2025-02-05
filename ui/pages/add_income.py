# local
import ui
from data import data_manager
from .page import Page, PageManagerBase



class AddIncomePage(Page):
    STR = 'add_income'

    def __init__(self, parent: ui.Canvas, manager: PageManagerBase) -> None:
        super().__init__(parent, manager)

        page_title = ui.Text(
            self,
            (0, 50),
            'Add Income Source',
            ('Nunito', 50, True, False)
        )
        ui.center(page_title, axis='x')

        ###################
        # ACCOUNT OPTIONS #
        ###################

        account_tab = ui.Canvas(self, (10, 175, 125, 200))

        account_title = ui.Text(
            account_tab,
            (0, 10),
            'Account',
            ('Nunito', 30)
        )

        ui.center(account_title, axis='x')

        if not data_manager.accounts:
            create_account_button = ui.TextButton(
                account_tab,
                'Create Account',
                ('Nunito', 20),
                (0, account_title.bottom + 10),
                lambda: manager.go_to('accounts'),
                size=(100, -1),
                padding=6,
                border_thickness=4,
                corner_radius=10
            )

        else:
            account_ptrs: dict[str, ui.Pointer[bool]] = {}
            account_y = account_title.bottom + 10

            for account in data_manager.accounts:
                account_label = ui.Text(
                    account_tab,
                    (0, account_y),
                    f'{account.name}',
                    ('Nunito', 20)
                )

                account_ptr = ui.Pointer(False)
                account_ptrs[account.name] = account_ptr

                account_toggle = ui.Toggle(
                    account_tab,
                    (account_label.right + 10, account_label.centery - 10),
                    21,
                    account_ptr,
                    border_thickness=4,
                    corner_radius=-1
                )

                ui.center(account_label, account_toggle, axis='x')

                account_y = account_label.bottom + 7

            list(account_ptrs.values())[0].set_no_listen(True)

            for ptr in account_ptrs.values():
                ptr.listen(lambda pp: [p.set_no_listen(False) and print(p, p.get()) for p in account_ptrs.values() if p is not pp] if pp.get() else pp.set_no_listen(True))

        ################
        # NAME OPTIONS #
        ################

        name_tab = ui.Canvas(self, (account_tab.right + 10, account_tab.top, 175, 200))

        name_title = ui.Text(
            name_tab,
            (0, 10),
            'Name',
            ('Nunito', 30)
        )

        ui.center(name_title, axis='x')

        name_ptr = ui.Pointer('')

        amount_textbox = ui.Textbox(
            name_tab,
            name_ptr,
            ('Nunito', 20),
            (0, name_title.bottom + 10),
            (150, -1),
            validation_function=lambda _: True,
            padding=6,
            border_thickness=4,
            corner_radius=10
        )

        ui.center(amount_textbox, axis='x')

        ##################
        # AMOUNT OPTIONS #
        ##################

        amount_tab = ui.Canvas(self, (name_tab.right + 10, name_tab.top, 175, 200))

        amount_title = ui.Text(
            amount_tab,
            (0, 10),
            'Amount',
            ('Nunito', 30)
        )

        ui.center(amount_title, axis='x')

        def amount_validation(text: str) -> bool:
            try:
                amount_ptr.set(float('0' + text.strip('$')))

                return True

            except:
                return False

        amount_ptr = ui.Pointer(0.0)
        amount_text_ptr = ui.Pointer('$0.0')

        amount_textbox = ui.Textbox(
            amount_tab,
            amount_text_ptr,
            ('Nunito', 20),
            (0, amount_title.bottom + 10),
            (150, -1),
            validation_function=amount_validation,
            padding=6,
            border_thickness=4,
            corner_radius=10
        )

        ui.center(amount_textbox, axis='x')

        ###############
        # DAY OPTIONS #
        ###############

        time_period_tab = ui.Canvas(self, (amount_tab.right + 10, amount_tab.top, 175, 130))

        time_period_title = ui.Text(
            time_period_tab,
            (0, 10),
            'Time Period',
            ('Nunito', 30)
        )

        time_period_ptr = ui.Pointer('') # pointer for the actual recurring value

        start_day_ptr = ui.Pointer('01')
        start_month_ptr = ui.Pointer('01')
        start_year_ptr = ui.Pointer('2025')

        def day_validation(text: str) -> bool:
            try:
                return 0 <= int('0' + text) <= 31

            except:
                return False

        def month_validation(text: str) -> bool:
            try:
                return 0 <= int('0' + text) <= 12

            except:
                return False

        def year_validation(text: str) -> bool:
            try:
                return 0 <= int('0' + text) <= 9999

            except:
                return False

        start_month_textbox = ui.Textbox(
            time_period_tab,
            start_month_ptr,
            ('Nunito', 20),
            (0, time_period_title.bottom + 10),
            (48, -1),
            validation_function=month_validation,
            padding=6,
            border_thickness=4,
            corner_radius=10,
            align='center'
        )

        start_day_textbox = ui.Textbox(
            time_period_tab,
            start_day_ptr,
            ('Nunito', 20),
            (start_month_textbox.right, start_month_textbox.top),
            (48, -1),
            validation_function=day_validation,
            padding=6,
            border_thickness=4,
            corner_radius=10,
            align='center'
        )

        start_year_textbox = ui.Textbox(
            time_period_tab,
            start_year_ptr,
            ('Nunito', 20),
            (start_day_textbox.right, start_month_textbox.top),
            (74, -1),
            validation_function=year_validation,
            padding=6,
            border_thickness=4,
            corner_radius=10,
            align='center'
        )

        # ui.center(recurring_title, recurring_toggle, axis='x')

        # recurring_option_ptrs = {'weekly': ui.Pointer(True), 'biweekly': ui.Pointer(False), 'monthly': ui.Pointer(False)}

        # def open_recurring_options() -> ui.Canvas:
        #     recurring_options_tab = ui.Canvas(recurring_tab, (0, recurring_title.bottom + 10, 175, 80))

        #     recurring_y = 0

        #     for option, option_ptr in recurring_option_ptrs.items():
        #         recurring_label = ui.Text(
        #             recurring_options_tab,
        #             (0, recurring_y),
        #             f'{option.capitalize()}',
        #             ('Nunito', 20)
        #         )

        #         recurring_toggle = ui.Toggle(
        #             recurring_options_tab,
        #             (recurring_label.right + 10, recurring_label.centery - 10),
        #             21,
        #             option_ptr,
        #             border_thickness=4,
        #             corner_radius=-1
        #         )

        #         ui.center(recurring_label, recurring_toggle, axis='x')

        #         recurring_y = recurring_label.bottom + 7

        #     return recurring_options_tab

        # recurring_options_tab = ui.Pointer(None)

        # show_recurring_options_ptr.listen(lambda pointer: recurring_options_tab.set(open_recurring_options()) if pointer.get() else recurring_options_tab.get().close()) # type: ignore

        # for ptr in recurring_option_ptrs.values():
        #     ptr.listen(lambda pp: [p.set_no_listen(False) and print(p, p.get()) for p in recurring_option_ptrs.values() if p is not pp] if pp.get() else pp.set_no_listen(True))

        # for option, ptr in recurring_option_ptrs.items():
        #     ptr.listen(lambda _: recurring_ptr.set(option))

        #####################
        # RECURRING OPTIONS #
        #####################

        recurring_tab = ui.Canvas(self, (time_period_tab.right + 10, time_period_tab.top, 175, 130))

        recurring_title = ui.Text(
            recurring_tab,
            (0, 10),
            'Recurring',
            ('Nunito', 30)
        )

        recurring_ptr = ui.Pointer('') # pointer for the actual recurring value

        show_recurring_options_ptr = ui.Pointer(False) # pointer whether or not to show recurring
        show_recurring_options_ptr.listen(lambda ptr: recurring_ptr.set('never') if not ptr.get() else None)

        recurring_toggle = ui.Toggle(
            recurring_tab,
            (recurring_title.right + 10, recurring_title.centery - 12),
            25,
            show_recurring_options_ptr,
            border_thickness=4,
            corner_radius=-1
        )

        ui.center(recurring_title, recurring_toggle, axis='x')

        recurring_option_ptrs = {'weekly': ui.Pointer(True), 'biweekly': ui.Pointer(False), 'monthly': ui.Pointer(False)}

        def open_recurring_options() -> ui.Canvas:
            recurring_options_tab = ui.Canvas(recurring_tab, (0, recurring_title.bottom + 10, 175, 80))

            recurring_y = 0

            for option, option_ptr in recurring_option_ptrs.items():
                recurring_label = ui.Text(
                    recurring_options_tab,
                    (0, recurring_y),
                    f'{option.capitalize()}',
                    ('Nunito', 20)
                )

                recurring_toggle = ui.Toggle(
                    recurring_options_tab,
                    (recurring_label.right + 10, recurring_label.centery - 10),
                    21,
                    option_ptr,
                    border_thickness=4,
                    corner_radius=-1
                )

                ui.center(recurring_label, recurring_toggle, axis='x')

                recurring_y = recurring_label.bottom + 7

            return recurring_options_tab

        recurring_options_tab = ui.Pointer(None)

        show_recurring_options_ptr.listen(lambda pointer: recurring_options_tab.set(open_recurring_options()) if pointer.get() else recurring_options_tab.get().close()) # type: ignore

        for ptr in recurring_option_ptrs.values():
            ptr.listen(lambda pp: [p.set_no_listen(False) and print(p, p.get()) for p in recurring_option_ptrs.values() if p is not pp] if pp.get() else pp.set_no_listen(True))

        for option, ptr in recurring_option_ptrs.items():
            ptr.listen(lambda _: recurring_ptr.set(option))

        ###############
        # back button #
        ###############

        back_button = ui.TextButton(
            self,
            'Back',
            ('Nunito', 20),
            (25, 660),
            command=lambda: manager.back(),
            padding=(15, 7),
            border_thickness=4
        )

