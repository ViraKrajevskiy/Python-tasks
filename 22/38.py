def trim_and_align_text(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    with open('output_task38.txt', 'w', encoding='utf-8') as file:
        for line in lines:
            trimmed_line = line.strip()  # Убираем пробелы с обоих сторон
            if trimmed_line:
                file.write(trimmed_line + '\n')
            else:
                file.write('\n')

trim_and_align_text('input_task38.txt')
