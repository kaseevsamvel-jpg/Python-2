def load_hall_state(filename):
    hall = []
    with open(filename, 'r') as f:
        for line in f:
            hall.append([int(seat) for seat in line.split()])
    return hall

def count_free_seats(hall):
    free_seats = 0
    for row in hall:
        free_seats += row.count(0)
    return free_seats

def check_seat(hall, row_num, seat_num):
    if 1 <= row_num <= len(hall) and 1 <= seat_num <= len(hall[row_num - 1]):
        if hall[row_num - 1][seat_num - 1] == 0:
            return f"Місце (Ряд {row_num}, Місце {seat_num}) - вільне."
        else:
            return f"Місце (Ряд {row_num}, Місце {seat_num}) - зайняте."
    else:
        return "Такого місця не існує."

# Основна частина
file_path = 'hall.txt'
cinema_hall = load_hall_state(file_path)

if cinema_hall:
    print(f"Загальна кількість вільних місць: {count_free_seats(cinema_hall)}")
    
    user_row_str = input("Введіть номер ряду: ")
    user_seat_str = input("Введіть номер місця: ")
    
    if user_row_str.isdigit() and user_seat_str.isdigit():
        user_row = int(user_row_str)
        user_seat = int(user_seat_str)
        result = check_seat(cinema_hall, user_row, user_seat)
        print(result)
    else:
        print("Будь ласка, вводьте номери у вигляді цілих чисел.")