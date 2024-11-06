def add_empty_lines_between_paragraphs(file_path):
    with open(file_path,'r') as f:
        content = f.read()

    paragraphs = content.split('\n\n')
    new_paragraphs = []

    for p in paragraphs:
        new_paragraphs.append(p)
        new_paragraphs.append('')

    if new_paragraphs and new_paragraphs[-1] == '':
        new_paragraphs.pop()

    with open(file_path, 'w') as f:
        f.write('\n\n'.join(new_paragraphs))

add_empty_lines_between_paragraphs('text.txt')
