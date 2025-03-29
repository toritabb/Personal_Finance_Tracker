# standard library
from datetime import date as Date

from pygame import Color

# local
import ui
from data import Income, Expense, data_manager
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

        ##########
        # Income #
        ##########

        income_canvas = ui.Canvas(
            self,
            (0, page_title.bottom + 40, 550, 400),
            fill_color=Color(255, 0, 0)
        )

        income_title = ui.Text(
            income_canvas,
            (0, 0),
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

        for i, (income, date) in enumerate(sorted(incomes, key=lambda x: x[1])):
            y = income_title.bottom + 20 + i * 38

            date_text = ui.Text(
                income_canvas,
                (0, y),
                f'{date.strftime("%m/%d/%Y")}',
                ('Nunito', 25)
            )

            name_text = ui.Text(
                income_canvas,
                (160, y),
                income.name,
                ('Nunito', 25)
            )

            amount_text = ui.Text(
                income_canvas,
                (425, y),
                f'${income.amount:,}',
                ('Nunito', 25)
            )

            # ui.center(date_text, name_text, amount_text)

        add_income_button = ui.TextButton(
            income_canvas,
            'Add Income',
            ('Nunito', 25),
            (0, income_canvas.height - 50),
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
            (income_canvas.right + 50, page_title.bottom + 40, 550, 400),
            fill_color=Color(255, 0, 0)
        )

        expenses_title = ui.Text(
            expenses_canvas,
            (0, 0),
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

        for i, (expense, date) in enumerate(sorted(expenses, key=lambda x: x[1])):
            y = expenses_title.bottom + 20 + i * 38

            date_text = ui.Text(
                expenses_canvas,
                (0, y),
                f'{date.strftime("%m/%d/%Y")}',
                ('Nunito', 25),
                line_spacing=4
            )

            name_text = ui.Text(
                expenses_canvas,
                (160, y),
                expense.name,
                ('Nunito', 25),
                line_spacing=4
            )

            amount_text = ui.Text(
                expenses_canvas,
                (425, y),
                f'${expense.amount:,}',
                ('Nunito', 25),
                line_spacing=4
            )

        add_expense_button = ui.TextButton(
            expenses_canvas,
            'Add Expense',
            ('Nunito', 25),
            (0, income_canvas.height - 50),
            command=lambda: manager.go_to('add_expense'),
            padding=(25, 10),
            border_thickness=0,
            colors='button_accent'
        )

        ui.center(add_expense_button)

        ui.center(income_canvas, expenses_canvas)

