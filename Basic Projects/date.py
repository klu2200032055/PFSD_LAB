import calendar
import datetime
import time
from datetime import timedelta



#print(time.time())
print('-----')
print(time.asctime())
print('-----')
d_o=datetime.datetime.now()
print(d_o)
print('-----')
print("Year: ",d_o.year)

s=calendar.prcal(2024)
s1=calendar.isleap(2003)
s2=calendar.month(2003,11)
print(s)
print('-----')
print(s1)
print('-----')
print(s2)
print('-----')

x=datetime.datetime.now()
print(x+timedelta(days=11))

print('-----')

import pytz
from datetime import datetime
print('Euro')
time1=pytz.timezone('Europe/Berlin')
print(datetime.now(time1))