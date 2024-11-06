class BankKarta:
    def __init__(self, nomer, balans=0):
        self.nomer = nomer
        self.balans = balans

    def dobavit_dengi(self, summa):
        if summa > 0:
            self.balans += summa
            print(f"{summa} сум добавлено. Новый баланс: {self.balans} сум.")
        else:
            print("Сумма должна быть больше нуля.")

    def proverit_balans(self):
        print(f"Баланс карты: {self.balans} сум.")
        return self.balans

    def informaciya(self):
        return {"Номер карты": self.nomer, "Баланс": self.balans}


class Bankomat:
    def __init__(self):
        self.karty = []

    def dobavit_kartu(self, nomer):

        for karta in self.karty:
            if karta.nomer == nomer:
                print("Карта с таким номером уже существует.")
                return
        novaya_karta = BankKarta(nomer)
        self.karty.append(novaya_karta)
        print(f"Карта с номером {nomer} добавлена.")

    def dobavit_dengi_na_kartu(self, nomer, summa):

        for karta in self.karty:
            if karta.nomer == nomer:
                karta.dobavit_dengi(summa)
                return
        print("Карта с таким номером не найдена.")

    def pokazat_vse_karty(self):

        print("Список всех карт:")
        for karta in self.karty:
            info = karta.informaciya()
            print(f"Номер карты: {info['Номер карты']}, Баланс: {info['Баланс']} сум")

bankomat = Bankomat()
bankomat.dobavit_kartu("8600123456789123")
bankomat.dobavit_dengi_na_kartu("8600123456789123", 100000)
bankomat.dobavit_kartu("8600987654321098")
bankomat.dobavit_dengi_na_kartu("8600987654321098", 50000)

bankomat.pokazat_vse_karty()
