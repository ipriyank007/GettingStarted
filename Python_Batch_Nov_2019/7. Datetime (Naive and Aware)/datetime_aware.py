import datetime
import pytz

india_tz = pytz.timezone('Asia/Kolkata')
london_tz = pytz.timezone('Europe/London')

time = datetime.datetime(2019, 11, 13, 4, 30, 0, tzinfo=india_tz)
london_time = time.astimezone(london_tz)
print(london_time)
