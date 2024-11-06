# Родительский класс Texnika
class Texnika:
    def __init__(self, brand, model, type):
        self.brand = brand
        self.model = model
        self.type = type

    def info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Type: {self.type}")

# Классы техники
# Класс компьютеры
class PK(Texnika):
    def __init__(self, brand, model, type, video_card, ram, display):
        super().__init__(brand, model, type)
        self.video_card = video_card
        self.ram = ram
        self.display = display

    def info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Type: {self.type}, "
              f"Video Card: {self.video_card}, RAM: {self.ram}, Display: {self.display}")

# Класс телевизоры
class TV(Texnika):
    def __init__(self, brand, model, type, size, display):
        super().__init__(brand, model, type)
        self.size = size
        self.display = display

    def info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Type: {self.type}, "
              f"Size: {self.size}, Display: {self.display}")

# Класс телефоны
class Phone(Texnika):
    def __init__(self, brand, model, type, size, sim_count):
        super().__init__(brand, model, type)
        self.size = size
        self.sim_count = sim_count

    def info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Type: {self.type}, "
              f"Size: {self.size}, SIM Count: {self.sim_count}")

# Классы транспорта
# Класс автомобили
class Cars(Texnika):
    def __init__(self, brand, model, type, battery_life, charging_time):
        super().__init__(brand, model, type)
        self.battery_life = battery_life
        self.charging_time = charging_time

    def info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Type: {self.type}, "
              f"Battery Life: {self.battery_life}, Charging Time: {self.charging_time}")

# Класс мотоциклы
class Moto(Texnika):
    def __init__(self, brand, model, type, motor, color):
        super().__init__(brand, model, type)
        self.motor = motor
        self.color = color

    def more_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Type: {self.type}, "
              f"Motor: {self.motor}, Color: {self.color}")

# Класс фура
class Fura(Texnika):
    def __init__(self, brand, model, type, motor, height, long, weight):
        super().__init__(brand, model, type)
        self.motor = motor
        self.height = height
        self.long = long
        self.weight = weight

    def info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Type: {self.type}, "
              f"Motor: {self.motor}, Height: {self.height}, Length: {self.long}, Weight: {self.weight}")

# Примеры использования
if __name__ == "__main__":
    print("Техника:")
    pc = PK("Dell", "Inspiron", "Laptop", "NVIDIA GTX 1050", "16GB", "15.6 inch")
    pc.info()

    tv = TV("Samsung", "QLED", "Smart TV", "55 inches", "4K UHD")
    tv.info()

    phone = Phone("Apple", "iPhone 14", "Smartphone", "6.1 inches", 2)
    phone.info()

    # --- Транспорт ---
    print("\nТранспорт:")
    car = Cars("Tesla", "Model S", "Electric", "500km", "1 hour")
    car.info()

    moto = Moto("Harley Davidson", "Sportster", "Motorbike", "1200cc", "Black")
    moto.more_info()

    fura = Fura("Volvo", "FH16", "Truck", "750hp", "4m", "12m", "20 tons")
    fura.info()
