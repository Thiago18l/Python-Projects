from datetime import datetime, timedelta, timezone

JST = timezone(timedelta(hours=+9))

dt = datetime(2020, 1, 1, 12, 0, 0, tzinfo=JST)
print(dt)

print(dt.tzname())
dt = datetime(2020, 1, 1, 12, 0, 0, tzinfo=timezone(timedelta(hours=-3), 'JST'))
print(dt.tzname)

# Date differences

from datetime import datetime, timedelta
now = datetime.now()
then = datetime(2020, 4, 1)

delta = now - then

print(delta.days)

# n days after date:

def get_n_days_after(date_format="%d %B %Y", add_days=120):
    date_n_days_after = datetime.now() + timedelta(days=add_days)
    return date_n_days_after.strftime(date_format)

# n days before date:

def get_n_days_before(date_format="%d %B %Y", days_before=120):
    date_n_days_ago = datetime.now() - timedelta(days=days_before)
    return date_n_days_ago

print(get_n_days_after())
print(get_n_days_before())