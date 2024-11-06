def task_44(filename):
    with open(filename, 'r') as file:
        numbers = [int(num) for line in file for num in line.split()]
    print("Количество чисел:", len(numbers))
    print("Сумма чисел:", sum(numbers))

task_44('input.txt')
