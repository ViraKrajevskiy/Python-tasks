def read_file(f_name):

    try:
        with open(f_name, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return f"Файл не найден: {f_name}"
    except Exception as e:
        return f"Произошла ошибка: {str(e)}"

file_name = "example.txt"
content = read_file(file_name)
print(content)
