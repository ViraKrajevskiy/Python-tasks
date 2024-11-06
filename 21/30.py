def last_word(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    words = content.split()
    return words[-1] if words else ''

print(last_word('text.txt'))
