n = int(input("Введите n: "))
arr = []

for i in range(n):
    elem = int(input("Введите элемент: "))
    arr.append(elem)

is_alternating = True
for i in range(1, n):
    if (arr[i] % 2 == arr[i-1] % 2):
        is_alternating = False
        break

if is_alternating:
    print("Четные и нечетные элементы чередуются")
else:
    print("Четные и нечетные элементы не чередуются")
