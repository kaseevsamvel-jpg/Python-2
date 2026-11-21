import calendar

def get_month_calendar(year, month):
    return calendar.month(year, month)

year = int(input())
month = int(input())
print(get_month_calendar(year, month))