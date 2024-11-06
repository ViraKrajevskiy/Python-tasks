def format_text_k(input_file, output_file, K):
    try:
        with open(input_file, 'r') as f:
            lines = f.read().splitlines()
    except FileNotFoundError:
        print(f"Файл {input_file} не найден. Создаю пустой файл.")
        with open(input_file, 'w') as f:
            pass
        return

    formatted_lines = []
    for line in lines:
        if line.strip():
            words = line.split()
            current_line = ''
            for word in words:
                if len(current_line) + len(word) + 1 <= K:
                    current_line += (word + ' ')
                else:
                    formatted_lines.append(current_line.strip())
                    current_line = word + ' '
            formatted_lines.append(current_line.strip())

    with open(output_file, 'w') as f:
        f.writelines(f"{line}\n" for line in formatted_lines)

format_text_k('Text38.txt', 'formatted_text38.txt', 25)
