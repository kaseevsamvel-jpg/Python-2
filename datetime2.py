from datetime import datetime

now = datetime.now()
row_format = now.strftime("%Y-%m-%d %H:%M:%S")
print(row_format)