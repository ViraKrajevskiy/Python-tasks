n = int(input("Введите значение n: "))

product = 1
for i in range(1, n + 1):
    product *= 1 + i / 10

print(f"Произведение: {product}")
