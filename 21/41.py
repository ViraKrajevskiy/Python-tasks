def create_two_column_file_left(file1, file2, output_file):
    try:
        with open(file1, 'r') as f1, open(file2, 'r') as f2:
            with open(output_file, 'w') as out:
                for num1, num2 in zip(f1, f2):
                    out.write(f"{num1.strip():<30} l {num2.strip():<30} l\n")
    except FileNotFoundError as e:
        print(f"Файл не найден: {e.filename}. Создаю пустые файлы.")
        if e.filename == file1 or e.filename == file2:
            with open(e.filename, 'w') as f:
                pass

create_two_column_file_left('Text41_1.txt', 'Text41_2.txt', 'output41.txt')
