class Client:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.addresses = []

    def insert_address(self, city, state):
        self.addresses.append(Address(city, state).data())

    def list_addresses(self):
        for address in self.addresses:
            print(f'{address}')


class Address:
    def __init__(self, city, state):
        self.city = city
        self.state = state

    def data(self):
        return f'{self.city} ({self.state})'


c1 = Client('Kevin', 14)

c1.insert_address('Fortaleza', 'CE')

print(c1.name, c1.age)
c1.list_addresses()
