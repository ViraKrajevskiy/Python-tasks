def text27(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        paragraphs = file.read().split('\n\n')
    result = [p.strip() for p in paragraphs if p.strip().endswith('т')]
    print("Абзацы, заканчивающиеся на 'т':")
    for paragraph in result:
        print(paragraph, "\n")
    return result
