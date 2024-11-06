def first_word(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    words = content.split()
    return words[0] if words else ''

print(first_word('text.txt'))
