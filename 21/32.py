def words_starting_with_c(file_path, c):
    with open(file_path, 'r') as f:
        content = f.read()
    words = content.split()
    result = [word for word in words if word.lower().startswith(c.lower())]
    with open('result.txt', 'w') as f:
        f.write('\n'.join(result))

words_starting_with_c('text.txt', 'и')
