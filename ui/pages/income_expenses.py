# standard library
from datetime import date as Date

from pygame import Color

# local
import ui
from data import Income, Expense, data_manager
from ui.theme import OLD_PAPER, DESERT_TAN
from .page import Page, PageManagerBase
from .header import HeaderPage



class IncomeExpensesPage(Page):
    STR = 'income_expenses'

    def __init__(self, parent: ui.Canvas, manager: PageManagerBase) -> None:
        super().__init__(parent, manager)

        header = HeaderPage(self, manager)

        page_title = ui.Text(
            self,
            (25, header.bottom + 25),
            'Income & Expenses',
            ('Nunito', 50, True, False)
        )

        ui.center(page_title, axis='x')

        ###############
        # Positioning #
        ###############

        width = 580
        height = 450

        padding = 15
        date_x = 0 + padding
        description_x = 100 + padding
        account_x = 300 + padding
        amount_x = 450 + padding


        ##########
        # Income #
        ##########

        income_canvas = ui.Canvas(
            self,
            (0, page_title.bottom + 30, width, height),
            fill_color=DESERT_TAN
        )

        income_title = ui.Text(
            income_canvas,
            (0, padding),
            'Next Month\'s Income',
            ('Nunito', 35, True, False)
        )

        ui.center(income_title)

        incomes: list[tuple[Income, Date]] = []

        for account in data_manager.user.accounts.values(): # type: ignore
            for income in account.incomes:
                for date in income.timing.get_within_next_days(30):
                    incomes.append((income, date))

        if not incomes:
            no_income_text = ui.Text(
                income_canvas,
                (0, income_title.bottom + 20),
                f'No income in the next month',
                ('Nunito', 25)
            )

            ui.center(no_income_text)

        else:
            date_label = ui.Text(
                income_canvas,
                (date_x, income_title.bottom + 20),
                'Date',
                ('Nunito', 20, True, False)
            )

            description_label = ui.Text(
                income_canvas,
                (description_x, date_label.top),
                'Description',
                ('Nunito', 20, True, False)
            )

            account_label = ui.Text(
                income_canvas,
                (account_x, date_label.top),
                'Account',
                ('Nunito', 20, True, False)
            )

            amount_label = ui.Text(
                income_canvas,
                (amount_x, date_label.top),
                'Amount',
                ('Nunito', 20, True, False)
            )

            for i, (income, date) in enumerate(sorted(incomes, key=lambda x: x[1])):
                y = date_label.bottom + 20 + i * 28

                date_text = ui.Text(
                    income_canvas,
                    (date_x, y),
                    f'{date.strftime("%m/%d")}',
                    ('Nunito', 20)
                )

                description_text = ui.Text(
                    income_canvas,
                    (description_x, y),
                    income.name,
                    ('Nunito', 20)
                )

                account_text = ui.Text(
                    income_canvas,
                    (account_x, y),
                    income.account,
                    ('Nunito', 20)
                )

                amount_text = ui.Text(
                    income_canvas,
                    (amount_x, y),
                    f'${income.amount:,.2f}',
                    ('Nunito', 20)
                )

        add_income_button = ui.TextButton(
            income_canvas,
            'Add Income',
            ('Nunito', 25),
            (0, income_canvas.height - padding - 42),
            command=lambda: manager.go_to('add_income'),
            padding=(25, 10),
            border_thickness=0,
            colors='button_accent'
        )

        ui.center(add_income_button)

        ############
        # Expenses #
        ############

        expenses_canvas = ui.Canvas(
            self,
            (income_canvas.right + 40, income_canvas.top, width, height),
            fill_color=DESERT_TAN
        )

        expenses_title = ui.Text(
            expenses_canvas,
            (0, padding),
            'Next Month\'s Expenses',
            ('Nunito', 35, True, False)
        )

        ui.center(expenses_title)

        expenses: list[tuple[Expense, Date]] = []

        for account in data_manager.user.accounts.values(): # type: ignore
            for expense in account.expenses:
                for date in expense.timing.get_within_next_days(30):
                    expenses.append((expense, date))

        if not expenses:
            no_expenses_text = ui.Text(
                expenses_canvas,
                (0, expenses_title.bottom + 20),
                f'No expenses in the next month',
                ('Nunito', 25)
            )

            ui.center(no_expenses_text)

        else:
            date_label = ui.Text(
                expenses_canvas,
                (date_x, expenses_title.bottom + 20),
                'Date',
                ('Nunito', 20, True, False)
            )

            description_label = ui.Text(
                expenses_canvas,
                (description_x, date_label.top),
                'Description',
                ('Nunito', 20, True, False)
            )

            account_label = ui.Text(
                expenses_canvas,
                (account_x, date_label.top),
                'Account',
                ('Nunito', 20, True, False)
            )

            amount_label = ui.Text(
                expenses_canvas,
                (amount_x, date_label.top),
                'Amount',
                ('Nunito', 20, True, False)
            )

            for i, (expense, date) in enumerate(sorted(expenses, key=lambda x: x[1])):
                y = date_label.bottom + 20 + i * 28

                date_text = ui.Text(
                    expenses_canvas,
                    (date_x, y),
                    f'{date.strftime("%m/%d")}',
                    ('Nunito', 20)
                )

                description_text = ui.Text(
                    expenses_canvas,
                    (description_x, y),
                    expense.name,
                    ('Nunito', 20)
                )

                account_text = ui.Text(
                    expenses_canvas,
                    (account_x, y),
                    expense.account,
                    ('Nunito', 20)
                )

                amount_text = ui.Text(
                    expenses_canvas,
                    (amount_x, y),
                    f'${expense.amount:,.2f}',
                    ('Nunito', 20)
                )

        add_expense_button = ui.TextButton(
            expenses_canvas,
            'Add Expense',
            ('Nunito', 25),
            (0, expenses_canvas.height - padding - 42),
            command=lambda: manager.go_to('add_expense'),
            padding=(25, 10),
            border_thickness=0,
            colors='button_accent'
        )

        ui.center(add_expense_button)

        ui.center(income_canvas, expenses_canvas)

