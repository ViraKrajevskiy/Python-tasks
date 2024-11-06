n = int(input("Введите n: "))
A = int(input("Введите первый член A: "))
R = int(input("Введите знаменатель R: "))
arr = []

for i in range(n):
    arr.append(A * R ** i)

print("Массив:", arr)
