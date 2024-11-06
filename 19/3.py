def contains_digit(text):
    return any(char.isdigit() for char in text)


text = "There are 3 apples."
print(contains_digit(text))
