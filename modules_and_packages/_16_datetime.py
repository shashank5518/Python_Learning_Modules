import datetime
import pytz

d = datetime.date(2016, 7, 24)  # yyyy-mm-dd no leading zeroes
print(d)

tday = datetime.date.today()
print(tday)
print(tday.year)
print(tday.day)

print(tday.weekday())  # monday = 0
print(tday.isoweekday())  # monday = 1

tdelta = datetime.timedelta(days=7)
print(tday + tdelta)
print(tday - tdelta)

new_date = tday + tdelta
print(new_date - tday)

time = datetime.time(9, 30, 45, 100000)
print(time)
print(time.hour)

new_time = datetime.datetime(2016, 7, 26, 12, 30, 45, 100000)
print(new_time)
print(new_time.date())
print(new_time.time())

tdelta = datetime.timedelta(days=7, hours=12)
print(new_time + tdelta)

dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()  # deprecated

print(dt_today)
print(dt_now)
print(dt_utcnow)

dt = datetime.datetime(2026, 7, 27, 12, 30, 45, 100000, tzinfo=pytz.UTC)
print(dt)

dt_now = datetime.datetime.now(tz=pytz.UTC)
print(dt_now)

dt_ind = dt_now.astimezone(pytz.timezone("Asia/Kolkata"))
print(dt_ind)

# for tz in pytz.all_timezones:
#     print(tz)

# strftime - datetime to string
# strptime - string to datetime
