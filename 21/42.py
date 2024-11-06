def create_function_table(N, A, B, output_file):
    with open(output_file, 'w') as out:
        for i in range(N + 1):
            x = A + i * (B - A) / N
            out.write(f"{x:.4f} {x ** 0.5:.4f}\n")

create_function_table(10, 0, 100, 'function_table42.txt')
