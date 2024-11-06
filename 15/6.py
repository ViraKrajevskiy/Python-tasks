n = int(input("Bведите  n (n > 2): "))
A = int(input("Введите первый элемент (A): "))
B = int(input("( B): "))
x = [A, B]
while len(x)<n:
    s = sum(x)
    x.append(s)
print(x)
