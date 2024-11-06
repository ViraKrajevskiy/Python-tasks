def count_paragraphs(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    paragraphs = content.split('\n\n')
    return len(paragraphs)
print(count_paragraphs('text.txt'))
