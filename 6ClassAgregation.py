class Shopping_cart:
    def __init__(self):
        self.products = []

    def insert_products(self, product):
        self.products.append(product)

    def products_list(self):
        for product in self.products:
            print(f'{product.name}:  R${product.price}')

    def total_price(self):
        total = 0
        for product in self.products:
            total += product.price
        return f'Total price: R${total}'


class Products:
    def __init__(self, name, price):
        self.name = name
        self.price = price


car = Shopping_cart()

p1 = Products('Shirt', 50)
p2 = Products('Phone', 2399)
p3 = Products('Mouse', 25)

car.insert_products(p1)
car.insert_products(p2)
car.insert_products(p3)

car.products_list()
print(car.total_price())