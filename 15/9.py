
n = int(input("Введите n: "))
arr = []

for i in range(n):
    elem = int(input("Введите элемент: "))
    arr.append(elem)

even_elements = []
for i in range(1, n, 2):
    if arr[i] % 2 == 0:
        even_elements.append(arr[i])

for i in range(len(even_elements)):
    for j in range(i + 1, len(even_elements)):
        if even_elements[i] < even_elements[j]:
            even_elements[i], even_elements[j] = even_elements[j], even_elements[i]

print("Четные элементы с нечетными индексами:", even_elements)
print("Количество четных элементов:", len(even_elements))
