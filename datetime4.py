from datetime import datetime

first_date = datetime(2018, 8, 1)
second_date = datetime(2019, 3, 4) 

difference = second_date - first_date
print(f"Різниця між датами: {difference.days} днів")