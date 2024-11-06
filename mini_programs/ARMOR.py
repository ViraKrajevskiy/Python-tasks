import time

# показывает скоко времени прошло
def stopwatch():
    input("Нажмите Enter, чтобы начать секундомер...")
    start_time = time.time()  # Текущее время
    input("Нажмите Enter, чтобы остановить секундомер...")
    end_time = time.time()    # Текущее время снова
    elapsed_time = end_time - start_time
    print(f"Прошло времени: {elapsed_time:.2f} секунд")

def timer(duration):
    print(f"Таймер запущен на {duration} секунд.")
    while duration:
        minutes, seconds = divmod(duration, 60)
        print(f"{minutes:02}:{seconds:02}", end="\r")  # Печатаем таймер в строке
        time.sleep(1)
        duration -= 1
    print("Время вышло!")

timer(10)  # Таймер на 10 секунд

