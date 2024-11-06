def task_48(filename):
    with open(filename, 'r') as file:
        numbers = [int(num) for line in file for num in line.split() if int(num) % 1 == 0]
    with open('output.txt', 'w') as output_file:
        for num in numbers:
            output_file.write(f"{num}\n")

task_48('input.txt')
