
n = int(input("Введите n: "))
arr = []

for i in range(n):
    elem = int(input("Введите элемент: "))
    arr.append(elem)

even_elements = []
odd_elements = []
for i in range(n):
    if arr[i] % 2 == 0:
        even_elements.append(arr[i])
    else:
        odd_elements.append(arr[i])


for i in range(len(even_elements)):
    for j in range(i + 1, len(even_elements)):
        if even_elements[i] < even_elements[j]:
            even_elements[i], even_elements[j] = even_elements[j], even_elements[i]


for i in range(len(odd_elements)):
    for j in range(i + 1, len(odd_elements)):
        if odd_elements[i] < odd_elements[j]:
            odd_elements[i], odd_elements[j] = odd_elements[j], odd_elements[i]


print("Четные элементы по убыванию:", even_elements)
print("Нечетные элементы по убыванию:", odd_elements)
