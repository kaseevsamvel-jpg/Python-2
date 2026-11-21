from datetime import datetime, date

year = int(input())
month = int(input())
day = int(input())

today = date.today()
age = today.year - year - ((today.month, today.day) < (month, day))

print(age)