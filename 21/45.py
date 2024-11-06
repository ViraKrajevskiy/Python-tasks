def count_integers_and_floats(input_file):
    try:
        with open(input_file, 'r') as f:
            numbers = f.read().split()
            int_count = sum(1 for num in numbers if num.isdigit())
            float_count = sum(1 for num in numbers if '.' in num)
        return int_count, float_count
    except FileNotFoundError:
        print(f"Файл {input_file} не найден. Создаю пустой файл.")
        with open(input_file, 'w') as f:
            pass
        return 0, 0

int_count, float_count = count_integers_and_floats('Text45.txt')
print(f"Integer count: {int_count}, Float count: {float_count}")
