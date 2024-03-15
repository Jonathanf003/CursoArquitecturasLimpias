class Cart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def calculate_total(self):
        return sum(product.price for product in self.products)

    def apply_discount(self, discount):
        self.discount = discount / 100
        self.total *= (1 - self.discount)