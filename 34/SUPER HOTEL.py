class User:
    def __init__(self, name, surname, age, passportid, phonenumber, balance, role="user"):
        self.name = name
        self.surname = surname
        self.age = age
        self.passportid = passportid
        self.phonenumber = phonenumber
        self.balance = balance
        self.role = role  # "user" или "admin"

    def __str__(self):
        return f"User(name={self.name}, surname={self.surname}, age={self.age}, passportid={self.passportid}, phonenumber={self.phonenumber}, balance={self.balance}, role={self.role})"

class Card(User):
    def __init__(self, name, surname, age, passportid, balance, phonenumber, password, datework, serialnumber, role="user"):
        super().__init__(name, surname, age, passportid, phonenumber, balance, role)
        self.password = password
        self.datework = datework
        self.serialnumber = serialnumber

    def __str__(self):
        return f"Card(name={self.name}, surname={self.surname}, passportid={self.passportid}, balance={self.balance}, phonenumber={self.phonenumber}, password={self.password}, datework={self.datework}, serialnumber={self.serialnumber}, role={self.role})"

class Hotel:
    def __init__(self, hotelname, rom, balance, serialnumber, usersdata, clients, numbercost):
        self.hotelname = hotelname
        self.rom = rom
        self.hotebalance = balance
        self.serialnumber = serialnumber
        self.usersdata = usersdata
        self.clients = clients
        self.numbercost = numbercost

    def __str__(self):
        return f"Hotel(hotelname={self.hotelname}, daily_rate={self.numbercost})"

    def calculate_cost(self, days):
        return days * self.numbercost

    def book_room(self, user, days):
        total_cost = self.calculate_cost(days)
        if user.balance >= total_cost:
            user.balance -= total_cost
            self.hotebalance += total_cost  # Увеличение баланса отеля
            print(f"Бронирование успешно! Вы забронировали номер на {days} дней. Остаток баланса: {user.balance}.")
        else:
            max_days = user.balance // self.numbercost
            print(
                f"Недостаточно средств! Вашего баланса хватает на {max_days} дней. "
                f"Пожалуйста, укажите меньшее количество дней."
            )

hoteladmin = User("Vira", "Krajevskiy", 25, "AD21313233", "+998900368052", 50435, role="admin")
hotelcreator = Card("Vira", "Krajevskiy", 25, "AD21313233", 245, "+998900368052", 2341, "23/28", 6064566767494159, role="admin")
user1 = Card("Nicola", "Tesla", 34, "AD2313231", 234, "+998807419654", 2312, "23/25", 1569737344034902)
user2 = Card("Jason", "Vurhis", 40, "AD2314211", 603, "+998545266235", 1245, "31/24", 1511568310804246)
user3 = Card("Lev", "Kravchenko", 18, "AD3213321", 500, "+998904522242", 2224, "25/24", 8278493165778179)
user4 = Card("Maks", "KOrj", 18, "AD2213634", 3234523, "+998908045068", [8954, 8654, 6006], ["23/24", "21/25", "09/29"], [6389216235616658, 6115014664432703, 3520976220489847])
user5 = Card("Uilyam", "Erno", 32, "AD2314235", 15000, "+998607415020", [2331, 1234], ["23/28", "12/27"], [8498617394558745, 1711838709101918])
user6 = Card("Brandon", "Hererro", 39, "AD2345122", 546000,  ["+998806058540"], [2345, 2313], ["12/24", "15/25"], [4577808632405136, 2209322009290605])



hotelBuild = Hotel("Hilor", "roms", 6, [], [], [], 154)

giperuser = [hoteladmin, hotelcreator, user1, user2, user3, user4, user5, user6,hotelBuild]



def enter():

    userinput = input("Введите ваш паспортный ID для входа: ")

    for user in giperuser:
        if user.passportid   == userinput :
            print(f"Добро пожаловать, {user.name} {user.surname}!")
            return user.role, user

    print("Пользователь с таким паспортным ID не найден.")
    return None

def admin():
    while True:
        print("\nМеню администратора:")
        print("0. Добавить пользователя")
        print("1. Просмотреть всех пользователей")
        print("2. Изменить данные пользователя")
        print("3. Удалить пользователя")
        print("4. Показать баланс отеля")
        print("5. Выход")

        choice = input("Выберите действие: ")

        if choice == "0":
            print("\nДобавление нового пользователя.")
            try:
                name = input("Введите имя: ")
                surname = input("Введите фамилию: ")
                age = int(input("Введите возраст: "))
                passportid = input("Введите паспортный ID: ")
                balance = int(input("Введите начальный баланс: "))
                phonenumber = input("Введите номер телефона: ")
                role = input("Введите роль (user/admin, по умолчанию user): ").lower() or "user"

                new_user = User(name, surname, age, passportid, phonenumber, balance, role)
                giperuser.append(new_user)
                hotelBuild.usersdata.append(new_user)
                print(f"Пользователь {name} {surname} успешно добавлен!")
            except ValueError:
                print("Ошибка ввода. Проверьте данные и попробуйте снова.")

        elif choice == "1":
            print("\nСписок всех пользователей:")
            for idx, user in enumerate(giperuser, 1):
                print(f"{idx}. {user}")

        elif choice == "2":
            user_passport_id = input("Введите паспортный ID пользователя для изменения данных: ")
            found_user = next((user for user in giperuser if user.passportid == user_passport_id), None)

            if not found_user:
                print("Пользователь с таким паспортным ID не найден.")
                continue

            print(f"Выбранный пользователь: {found_user}")
            print("\nДоступные данные для изменения:")
            print("1. Имя")
            print("2. Фамилия")
            print("3. Возраст")
            print("4. Баланс")
            print("5. Номер телефона")

            field_choice = input("Введите номер поля для изменения: ")

            try:
                if field_choice == "1":
                    found_user.name = input("Введите новое имя: ")
                elif field_choice == "2":
                    found_user.surname = input("Введите новую фамилию: ")
                elif field_choice == "3":
                    found_user.age = int(input("Введите новый возраст: "))
                elif field_choice == "4":
                    if isinstance(found_user.balance, list):
                        print("Доступные балансы:")
                        for idx, bal in enumerate(found_user.balance, 1):
                            print(f"{idx}. {bal}")
                        balance_idx = int(input("Введите номер баланса для изменения: ")) - 1
                        found_user.balance[balance_idx] = int(input("Введите новый баланс: "))
                    else:
                        found_user.balance = int(input("Введите новый баланс: "))
                elif field_choice == "5":
                    found_user.phonenumber = input("Введите новый номер телефона: ")
                else:
                    print("Неверный выбор.")
                print("Данные успешно изменены.")
            except (ValueError, IndexError):
                print("Ошибка при изменении данных.")

        elif choice == "3":
            user_passport_id = input("Введите паспортный ID пользователя для удаления: ")
            found_user = next((user for user in giperuser if user.passportid == user_passport_id), None)

            if not found_user:
                print("Пользователь с таким паспортным ID не найден.")
            else:
                giperuser.remove(found_user)
                if found_user in hotelBuild.usersdata:
                    hotelBuild.usersdata.remove(found_user)
                print(f"Пользователь {found_user.name} {found_user.surname} удален.")

        elif choice == "4":
            print(f"Баланс отеля: {hotelBuild.hotebalance}.")

        elif choice == "5":
            print("Выход из режима администратора.")
            return enter()

        else:
            print("Некорректный выбор. Попробуйте снова.")


def user_booking(user):

    print(f"Добро пожаловать, {user.name}! В отеле {hotelBuild.hotelname} стоимость проживания {hotelBuild.numbercost}$ в день.")
    print("Для выхода введите 'exit'.")

    while True:
        user_input = input("Сколько дней вы хотите забронировать? ")

        if user_input.lower() == 'exit':
            print("Спасибо за использование системы бронирования. До свидания!")
            return enter()

        try:
            days = int(user_input)
            if days <= 0:
                print("Количество дней должно быть положительным.")
                continue
            hotelBuild.book_room(user, days)
            if user.balance == 0:
                print("Ваш баланс пуст. Вы больше не можете бронировать номера.")
                break
        except ValueError:
            print("Пожалуйста, введите корректное количество дней.")

while True:

    role, current_user = enter()

    if role == "admin":
        admin()
    elif role == "user":
        user_booking(current_user)