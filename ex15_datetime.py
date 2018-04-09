# Date and Time in python

# Importing date, time and datetime from datetime module

from datetime import date
from datetime import time
from datetime import datetime

# Todays date
print("Todays date is ",date.today())

# Current time
print("Current time is ",datetime.time(datetime.now()))

# Weekday returns 0(monday) through 6(sunday)
print("Todays week day ",date.weekday(date.today()))

# Assigning weekday number to a variable
wd = date.weekday(date.today())

# Creating a list
days = ["mon",'tue','wed','thu','fri','sat']

# Printing the weekday number
print("Today's day number is: ",wd)

print("Which is a: " + days[wd])
