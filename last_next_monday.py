"""Get the dates for the previous and next Mondays."""

from datetime import datetime, timedelta
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


output_date('Today', TODAY)

next_monday = adjacent_mondays(1)
output_date('Next Monday', next_monday)

last_monday = adjacent_mondays(-1)
output_date('Last Monday', last_monday)
