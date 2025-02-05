# standard library
from datetime import date, datetime, timedelta
from typing import Literal, Optional



__all__ = 'Account', 'Timing', 'Income', 'Expense'



class Account:
    __slots__ = 'username', 'password', 'name', 'type', 'balance', 'past_incomes', 'past_expenses', 'incomes', 'expenses'

    def __init__(self, username: str, password: str, name: str = '', type: Literal['checking', 'savings'] = 'checking', balance: int = 0, incomes: list[dict] | None = None, expenses: list[dict] | None = None) -> None:
        self.username = username
        self.password = password
        self.name = name
        self.type = type
        self.balance = balance
        self.incomes = [Income(**income) for income in (incomes or [])]
        self.expenses = [Expense(**expense) for expense in (expenses or [])]
    def get_save_dict(self) -> dict:
        return {
            'username': self.username,
            'password': self.password,
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
                future_weekly_dates: list[date] = []

                current_date = self.start_date

                while current_date < today:
                    current_date += timedelta(weeks=1)

                while current_date <= end_date:
                    future_weekly_dates.append(current_date)
                    current_date += timedelta(weeks=1)

                return future_weekly_dates

            case 'biweekly':
                future_biweekly_dates: list[date] = []

                current_date = self.start_date

                while current_date < today:
                    current_date += timedelta(weeks=2)

                while current_date <= end_date:
                    future_biweekly_dates.append(current_date)
                    current_date += timedelta(weeks=2)

                return future_biweekly_dates

            case 'monthly':
                future_monthly_dates: list[date] = []

                current_date = today

                while current_date <= end_date:
                    for day in sorted(self.days_of_month):
                        try:
                            next_date = current_date.replace(day=day)
                        except ValueError:
                            continue

                        if next_date >= today and next_date <= end_date:
                            future_monthly_dates.append(next_date)

                    current_date = (current_date.replace(day=1) + timedelta(days=32)).replace(day=1)

                return future_monthly_dates
            
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
                weekly_dates: list[date] = []

                last_occurrence = self.start_date

                while last_occurrence + timedelta(weeks=1) < today:
                    last_occurrence += timedelta(weeks=1)

                while last_occurrence >= self.start_date:
                    weekly_dates.append(last_occurrence)
                    last_occurrence -= timedelta(weeks=1)

                return weekly_dates

            case 'biweekly':
                biweekly_dates: list[date] = []

                last_occurrence = self.start_date

                while last_occurrence + timedelta(weeks=2) < today:
                    last_occurrence += timedelta(weeks=2)

                while last_occurrence >= self.start_date:
                    biweekly_dates.append(last_occurrence)
                    last_occurrence -= timedelta(weeks=2)

                return biweekly_dates

            case 'monthly':
                past_monthly_dates: list[date] = []

                current_date = today

                while current_date >= self.start_date:
                    for day in sorted(self.days_of_month, reverse=True):
                        try:
                            prev_date = current_date.replace(day=day)
                        except ValueError:
                            continue

                        if self.start_date <= prev_date < today:
                            past_monthly_dates.append(prev_date)

                    current_date = (current_date.replace(day=1) - timedelta(days=1)).replace(day=1)

                return sorted(past_monthly_dates, reverse=True)
            
        return []

    def get_save_dict(self) -> dict:
        return {
            'start_date': str(self.start_date),
            'end_date': str(self.end_date),
            'recurrence': self.recurrence,
            'days_of_month': self.days_of_month,
        }



class Income:
    __slots__ = 'name', 'timing', 'amount'

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
    __slots__ = 'name', 'timing', 'amount'

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


