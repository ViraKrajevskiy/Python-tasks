def add_list(a: list) -> int:

    even_product = 1
    odd_product = 1

    for num in a:
        if num % 2 == 0:
            even_product *= num
        else:
            odd_product *= num

    return even_product - odd_product


numbers = [1, 2, 3, 4, 5]
result = add_list(numbers)
print(f"Natija: {result}")
