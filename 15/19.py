n = int(input("Введите n: "))
arr = []

for i in range(n):
    elem = int(input("Введите элемент: "))
    arr.append(elem)

first_elem = arr[0]
last_elem = arr[-1]

print("Элементы, которые больше первого и меньше последнего:")
for i in range(n):
    if first_elem < arr[i] < last_elem:
        print(arr[i])
