def task_53(filename):
    from collections import Counter

    with open(filename, 'r') as file:
        text = file.read()

    text = ''.join(filter(str.isalpha, text))
    frequencies = Counter(text)

    with open('frequencies.txt', 'w') as f:
        for char, freq in frequencies.items():
            f.write(f"{char}: {freq}\n")

task_53('input.txt')
