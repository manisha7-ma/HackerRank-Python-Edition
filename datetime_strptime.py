'''
Given Times:
Sun 10 May 2015 13:54:36 -0700

This is 1:54:36 PM in a time zone that is 7 hours behind UTC (e.g., Pacific Daylight Time).

Sun 10 May 2015 13:54:36 -0000

This is 1:54:36 PM in UTC time (offset is zero).

'''
from datetime import datetime

fmt = '%a %d %b %Y %H:%M:%S %z'

t1 = datetime.strptime('Sun 10 May 2015 13:54:36 -0700', fmt)
t2 = datetime.strptime('Sun 10 May 2015 13:54:36 -0000', fmt)

diff = abs((t1 - t2).total_seconds())
print(f"Difference in seconds: {diff}")


