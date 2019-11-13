##12th Nov 2019
##
##12 days

import datetime

user_date = input('Enter the date: ')

user_date_obj = datetime.datetime.strptime(user_date, '%dth %b %Y')

month = user_date_obj.month
year = user_date_obj.year
start_month = datetime.datetime(year, month, 1)

##start_date = user_date_obj.replace(day=1)
print(user_date_obj - start_month)



