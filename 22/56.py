def task_56(filename):
    with open(filename, 'r') as file:
        text = file.read()

    words = text.split()
    word_count = len(words)
    unique_word_count = len(set(words))

    with open('word_count.txt', 'w') as f:
        f.write(f"Общее количество слов: {word_count}\n")
        f.write(f"Количество уникальных слов: {unique_word_count}\n")

task_56('input.txt')
