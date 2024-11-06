def text25(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        paragraphs = file.read().split('\n\n')
    result = [p.strip() for p in paragraphs if p.strip().startswith('К')]
    print("Абзацы, начинающиеся с 'К':", result)
    return result

