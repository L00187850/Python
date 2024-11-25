#Name: Philip Stewart
#Student Number: L00187850
#Date: 25 Nov 2024
#Purpose:Logging and Time: an introduction to time


from datetime import datetime

# Get a timestamp of the current day, month, year, and time.
current_datetime = datetime.now()

# Getting the weekday sorted. From researching I found that strftime is a method inside of pythons "Datetime" module". 
# It allows me to split datetime objects like day, week, month, year into strings based on a certain format.
weekday = datetime.now().strftime("%A")

#Getting the date sorted.
date = current_datetime.day

#Getting the time variable declared.
time = current_datetime.time()

# Getting the month variable sorted
month = datetime.now().strftime("%b")

# Getting the year sorted.
year = current_datetime.year

print("")
print("Below is the time, date, day, week and month in one line:")
print (weekday, date, month, year)
print("The time is currently: ", time)