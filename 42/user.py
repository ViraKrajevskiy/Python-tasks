my_list = [1, 2, 3]
iterator = iter(my_list)

print(next(iterator))
print(next(iterator))
print(next(iterator))

my_list = [10, 20, 30]
iterator = iter(my_list)

print(next(iterator))
print(next(iterator))
print(next(iterator))

class Counter:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):

        if self.current < self.end:
            self.current += 1
            return self.current - 1
        raise StopIteration

counter = Counter(1, 5)
for num in counter:
    print(num)


def counter_generator(start, end):
    while start < end:
        yield start
        start += 1

for num in counter_generator(1, 5):
    print(num)


# 4 способ: Генераторное выражение
squares = (x**2 for x in range(5))

print(next(squares))  # 0
print(next(squares))  # 1
print(next(squares))  # 4
