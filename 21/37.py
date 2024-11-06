def align_text(input_file, output_file):
    try:
        with open(input_file, 'r') as f:
            lines = f.read().splitlines()
    except FileNotFoundError:
        print(f"Файл {input_file} не найден. Создаю пустой файл.")
        with open(input_file, 'w') as f:
            pass
        return

    aligned_lines = [' '.join(line.split()) for line in lines if line.strip()]

    with open(output_file, 'w') as f:
        f.writelines(f"{line:<50}\n" for line in aligned_lines)

align_text('Text37.txt', 'aligned_text37.txt')
