import random
number = random.randint(-999, 999)
print(f"Число: {number}")

if -100 <= number <= -10 or 10 <= number <= 99:
    if number % 2 == 0:
        print("Число двузначное и чётное")
    else:
        print("Число двузначное и нечётное")
elif -999 <= number <= -100 or 100 <= number <= 999:
    if number % 2 == 0:
        print("Число трёхзначное и чётное")
    else:
        print("Число трёхзначное и нечётное")
else:
    print("Число однозначное или равно нулю")
