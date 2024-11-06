def text24(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        paragraphs = content.split('\n\n')
        paragraph_count = len([p for p in paragraphs if p.strip()])
        print("Количество абзацев:", paragraph_count)
        return paragraph_count

