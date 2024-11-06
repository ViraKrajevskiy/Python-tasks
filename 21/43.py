import math

def create_trig_table(N, A, B, output_file):
    with open(output_file, 'w') as out:
        for i in range(N + 1):
            x = A + i * (B - A) / N
            out.write(f"{x:.4f} {math.sin(x):.4f} {math.cos(x):.4f}\n")

create_trig_table(10, 0, 2 * math.pi, 'trig_table43.txt')
