def product_of_elements_at_multiples_of_three(a):
    product = 1
    for i in range(0, len(a), 3):
        product *= a[i]
    return product

a = [2, 4, 6, 8, 10, 12]
product = product_of_elements_at_multiples_of_three(a)
print(product)