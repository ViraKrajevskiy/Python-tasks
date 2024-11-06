def remove_paragraph_by_number(file_path, k):
    with open(file_path, 'r') as f:
        content = f.read()
    paragraphs = content.split('\n\n')
    if 0 <= k < len(paragraphs):
        del paragraphs[k]
    with open(file_path, 'w') as f:
        f.write('\n\n'.join(paragraphs))

remove_paragraph_by_number('text.txt', 0)
