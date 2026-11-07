def read_numbers_from_file(filename):
    numbers = []
    with open(filename, 'r') as f:
        for line in f:
            numbers.append(float(line.strip()))
    return numbers

def append_stats_to_file(filename, total, maximum):
    with open(filename, 'a') as f:
        f.write(f"{total}\n")
        f.write(f"{maximum}\n")

file_path = 'numbers.txt'
numbers_list = read_numbers_from_file(file_path)

if numbers_list:
    print(f"Завантажені числа: {numbers_list}")
    
    sum_of_numbers = sum(numbers_list)
    max_of_numbers = max(numbers_list)
    
    print(f"Сума: {sum_of_numbers:.2f}, Максимум: {max_of_numbers:.2f}")
    
    append_stats_to_file(file_path, sum_of_numbers, max_of_numbers)
    print(f"Статистика додана у файл {file_path}.")
else:
    print("Файл порожній або не містить чисел.")