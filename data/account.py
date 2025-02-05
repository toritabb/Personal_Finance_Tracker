# standard library
from datetime import date, datetime, timedelta
from typing import Literal, Optional



__all__ = 'Account', 'Timing', 'Income', 'Expense'



class Account:
    __slots__ = 'name', 'type', 'balance', 'past_incomes', 'past_expenses', 'incomes', 'expenses'

    def __init__(self, name: str, type: Literal['checking', 'savings'], balance: int, incomes: list[dict], expenses: list[dict]) -> None:
        self.name = name
        self.type = type

        self.balance = balance

        self.incomes = [Income(**income) for income in incomes]
        self.expenses = [Expense(**expense) for expense in expenses]

    def get_save_dict(self) -> dict:
        return {
            'name': self.name,
            'type': self.type,
            'balance': self.balance,
            'incomes': [income.get_save_dict() for income in self.incomes],
            'expenses': [expense.get_save_dict() for expense in self.expenses],
        }



class Timing:
    __slots__ = 'start_date', 'end_date', 'recurrence', 'days_of_month'

    def __init__(self, start_date: str, end_date: str, recurrence: Literal['never', 'weekly', 'biweekly', 'monthly'], days_of_month: list[int]) -> None:
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

            case 'weekly':
                dates: list[date] = []

                current_date = self.start_date

                while current_date < today:
                    current_date += timedelta(weeks=1)

                while current_date <= end_date:
                    dates.append(current_date)
                    current_date += timedelta(weeks=1)

                return dates

            case 'biweekly':
                dates: list[date] = []

                current_date = self.start_date

                while current_date < today:
                    current_date += timedelta(weeks=2)

                while current_date <= end_date:
                    dates.append(current_date)
                    current_date += timedelta(weeks=2)

                return dates

            case 'monthly':
                dates: list[date] = []

                current_date = today

                while current_date <= end_date:
                    for day in sorted(self.days_of_month):
                        try:
                            next_date = current_date.replace(day=day)
                        except ValueError:
                            continue

                        if next_date >= today and next_date <= end_date:
                            dates.append(next_date)

                    current_date = (current_date.replace(day=1) + timedelta(days=32)).replace(day=1)

                return dates
            
        return []

    def get_within_previous_days(self, days: int) -> list[date]:
        today = date.today()
        end_date = min(today + timedelta(days=days), self.end_date) if self.end_date is not None else today + timedelta(days=days)

        match self.recurrence:
            case 'never':
                if today <= self.start_date <= end_date:
                    return [self.start_date]
                
                else:
                    return []

            case 'weekly':
                dates: list[date] = []

                last_occurrence = self.start_date

                while last_occurrence + timedelta(weeks=1) < today:
                    last_occurrence += timedelta(weeks=1)

                while last_occurrence >= self.start_date:
                    dates.append(last_occurrence)
                    last_occurrence -= timedelta(weeks=1)

                return dates

            case 'biweekly':
                dates: list[date] = []

                last_occurrence = self.start_date

                while last_occurrence + timedelta(weeks=2) < today:
                    last_occurrence += timedelta(weeks=2)

                while last_occurrence >= self.start_date:
                    dates.append(last_occurrence)
                    last_occurrence -= timedelta(weeks=2)

                return dates

            case 'monthly':
                dates: list[date] = []

                current_date = today

                while current_date >= self.start_date:
                    for day in sorted(self.days_of_month, reverse=True):
                        try:
                            prev_date = current_date.replace(day=day)
                        except ValueError:
                            continue

                        if self.start_date <= prev_date < today:
                            dates.append(prev_date)

                    current_date = (current_date.replace(day=1) - timedelta(days=1)).replace(day=1)

                return sorted(dates, reverse=True)
            
        return []

    def get_save_dict(self) -> dict:
        return {
            'start_date': str(self.start_date),
            'end_date': str(self.end_date),
            'recurrence': self.recurrence,
            'days_of_month': self.days_of_month,
        }



class Income:
    __slots__ = 'name', 'timing', 'amount', 'recieved'

    def __init__(self, name: str, timing: dict, amount: int) -> None:
        self.name = name
        self.timing = Timing(**timing)
        self.amount = amount

    def get_save_dict(self) -> dict:
        return {
            'name': self.name,
            'timing': self.timing.get_save_dict(),
            'amount': self.amount,
        }



class Expense:
    __slots__ = 'name', 'timing', 'amount', 'paid'

    def __init__(self, name: str, timing: dict, amount: int) -> None:
        self.name = name
        self.timing = Timing(**timing)
        self.amount = amount

    def get_save_dict(self) -> dict:
        return {
            'name': self.name,
            'timing': self.timing.get_save_dict(),
            'amount': self.amount,
        }


