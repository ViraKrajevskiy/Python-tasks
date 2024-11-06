def filter_non_integer_numbers(input_file, output_file):
    try:
        with open(input_file, 'r') as f:
            numbers = f.read().split()
        with open(output_file, 'w') as out:
            out.writelines(f"{num}\n" for num in numbers if '.' in num and float(num) % 1 != 0)
    except FileNotFoundError:
        print(f"Файл {input_file} не найден. Создаю пустой файл.")
        with open(input_file, 'w') as f:
            pass

filter_non_integer_numbers('Text46.txt', 'non_integer.txt')
