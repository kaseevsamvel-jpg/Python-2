def is_float(string):
    if ',' in string:
        string = string.replace(',', '.')
    parts = string.split('.')
    if len(parts) > 2:
        return False
    if string.startswith('-'):
        return all(part.isdigit() for part in parts) or (parts[0] == '' and parts[1].isdigit())
    return all(part.isdigit() for part in parts)

def read_numbers_safely(filename):
    numbers = []
    with open(filename, 'r') as f:
        for line in f:
            clean_line = line.strip()
            if is_float(clean_line):
                numbers.append(float(clean_line.replace(',', '.')))
            else:
                print(f"Попередження: рядок '{clean_line}' не є числом і буде проігнорований.")
    return numbers

def append_stats_to_file(filename, total, maximum):
    with open(filename, 'a') as f:
        f.write(f"{total}\n")
        f.write(f"{maximum}\n")

file_path = 'numbers.txt'
numbers_list = read_numbers_safely(file_path)

if numbers_list:
    print(f"Завантажені числа: {numbers_list}")
    
    sum_of_numbers = sum(numbers_list)
    max_of_numbers = max(numbers_list)
    
    print(f"Сума: {sum_of_numbers:.2f}, Максимум: {max_of_numbers:.2f}")
    
    append_stats_to_file(file_path, sum_of_numbers, max_of_numbers)
    print(f"Статистика додана у файл {file_path}.")
else:
    print("Файл порожній або не містить коректних чисел.")