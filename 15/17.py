n = int(input("Введите n: "))
arr = []

for i in range(n):
    elem = int(input("Введите элемент: "))
    arr.append(elem)

print("Элементы с шагом 2, начиная с первого:")
for i in range(0, n, 2):
    print(arr[i])

print("Элементы с шагом 2, начиная с последнего:")
for i in range(n - 1, -1, -2):
    print(arr[i])
