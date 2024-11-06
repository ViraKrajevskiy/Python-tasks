def text30(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        paragraphs = file.read().split('\n\n')
    shortest_words = [min(p.split(), key=len) for p in paragraphs if p.strip()]
    for i, word in enumerate(shortest_words, 1):
        print(f"Самое короткое слово в абзаце {i}: {word}")
    return shortest_words

