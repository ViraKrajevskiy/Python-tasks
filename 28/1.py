class Account:
    def __init__(self, card_number, pin, balance=0, phone=None):
        self.card_number = card_number
        self.pin = pin
        self.balance = balance
        self.phone = phone
        self.sms_notifications = False

    def check_pin(self, pin):
        return self.pin == pin

    def deposit(self, amount):
        self.balance += amount
        print(f"Баланс пополнен на {amount}. Текущий баланс: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Недостаточно средств.")
        else:
            self.balance -= amount
            print(f"Снято {amount}. Текущий баланс: {self.balance}")
            if self.sms_notifications and self.phone:
                print(f"Сообщение отправлено на номер {self.phone}: Вы сняли {amount}")

    def check_balance(self):
        print(f"Текущий баланс: {self.balance}")

    def change_pin(self, new_pin):
        self.pin = new_pin
        print("Пин-код успешно изменен.")

    def enable_sms_notifications(self, phone):
        self.phone = phone
        self.sms_notifications = True
        print(f"SMS-уведомления подключены к номеру {self.phone}")


def find_account(accounts, card_number, pin):
    for account in accounts:
        if account.card_number == card_number and account.check_pin(pin):
            return account
    return None


def atm_menu(account):
    while True:
        print("\nВыберите операцию:")
        print("1. Пополнить баланс")
        print("2. Снять средства")
        print("3. Проверить баланс")
        print("4. Сменить пин-код")
        print("5. Подключить SMS-уведомления")
        print("6. Выйти")

        choice = input("Ваш выбор: ")

        if choice == "1":
            amount = float(input("Введите сумму для пополнения: "))
            account.deposit(amount)
        elif choice == "2":
            amount = float(input("Введите сумму для снятия: "))
            account.withdraw(amount)
        elif choice == "3":
            account.check_balance()
        elif choice == "4":
            new_pin = input("Введите новый пин-код: ")
            account.change_pin(new_pin)
        elif choice == "5":
            phone = input("Введите номер телефона для SMS-уведомлений: ")
            account.enable_sms_notifications(phone)
        elif choice == "6":
            print("Выход из меню.")
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")


def main():

    accounts = [
        Account("123456789", "1111", 1000),
        Account("987654321", "2222", 2000)
    ]

    print("Добро пожаловать в банкомат")
    while True:
        card_number = input("Введите номер карты: ")
        pin = input("Введите пин-код: ")

        account = find_account(accounts, card_number, pin)
        if account:
            print("Вход выполнен успешно.")
            atm_menu(account)
            break
        else:
            print("Неверный номер карты или пин-код. Попробуйте снова.")


if __name__ == "__main__":
    main()
