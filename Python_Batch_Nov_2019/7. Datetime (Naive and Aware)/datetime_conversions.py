import datetime

dt = datetime.datetime.now()

dt_str = dt.strftime("%b' %d, %Y %H:%M:%S")

'''
%d - date 1, 2, 3
%m - month number 10, 11, 12
%b - partial month name jan, oct, nov, dec
%B - Full month
%y - last two digits of the year
%Y - full year

'''


##print(dt_str)

date_str = "Nov' 13, 2019"

date_obj = datetime.datetime.strptime(date_str, "%b' %d, %Y")
print(date_obj.date())

