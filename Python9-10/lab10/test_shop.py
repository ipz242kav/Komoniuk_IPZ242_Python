import unittest
from shop import Shop, Discount


class TestShop(unittest.TestCase):
    def setUp(self):
        self.store = Shop("TechShop", "Електроніка")

    def test_shop_creation(self):
        self.assertEqual(self.store.shop_name, "TechShop")
        self.assertEqual(self.store.store_type, "Електроніка")
        self.assertEqual(self.store.number_of_units, 0)

    def test_shop_with_units(self):
        store = Shop("BookStore", "Книги", 50)
        self.assertEqual(store.number_of_units, 50)

    def test_set_number_of_units(self):
        self.store.set_number_of_units(100)
        self.assertEqual(self.store.number_of_units, 100)

    def test_increment_number_of_units(self):
        self.store.set_number_of_units(10)
        self.store.increment_number_of_units(5)
        self.assertEqual(self.store.number_of_units, 15)

    def test_describe_shop(self):
        self.assertIsNone(self.store.describe_shop())

    def test_open_shop(self):
        self.assertIsNone(self.store.open_shop())


class TestDiscount(unittest.TestCase):
    def setUp(self):
        self.discount_store = Discount("SaleShop", "Одяг", 20, ["Футболка", "Джинси"])

    def test_discount_creation(self):
        self.assertEqual(self.discount_store.shop_name, "SaleShop")
        self.assertEqual(self.discount_store.store_type, "Одяг")
        self.assertEqual(self.discount_store.number_of_units, 20)

    def test_discount_products(self):
        products = self.discount_store.get_discounts_products()
        self.assertEqual(len(products), 2)
        self.assertIn("Футболка", products)

    def test_discount_empty_products(self):
        store = Discount("EmptyStore", "Техніка")
        self.assertEqual(store.discount_products, [])

    def test_discount_inherits_shop(self):
        self.assertIsInstance(self.discount_store, Shop)


if __name__ == '__main__':
    unittest.main()
