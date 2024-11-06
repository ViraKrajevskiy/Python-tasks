def words_of_length_k(file_path, k):
    with open(file_path, 'r') as f:
        content = f.read()

    words = content.split()
    result = [word for word in words if len(word) == k]
    with open('result.txt', 'w') as f:
        f.write('\n'.join(result))

words_of_length_k('text.txt', 5)
