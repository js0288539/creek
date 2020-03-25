# Think Python 2e
# Exercise 5.1

import time

sec_total = time.time()

minutes_float = (sec_total / 60) # total minutes as a floating point
minutes_total = (sec_total // 60) # total minutes as an integer
seconds_actual = (sec_total % 60) # date/time number of seconds as a floating point, in seconds

hours_float = (minutes_total / 60) # total hours as a floating point
hours_total = (minutes_total // 60) # total hours as an integer
minutes_actual = (minutes_total % 60) # date/time number of minutes as a floating point, in minutes

days_float = (hours_total / 24) # total days as a floating point
days_total = (hours_total // 24) # total days as an integer
hours_actual = (hours_total % 24) # date/time number of hours as a floating point, in hours

dt_hours = int(hours_actual)
dt_minutes = int(minutes_actual)
dt_seconds = int(seconds_actual)

string_hours = str(dt_hours)
string_minutes = str(dt_minutes)
string_seconds = str(dt_seconds)

print("Current time (GMT):  " + string_hours + ":" + string_minutes + ":" + string_seconds)
print("Days since epoch:    " + str(int(days_total)) + " days")
