def split_into_4_lines(text):
    lines = []
    while len(text) > 0:
        if len(text) >= 20:
            lines.append(text[:20])
            text = text[20:]
        else:
            lines.append(text)
            text = ""
    return "\n".join(lines)

text = "This is a long string that needs to be split into 4 lines with each line being at least 20 characters long."
print(split_into_4_lines(text))
