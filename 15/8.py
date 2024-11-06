
n = int(input("Введите n: "))
arr = [int(input("Введите элемент: ")) for _ in range(n)]

odd_elements = [arr[i] for i in range(1, n, 2)]
odd_elements.sort()

print("Нечетные элементы по индексам:", odd_elements)
print("Количество нечетных элементов:", len(odd_elements))
