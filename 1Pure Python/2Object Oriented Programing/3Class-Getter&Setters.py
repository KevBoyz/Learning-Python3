# Gets and setters are way to validate the instances attributes

class Product:
    store = 'Store x'  # Class attribute

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def discount(self, percent):
        self.price = self.price - (self.price * (percent / 100))

    @property  # Getter (name)
    def name(self):
        return self.name_

    @name.setter  # Setter (name)
    def name(self, value):
        self.name_ = value.title()


    @property   # Getter
    def price(self):
        return self.price_

    @price.setter  # Setter
    def price(self, value):
        if isinstance(value, str):
            value = float(value.replace('R$', ''))
        self.price_ = value



p1 = Product('shirt', 'R$50')
p1.discount(10)

print(p1.store)
Product.store = 'null'
print(p1.store)

print(p1.name, '...', p1.price)