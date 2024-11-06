import json
import os

filename = os.path.join(os.path.dirname(__file__), 'cars.json')


def load_data():
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {"cars": []}

def save_data(data):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def car_crud():
    print("\nВыберите операцию:")
    print("1. Добавить машину")
    print("2. Просмотреть все машины")
    print("3. Обновить машину")
    print("4. Удалить машину")

    action = input("Введите номер операции (1/2/3/4): ")

    data = load_data()

    if action == '1':

        car_id = int(input("Введите ID автомобиля: "))
        brand = input("Введите марку автомобиля: ")
        model = input("Введите модель автомобиля: ")
        color = input("Введите цвет автомобиля: ")
        new_car = {"id": car_id, "brand": brand, "model": model, "color": color}
        data['cars'].append(new_car)
        save_data(data)
        print(f"Машина добавлена: {new_car}")

    elif action == '2':

        if data['cars']:
            for car in data['cars']:
                print(f"ID: {car['id']}, Марка: {car['brand']}, Модель: {car['model']}, Цвет: {car['color']}")
        else:
            print("Нет данных о машинах.")

    elif action == '3':

        car_id = int(input("Введите ID автомобиля, который хотите обновить: "))
        for car in data['cars']:
            if car['id'] == car_id:
                new_model = input("Введите новую модель (оставьте пустым, если не нужно изменять): ")
                new_color = input("Введите новый цвет (оставьте пустым, если не нужно изменять): ")
                if new_model:
                    car['model'] = new_model
                if new_color:
                    car['color'] = new_color
                save_data(data)
                print(f"Машина обновлена: {car}")
                break
        else:
            print("Машина с таким ID не найдена.")

    elif action == '4':
        car_id = int(input("Введите ID автомобиля, который хотите удалить: "))
        updated_cars = [car for car in data['cars'] if car['id'] != car_id]
        if len(updated_cars) == len(data['cars']):
            print("Машина с таким ID не найдена.")
        else:
            data['cars'] = updated_cars
            save_data(data)
            print(f"Машина с ID {car_id} удалена.")

    else:
        print("Ошибка: Неверный выбор. Пожалуйста, выберите 1, 2, 3 или 4.")
