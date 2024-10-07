import random
year = random.randint(1900, 2100)
print(f"Год: {year}")

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} год — високосный (366 дней)")
else:
    print(f"{year} год — обычный (365 дней)")
