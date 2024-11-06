inero = input()

class Client:
    def __init__(self, name, phone, id, base):
        self.name = name
        self.phone = phone
        self.id = id

    def __repr__(self):
        return f"Client(name='{self.name}', phone='{self.phone}', id={self.id})"

class Rooms:
    def __init__(self, number, room_type):
        self.number = number
        self.room_type = room_type
        self.clients = []

    def add_client(self, client):
        self.clients.append(client)

    def del_client(self, client_id):
        self.clients = [client for client in self.clients if client.id != client_id]

    def client_data(self):
        return self.clients

    def __repr__(self):
        return f"Room(number={self.number}, type='{self.room_type}', clients={self.clients})"
