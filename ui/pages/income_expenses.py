# standard library
from datetime import date as Date

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
            (50, page_title.bottom + 40, 600, 400)
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

        for i, (income, date) in enumerate(sorted(incomes, key=lambda x: x[1])):
            y = income_title.bottom + 20 + i * 38

            date_text = ui.Text(
                income_canvas,
                (0, y),
                f'{date.strftime("%m/%d/%Y")}',
                ('Nunito', 25),
                line_spacing=4
            )

            name_text = ui.Text(
                income_canvas,
                (160, y),
                income.name,
                ('Nunito', 25),
                line_spacing=4
            )

            amount_text = ui.Text(
                income_canvas,
                (400, y),
                f'${income.amount:,}',
                ('Nunito', 25),
                line_spacing=4
            )

            # ui.center(date_text, name_text, amount_text)

        add_income_button = ui.TextButton(
            income_canvas,
            'Add Income',
            ('Nunito', 25),
            (0, income_canvas.height - 50),
            command=lambda: manager.go_to('add_income'),
            padding=(15, 8),
        )

        ############
        # Expenses #
        ############

        expenses_title = ui.Text(
            self,
            (income_title.right + 250, income_title.top),
            'Next Month\'s Expenses',
            ('Nunito', 35, True, False)
        )

        expenses: list[tuple[Expense, Date]] = []

        for account in data_manager.user.accounts.values(): # type: ignore
            for expense in account.expenses:
                for date in expense.timing.get_within_next_days(30):
                    expenses.append((expense, date))

        for i, (expense, date) in enumerate(sorted(expenses, key=lambda x: x[1])):
            text = '_'*40 + f'\n| {date.strftime("%m/%d/%Y"):^14} | {expense.name:^22} | {f'${expense.amount:,}':^10} |'

            text_obj = ui.Text(
                self,
                (expenses_title.left - 70, expenses_title.bottom + 20 + i * 38),
                text,
                ('Nunito', 25),
                line_spacing=4
            )

        if expenses:
            text_obj = ui.Text(
                self,
                (expenses_title.left - 70, expenses_title.bottom + 20 + (i + 1) * 38),
                '_'*40,
                ('Nunito', 25),
                line_spacing=4
            )

        add_expense_button = ui.TextButton(
            self,
            'Add Expense',
            ('Nunito', 25),
            (850, 640),
            command=lambda: manager.go_to('add_expense'),
            padding=(15, 8),
        )

