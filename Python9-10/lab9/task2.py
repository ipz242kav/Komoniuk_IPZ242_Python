class House:
    def __init__(self, area=50, price=10000):
        self._area = area
        self._price = price

    def final_price(self, discount):
        return self._price * (1 - discount / 100)


class SmallHouse(House):
    def __init__(self, price=5000):
        super().__init__(40, price)


class Human:
    default_name = "Іван Петренко"
    default_age = 30

    def __init__(self, name=None, age=None, money=0, house=None):
        if name is None:
            self.name = Human.default_name
        else:
            self.name = name
        if age is None:
            self.age = Human.default_age
        else:
            self.age = age
        self.__money = money
        self.__house = house

    def info(self):
        house_info = f"площа {self.__house._area} кв.м" if self.__house else "відсутній"
        print(f"Ім'я: {self.name}, Вік: {self.age}, Гроші: {self.__money}, Будинок: {house_info}")

    @staticmethod
    def default_info():
        print(f"Ім'я за замовчуванням: {Human.default_name}, Вік за замовчуванням: {Human.default_age}")

    def __make_deal(self, house, price):
        self.__money -= price
        self.__house = house

    def earn_money(self, amount):
        self.__money += amount
        print(f"Заробили {amount} грн! Поточний баланс: {self.__money}")

    def buy_house(self, house, discount=10):
        price = house.final_price(discount)
        if self.__money >= price:
            self.__make_deal(house, price)
            print("Будинок успішно куплено!")
        else:
            print("Недостатньо грошей для покупки цього будинку.")


if __name__ == '__main__':
    print("--- Тести Завдання 2 ---")
    Human.default_info()
    
    human = Human("Олексій", 25)
    human.info()
    
    small_house = SmallHouse(8500)
    
    print("Спроба купити будинок...")
    human.buy_house(small_house)
    
    human.earn_money(10000)
    print("Повторна спроба купити будинок...")
    human.buy_house(small_house)
    
    human.info()
