"""Get the dates for the previous and next Mondays."""

from datetime import (date,
                      datetime)
from dateutil.relativedelta import (relativedelta,
                                    MO)


def week_from_today(int_1, int_2):
    """Find next Monday's date."""
    datetime_obj = TODAY + relativedelta(days=+int_1, weekday=MO(+int_2))
    return datetime_obj.date()


def week_ago_today():
    """Find last Monday's date."""
    datetime_obj = TODAY + relativedelta(weekday=MO(-1))
    return  datetime_obj.date()


TODAY = datetime.now()

print(f"\nlast Monday's date: {week_ago_today()}")
NEXT_MON_LABEL = "next Monday's date:"
if date.today().weekday() == 0:
    print(f"{NEXT_MON_LABEL} {week_from_today(1, 1)}\n")
else:
    print(f"{NEXT_MON_LABEL} {week_from_today(0, 1)}\n")
