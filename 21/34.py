def center_justify(file_path, width=50):
    with open(file_path, 'r') as f:
        content = f.read()

    lines = content.splitlines()
    justified_lines = [line.center(width) for line in lines]

    with open(file_path, 'w') as f:
        f.write('\n'.join(justified_lines))

center_justify('text.txt')
