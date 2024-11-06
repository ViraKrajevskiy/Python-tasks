class User:
    def __init__(self, first_name, password, is_admin=False):
        self._first_name = first_name
        self._password = password
        self._is_admin = is_admin

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value

    @property
    def is_admin(self):
        return self._is_admin

    @is_admin.setter
    def is_admin(self, value):
        self._is_admin = value

class Car:
    def __init__(self, car_brand, car_model, car_year, speed, cost):
        self._car_brand = car_brand
        self._car_model = car_model
        self._car_year = car_year
        self._speed = speed
        self._cost = cost

    def __str__(self):
        return (f"{self.car_brand} {self.car_model}, Year: {self.car_year}, "
                f"Speed: {self.speed} km/h, Cost: ${self.cost}")

    @property
    def car_brand(self):
        return self._car_brand

    @car_brand.setter
    def car_brand(self, value):
        self._car_brand = value

    @property
    def car_model(self):
        return self._car_model

    @car_model.setter
    def car_model(self, value):
        self._car_model = value

    @property
    def car_year(self):
        return self._car_year

    @car_year.setter
    def car_year(self, value):
        self._car_year = value

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        self._speed = value

    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, value):
        self._cost = value

class CarMarketplace:
    def __init__(self):
        self.cars = []
        self.users = []
        self.admin_password = "admin123"

    def add_user(self, first_name, password, is_admin=False):
        self.users.append(User(first_name, password, is_admin))

    def login(self, first_name, password):
        for user in self.users:
            if user.first_name == first_name and user.password == password:
                return user
        return None

    def add_car(self, car):
        self.cars.append(car)

    def remove_car(self, car_index):
        if 0 <= car_index < len(self.cars):
            del self.cars[car_index]

    def replace_car(self, car_index, new_car):
        if 0 <= car_index < len(self.cars):
            self.cars[car_index] = new_car

    def list_cars(self):
        if not self.cars:
            print("No cars available.")
        else:
            for i, car in enumerate(self.cars):
                print(f"{i + 1}. {car}")

    def buy_car(self, car_index):
        if 0 <= car_index < len(self.cars):
            car = self.cars.pop(car_index)
            print(f"You have purchased: {car}")
        else:
            print("Invalid selection.")

def main():
    marketplace = CarMarketplace()

    marketplace.add_user("admin", marketplace.admin_password, is_admin=True)
    marketplace.add_user("user1", "user123")

    first_name = input("Enter your username: ")
    password = input("Enter your password: ")

    user = marketplace.login(first_name, password)

    if not user:
        print("Invalid login credentials.")
        return

    if user.is_admin:
        print(f"Welcome, Admin {user.first_name}!")
        while True:
            print("\nAdmin Panel:")
            print("1. Add a car")
            print("2. Remove a car")
            print("3. Replace a car")
            print("4. View cars")
            print("5. Logout")

            choice = input("Enter your choice: ")
            if choice == "1":
                brand = input("Enter car brand: ")
                model = input("Enter car model: ")
                year = int(input("Enter car year: "))
                speed = int(input("Enter car speed: "))
                cost = float(input("Enter car cost: "))
                car = Car(brand, model, year, speed, cost)
                marketplace.add_car(car)
                print("Car added successfully.")
            elif choice == "2":
                marketplace.list_cars()
                index = int(input("Enter car number to remove: ")) - 1
                marketplace.remove_car(index)
                print("Car removed successfully.")
            elif choice == "3":
                marketplace.list_cars()
                index = int(input("Enter car number to replace: ")) - 1
                brand = input("Enter new car brand: ")
                model = input("Enter new car model: ")
                year = int(input("Enter new car year: "))
                speed = int(input("Enter new car speed: "))
                cost = float(input("Enter new car cost: "))
                new_car = Car(brand, model, year, speed, cost)
                marketplace.replace_car(index, new_car)
                print("Car replaced successfully.")
            elif choice == "4":
                marketplace.list_cars()
            elif choice == "5":
                print("Logging out...")
                break
            else:
                print("Invalid choice. Try again.")

    else:
        print(f"Welcome, {user.first_name}!")
        while True:
            print("\nUser Panel:")
            print("1. View cars")
            print("2. Buy a car")
            print("3. Logout")

            choice = input("Enter your choice: ")
            if choice == "1":
                marketplace.list_cars()
            elif choice == "2":
                marketplace.list_cars()
                index = int(input("Enter car number to buy: ")) - 1
                marketplace.buy_car(index)
            elif choice == "3":
                print("Logging out...")
                break
            else:
                print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
