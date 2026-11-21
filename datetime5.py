from datetime import datetime, time

now = datetime.now()
print(f"Current date and time: {now}")
print(f"Current year: {now.year}")
print(f"Month of year: {now.month}")
print(f"Week number of the year: {now.isocalendar()[1]}")
print(f"Weekday of the week: {now.weekday()}")
print(f"Day of the year: {now.timetuple().tm_yday}")
print(f"Day of the month: {now.day}")
print(f"Day of the week: {now.weekday()}")