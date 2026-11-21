from datetime import date

def check_date(text):
    date(int(text[:4]), int(text[4:6]), int(text[6:]))

def digit_sum(number):
    total = 0
    while number > 0:
        total += number % 10
        number //= 10
    return total

def lucky_number(text):
    number = int(text)
    while number > 9:
        number = digit_sum(number)
    return number

with open("input.txt", encoding="utf-8") as f:
    date_text = f.readline().strip()

check_date(date_text)

with open("output.txt", "w", encoding="utf-8") as f:
    f.write(str(lucky_number(date_text)))