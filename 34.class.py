## date only


import datetime
from datetime import date
tod=date.today()
print(tod)
da=tod.day
mo=tod.month
yr=tod.year

print("Today's date is {0} and Month is {1} and Year is {2}".format(da,mo,yr))

# =====================================================================================

import datetime
from datetime import date
from datetime import timedelta
print (dir(date))
tod=date.today()
print (tod)
print (dir(tod))
tod_date=tod.day
currentmonth=tod.month
current_year=tod.year
print ("Current date is {0}\nToday date is {1}\nCurrent Month is {2}\nCurrent year is {3}".format(tod,tod_date,currentmonth,current_year))
usrinput=int(input("Enter the Number to days for forward and backward\n"))
backwarddate=tod-timedelta(days=usrinput)
forwarddate=tod+timedelta(days=usrinput)
print ("Forward date is {0}\nBackwarddate is {1}".format(forwarddate,backwarddate))


print(tod.isoformat())
print(tod.isoweekday())
print(tod.weekday())