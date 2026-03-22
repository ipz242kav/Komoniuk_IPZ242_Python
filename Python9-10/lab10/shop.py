class Shop:
    def __init__(self, shop_name, store_type, number_of_units=0):
        self.shop_name = shop_name
        self.store_type = store_type
        self.number_of_units = number_of_units

    def describe_shop(self):
        print(f"Назва: {self.shop_name}, Тип: {self.store_type}")

    def open_shop(self):
        print(f"Онлайн-магазин '{self.shop_name}' відкрито!")

    def set_number_of_units(self, units):
        self.number_of_units = units

    def increment_number_of_units(self, amount):
        self.number_of_units += amount


class Discount(Shop):
    def __init__(self, shop_name, store_type, number_of_units=0, discount_products=None):
        super().__init__(shop_name, store_type, number_of_units)
        if discount_products is None:
            self.discount_products = []
        else:
            self.discount_products = discount_products

    def get_discounts_products(self):
        print(f"Товари зі знижкою: {self.discount_products}")
        return self.discount_products
