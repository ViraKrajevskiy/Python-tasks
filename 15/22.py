n = int(input("Введите n: "))
K = int(input("Введите K: "))
L = int(input("Введите L: "))
arr = []

for i in range(n):
    elem = int(input("Введите элемент: "))
    arr.append(elem)

sum_K_to_L = sum(arr[K:L+1])

sum_L_to_end = sum(arr[L+1:])

print(f"Сумма элементов с индексами от {K} до {L}: {sum_K_to_L}")
print(f"Сумма элементов с индексами от {L+1} до конца: {sum_L_to_end}")
