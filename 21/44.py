
def count_integers(input_file):
    try:
        with open(input_file, 'r') as f:
            numbers = list(map(int, f.read().split()))
        return len(numbers), sum(numbers)
    except FileNotFoundError:
        print(f"Файл {input_file} не найден. Создаю пустой файл.")
        with open(input_file, 'w') as f:
            pass
        return 0, 0

count, total = count_integers('Text44.txt')
print(f"Count: {count}, Total: {total}")
