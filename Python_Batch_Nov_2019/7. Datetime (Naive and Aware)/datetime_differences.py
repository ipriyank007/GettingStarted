##from datetime import datetime, time, date
##
##dt = datetime.now()
##d = date.today()
##
##print(d)
##print(dt)

import datetime

date1 = datetime.datetime(2018, 12, 25)
date2 = datetime.datetime.now()

date_distance = date2 - date1  # datetime.timedelta object

td = datetime.timedelta(days=100)

todays_date = datetime.date.today()

date_after_td = todays_date - td  # + to go in future

print(date_after_td)



