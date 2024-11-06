def format_paragraphs(filename):
    max_length = 50
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    formatted_text = []
    paragraph = []

    for line in lines:
        stripped_line = line.strip()
        if stripped_line:
            paragraph.append(stripped_line)
        else:
            if paragraph:
                formatted_text.append(' '.join(paragraph))
                paragraph = []
            formatted_text.append('')

    if paragraph:
        formatted_text.append(' '.join(paragraph))

    with open('output_task39.txt', 'w', encoding='utf-8') as file:
        for line in formatted_text:
            while len(line) > max_length:
                file.write(line[:max_length] + '\n')
                line = line[max_length:]
            file.write(line + '\n')

format_paragraphs('input_task39.txt')
