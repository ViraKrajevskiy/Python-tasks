def text34(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        paragraphs = file.read().split('\n\n')
    short_paragraphs = [p.strip() for p in paragraphs if len(p.strip()) < 50]
    print("Абзацы длиной менее 50 символов:")
    for paragraph in short_paragraphs:
        print(paragraph, "\n")
    return short_paragraphs
