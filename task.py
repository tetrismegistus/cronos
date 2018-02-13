from datetime import date
from dateutil import relativedelta


class Task:
    def __init__(self, task_description, due_date):
        self.description = task_description
        self.due = self.parse_date(due_date)
        self.complete = False
        self.date_completed = None

    def complete_task(self):
        self.complete = True
        self.date_completed = date.today()

    def parse_date(self, due_date):
        dt = [int(d) for d in due_date.split('/')]
        if len(dt) == 2:
            y = date.today().year
        else:
            y = dt[2]
        d = dt[1]
        m = dt[0]

        return date(y, m, d)

    def get_status(self):
        if date.today() > (self.due):
            status = 'red'
        else:
            status = 'green'

        if self.complete:
            status = 'blue'

        return status


class RecurrentTask(Task):
    def __init__(self, task_description, due_date, recurrence_string):
        super().__init__(task_description, due_date)
        self.recurrence = self.set_recurrence(recurrence_string)

    def set_recurrence(self, recurrence_string):
        length = int(recurrence_string[:-1])
        unit = recurrence_string[-1]
        days, weeks, months, years = 0, 0, 0, 0
        if unit == 'w':
            weeks = length
        elif unit == 'd':
            days = length
        elif unit == 'm':
            months = length
        elif unit == 'y':
            years == length
        return relativedelta.relativedelta(days=days,
                                           weeks=weeks,
                                           months=months,
                                           years=years)

    def get_next_due(self):
        return date.today() + self.recurrence

    def complete_task(self):
        self.date_completed = date.today()
        self.due = self.get_next_due()

    def get_status(self):
        warn = self.due + self.recurrence
        if date.today() <= self.due:
            return 'green'
        elif self.due < date.today() < warn:
            return 'yellow'
        else:
            return 'red'
