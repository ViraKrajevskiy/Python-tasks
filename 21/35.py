

def right_justify(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    lines = content.splitlines()
    justified_lines = [line.rstrip().rjust(50) for line in lines]
    with open(file_path, 'w') as f:
        f.write('\n'.join(justified_lines))

right_justify('text.txt')
