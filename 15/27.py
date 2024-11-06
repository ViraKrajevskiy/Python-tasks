n = int(input("Введите n: "))
arr = []

for i in range(n):
    elem = int(input("Введите элемент: "))
    arr.append(elem)

is_alternating = True
for i in range(1, n):
    if (arr[i] > 0 and arr[i-1] > 0) or (arr[i] < 0 and arr[i-1] < 0):
        is_alternating = False
        break

if is_alternating:
    print(0)
else:
    print(f"Чередование нарушено на индексе: {i}")

