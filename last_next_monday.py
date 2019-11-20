""" __doc__ """

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from dateutil.rrule import MO

TODAY = datetime.now()

def adjacent_mondays(a, b):
    a = TODAY + relativedelta(weekday=MO(b))
    return a


def output_date(a, b):
    print(f"{a}: {b.strftime('%Y-%m-%d')}")


output_date('Today', TODAY)

last_monday = adjacent_mondays('last_monday', +1)
output_date('Last Monday', last_monday)

next_monday = adjacent_mondays('next_monday', -1)
output_date('Last Monday', next_monday)
