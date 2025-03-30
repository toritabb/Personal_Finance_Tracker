# standard library
from datetime import date, datetime, timedelta
from typing import Literal, Optional



__all__ = 'Account', 'Timing', 'Income', 'Expense'



class Account:
    '''
    A bank account with a balance and transaction history.
    '''

    __slots__ = 'name', 'type', 'balance', 'index', 'incomes', 'expenses'

    def __init__(
            self,
            name: str = '',
            type: Literal['checking', 'savings'] = 'checking',
            balance: float = 0.0,
            index: int = 0,
            incomes: Optional[list[dict]] = None,
            expenses: Optional[list[dict]] = None
        ) -> None:

        '''
        Initialize a new bank account.

        `name`: Display name for the account

        `type`: Either 'checking' or 'savings'

        `balance`: Current balance in dollars

        `_number`: Used to order accounts

        `incomes`: List of income transactions

        `expenses`: List of expense transactions
        '''

        self.name = name
        self.type = type
        self.balance = balance
        self.index = index

        self.incomes = [Income(**income) for income in (incomes or [])]
        self.expenses = [Expense(**expense) for expense in (expenses or [])]

    def get_save_dict(self) -> dict:
        '''
        Get dictionary representation for saving to storage.
        '''

        return {
            'name': self.name,
            'type': self.type,
            'balance': self.balance,
            'index': self.index,
            'incomes': [income.get_save_dict() for income in self.incomes],
            'expenses': [expense.get_save_dict() for expense in self.expenses]
        }

    def update_balance(self) -> None:
        self.balance = 0

        # add all of the incomes
        for income in self.incomes:
            days = (date.today() - income.timing.start_date).days

            income_cost = len(income.timing.get_within_previous_days(days)) * income.amount

            self.balance += income_cost

        # add all of the expenses
        for expense in self.expenses:
            days = (date.today() - expense.timing.start_date).days

            expense_cost = len(expense.timing.get_within_previous_days(days)) * expense.amount

            self.balance -= expense_cost



class Timing:
    '''
    The start, end, and recurrence os a transaction.
    '''

    __slots__ = 'start_date', 'end_date', 'recurrence', 'days_of_month'

    def __init__(
            self,
            start_date: str,
            end_date: str,
            recurrence: Literal['never', 'weekly', 'biweekly', 'monthly'],
            days_of_month: list[int]
        ) -> None:

        self.start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
        self.end_date = datetime.strptime(end_date, "%Y-%m-%d").date() if end_date != 'None' else None

        self.recurrence = recurrence
        self.days_of_month = days_of_month

    def get_within_next_days(self, days: int) -> list[date]:
        today = date.today()
        end_date = min(today + timedelta(days=days), self.end_date) if self.end_date is not None else today + timedelta(days=days)

        match self.recurrence:
            case 'never':
                if today <= self.start_date <= end_date:
                    return [self.start_date]

                else:
                    return []

            case other:
                delta_time = timedelta(weeks=1) if other == 'weekly' else timedelta(weeks=2) if other == 'biweekly' else timedelta(days=31)

                dates: list[date] = []

                current_date = self.start_date

                while current_date < today:
                    current_date += delta_time

                while current_date <= end_date:
                    dates.append(current_date)
                    current_date += delta_time

                return dates

        return []

    def get_within_previous_days(self, days: int) -> list[date]:
        today = date.today()
        end_date = min(today + timedelta(days=days), self.end_date) if self.end_date is not None else today + timedelta(days=days)

        match self.recurrence:
            case 'never':
                if today >= self.start_date:
                    return [self.start_date]

                else:
                    return []

            case other:
                delta_time = timedelta(weeks=1) if other == 'weekly' else timedelta(weeks=2) if other == 'biweekly' else timedelta(days=31)

                dates: list[date] = []

                last_occurrence = self.start_date

                while last_occurrence + delta_time < today:
                    last_occurrence += delta_time

                while last_occurrence >= self.start_date:
                    dates.append(last_occurrence)
                    last_occurrence -= delta_time

                return dates

        return []

    def get_save_dict(self) -> dict:
        return {
            'start_date': str(self.start_date),
            'end_date': str(self.end_date),
            'recurrence': self.recurrence,
            'days_of_month': self.days_of_month,
        }



class Income:
    __slots__ = 'name', 'timing', 'amount', 'account'

    def __init__(
            self,
            name: str,
            timing: dict,
            amount: float,
            account: str,
        ) -> None:

        self.name = name
        self.timing = Timing(**timing)
        self.amount = amount
        self.account = account

    def get_save_dict(self) -> dict:
        return {
            'name': self.name,
            'timing': self.timing.get_save_dict(),
            'amount': self.amount,
            'account': self.account,
        }



class Expense:
    __slots__ = 'name', 'timing', 'amount', 'account'

    def __init__(
            self,
            name: str,
            timing: dict,
            amount: float,
            account: str,
        ) -> None:

        self.name = name
        self.timing = Timing(**timing)
        self.amount = amount
        self.account = account

    def get_save_dict(self) -> dict:
        return {
            'name': self.name,
            'timing': self.timing.get_save_dict(),
            'amount': self.amount,
            'account': self.account,
        }


