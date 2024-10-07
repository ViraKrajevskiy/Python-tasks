a = int(input("Введите значение a: "))
b = int(input("Введите значение b (a < b): "))

sum_squares = sum(i**2 for i in range(a, b + 1))

print(f"Сумма квадратов чисел от {a} до {b}: {sum_squares}")
