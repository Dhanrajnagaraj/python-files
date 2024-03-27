## date and time 

import datetime
from datetime import datetime
print(datetime.today())
cdt=datetime.now()
print(cdt)
cm=cdt.minute
ch=cdt.hour
cs=cdt.second
cd=cdt.day
cmo=cdt.month
cy=cdt.year
print("Current minute is {0}\nCurrent hour is {1}\nCurrent second is {2}\nCurrent day is {3}\nCurrent month is {4}\nCurrent year is {5}".format(cm,ch,cs,cd,cmo,cy))

#===============================================================================

import datetime
from datetime import datetime
from datetime import timedelta
#print (datetime.today())
curr_dat_time=datetime.now()
curr_time=curr_dat_time
curr_hr=curr_dat_time.hour
curr_min=curr_dat_time.minute
curr_sec=curr_dat_time.second
curr_day=curr_dat_time.day
curr_month=curr_dat_time.month
curre_year=curr_dat_time.year
print ("Current datetime is {0}\ncurrent time is {0}\ncurrent hour is {1}\ncurrent minute is {2}\ncurrent second is {3}".format(curr_time,curr_hr,curr_min,curr_sec))
hour_forw=int(input("Enter the forward or backward hours/minutes"))
print (curr_dat_time+timedelta(hours=hour_forw))
print (curr_dat_time-timedelta(hours=hour_forw))
print (curr_dat_time.strftime("%H:%M:%S %d:%Y:%m"))

#==================================================================================

import datetime
from datetime import date as da
from datetime import timedelta
k=da.today()
for_back=int(input("Enter the interger for forward/backward\n"))
usrinput=input("Enter '1'  for current date\n'2' for formwated date innformat date-monthname-year\n'3' for forward date\n'4' for bakward date\n'5' for current date forward back date")
if (usrinput == "1"):
    print ("Current date is {0}".format(k))
elif (usrinput == "2"):
    print (k.strftime("%d-%B-%y"))
elif (usrinput == "3"):
    print (k+timedelta(days=for_back))
elif (usrinput == "4"):
    print (k-timedelta(days=for_back))
elif (usrinput == "5"):
    print ("Current date is {0}\n formated date is {1}\nforwarddate is {2}\nbackwarddate is {3}".format(k,k.strftime("%d-%B-%y"),k+timedelta(days=for_back),k-timedelta(days=for_back)))
