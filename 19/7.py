def remove_uppercase(text):
    return ''.join(char for char in text if not char.isupper())


text = "Hello World!"
print(remove_uppercase(text))
