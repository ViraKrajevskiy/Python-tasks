import time

n = 3
m = 100000

def timer():
    for i in range(n):
        start_time = time.time()
        for j in range(m):
            _ = i * j
        end_time = time.time()

        return f"Цикл {i + 1}/{n} {end_time - start_time:.6f} времени отработал"


def fibonacci_closure():
    a, b = 0, 1

    def next_fibonacci():
        nonlocal a, b
        result = a
        a, b = b, a + b
        return result

    return next_fibonacci


fib = fibonacci_closure()

for _ in range(10):
    fib_number = fib()
    timer_result = timer()
    print(f"{fib_number}, {timer_result}")
