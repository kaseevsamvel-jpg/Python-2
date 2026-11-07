def write_numbers_to_file(filename, numbers):
    with open(filename, 'w') as f:
        for number in numbers:
            f.write(f"{number}\n")

input_str = input("Введіть дійсні числа через пробіл: ")
numbers_list = [float(n) for n in input_str.split()]
    
file_path = 'numbers.txt'
write_numbers_to_file(file_path, numbers_list)
print(f"Числа успішно записані у файл {file_path}")