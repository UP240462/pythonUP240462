import datetime
#1 Get the current day, month, year, hour, minute and timestamp from datetime module
nownow=datetime.datetime.now()
print("Fecha y hora actuales:",nownow)

#2 Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
formatoAhora=nownow.strftime("%m/%d/%Y, %H:%M:%S")
print("Formato de fecha y hora:", formatoAhora)

#3 Today is 5 December, 2019. Change this time string to time.
from datetime import datetime
date = "5 December, 2019"
print("dateString =", date)
dateObject = datetime.strptime(date, "%d %B, %Y")
print("dateObject =", dateObject)

#4 Calculate the time difference between now and new year.
from datetime import datetime, timedelta, date
today = date(year=2025, month=4, day=2)
newYear = date(year=2026, month=1, day=1)
time= newYear - today
print("Time left for new year: ", time)

#5 Calculate the time difference between 1 January 1970 and now.
today = date(year=2025, month=4, day=2)
old = date(year=1972, month=1, day=1)
times= today- old
print(times)

#6 Think, what can you use the datetime module for? Examples:
# Time series analysis
# To get a timestamp of any activities in an application
# Adding posts on a blog
print('se puede usar para llevar un control de diferentes zonas horarias para la aviación')