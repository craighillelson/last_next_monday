"""Get the dates for the previous and next Mondays."""

from datetime import (date,
                      datetime,
                      timedelta)
from dateutil.relativedelta import relativedelta
from dateutil.rrule import MO

TODAY = datetime.now()


def adjacent_mondays(num_weeks):
    """
    Given an intenger representing the number of weeks in either direction
    (greater than zero representing Mondays in the future, less than zero
    representing Mondays in the past), calculate the date of that Monday.
    """
    return TODAY + relativedelta(weekday=MO(num_weeks))


def output_date(label, mon_date):
    """Print a specified Monday's date."""
    print(f"{label}: {mon_date.strftime('%Y-%m-%d')}")


output_date("\nToday", TODAY)

if date.today().weekday() == 0:
    next_monday_delta = 2
    last_monday_delta = -2
else:
    next_monday_delta = 1
    last_monday_delta = -1

next_monday = adjacent_mondays(next_monday_delta)
output_date("Next Monday", next_monday)
last_monday = adjacent_mondays(last_monday_delta)
output_date("Last Monday", last_monday)
print("\n")
