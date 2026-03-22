import random
from datetime import date


class Bank:
    def __init__(self, balance=0):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Поповнено на {amount} грн. Поточний баланс: {self.__balance} грн")
        else:
            print("Сума повинна бути додатною!")

    def withdraw(self, amount):
        if amount > 0:
            if self.__balance >= amount:
                self.__balance -= amount
                print(f"Знято {amount} грн. Поточний баланс: {self.__balance} грн")
            else:
                print(f"Недостатньо коштів! Поточний баланс: {self.__balance} грн")
        else:
            print("Сума повинна бути додатною!")

    def get_balance(self):
        return self.__balance


class Coin:
    def __init__(self):
        self.__sideup = random.choice(['heads', 'tails'])

    def toss(self):
        self.__sideup = random.choice(['heads', 'tails'])
        return self.__sideup

    def get_sideup(self):
        return self.__sideup


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.__speed = 0

    def accelerate(self):
        self.__speed += 5

    def brake(self):
        self.__speed -= 5
        if self.__speed < 0:
            self.__speed = 0

    def get_speed(self):
        return self.__speed


class Dog:
    mammal = "Ссавець"
    nature = "Дружелюбний"
    breed = "Загальна"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def describe(self):
        print(f"Кличка: {self.name}")
        print(f"Вік: {self.age} років")
        print(f"Тип: {self.mammal}")
        print(f"Характер: {self.nature}")
        print(f"Порода: {self.breed}")

    def bark(self):
        print(f"{self.name} гавкає: Гав-гав!")


class GoldenRetriever(Dog):
    nature = "Дуже дружелюбний"
    breed = "Золотистий ретрівер"

    def fetch(self):
        print(f"{self.name} приносить м'яч!")


class Bulldog(Dog):
    nature = "Спокійний"
    breed = "Бульдог"

    def guard(self):
        print(f"{self.name} охороняє будинок!")


class Husky(Dog):
    nature = "Енергійний"
    breed = "Хаскі"

    def howl(self):
        print(f"{self.name} виє: Ауууу!")


class Pets:
    def __init__(self):
        self.pets_list = []

    def add_pet(self, pet):
        self.pets_list.append(pet)

    def show_all_pets(self):
        print("=" * 50)
        print("МОЇ ДОМАШНІ УЛЮБЛЕНЦІ")
        print("=" * 50)
        for i, pet in enumerate(self.pets_list, 1):
            print(f"\n--- Улюбленець #{i} ---")
            pet.describe()


class Buffer:
    def __init__(self):
        self.__buffer = []

    def add(self, *a):
        self.__buffer.extend(a)

        while len(self.__buffer) >= 5:
            five_elements = self.__buffer[:5]
            print(sum(five_elements))
            self.__buffer = self.__buffer[5:]

    def get_current_part(self):
        return self.__buffer.copy()


class NameTooShortError(ValueError):
    def __init__(self, name, min_length=10):
        self.name = name
        self.min_length = min_length
        self.message = f"Ім'я '{name}' занадто коротке! Мінімальна довжина: {min_length} символів."
        super().__init__(self.message)


def validate_name(name):
    if len(name) < 10:
        raise NameTooShortError(name)
    else:
        print(f"Ім'я '{name}' прийнято успішно!")


class DecimalToRoman:
    def __init__(self):
        self.values = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]

    def convert(self, num):
        if not 1 <= num <= 3999:
            raise ValueError("Число має бути в діапазоні 1-3999")

        result = ""
        for value, letter in self.values:
            count = num // value
            if count:
                result += letter * count
                num -= value * count
        return result


class RomanToDecimal:
    def __init__(self):
        self.values = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }

    def convert(self, roman):
        roman = roman.upper()
        result = 0
        prev_value = 0

        for char in reversed(roman):
            if char not in self.values:
                raise ValueError(f"Невірний символ: {char}")

            value = self.values[char]
            if value < prev_value:
                result -= value
            else:
                result += value
            prev_value = value

        return result


class Shop:
    def __init__(self, shop_name, store_type):
        self.shop_name = shop_name
        self.store_type = store_type
        self.number_of_units = 0

    def describe_shop(self):
        print(f"Назва магазину: {self.shop_name}")
        print(f"Тип магазину: {self.store_type}")

    def open_shop(self):
        print(f"Онлайн-магазин '{self.shop_name}' відкритий!")

    def set_number_of_units(self, number):
        self.number_of_units = number

    def increment_number_of_units(self, increment):
        self.number_of_units += increment


class Discount(Shop):
    def __init__(self, shop_name, store_type):
        super().__init__(shop_name, store_type)
        self.discount_products = []

    def get_discounts_products(self):
        print("Товари зі знижкою:")
        for product in self.discount_products:
            print(f"  - {product}")


class User:
    def __init__(self, first_name, last_name, email, nickname, newsletter=True):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.nickname = nickname
        self.newsletter = newsletter
        self.login_attempts = 0

    def describe_user(self):
        print(f"Повне ім'я: {self.first_name} {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Нікнейм: {self.nickname}")
        print(f"Підписка на новини: {'Так' if self.newsletter else 'Ні'}")

    def greeting_user(self):
        print(f"Вітаємо, {self.nickname}! Раді бачити вас знову!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Privileges:
    def __init__(self):
        self.privileges = [
            "Allowed to add message",
            "Allowed to delete users",
            "Allowed to ban users",
            "Allowed to modify settings"
        ]

    def show_privileges(self):
        print("Привілеї адміністратора:")
        for privilege in self.privileges:
            print(f"  - {privilege}")


class Admin(User):
    def __init__(self, first_name, last_name, email, nickname, newsletter=True):
        super().__init__(first_name, last_name, email, nickname, newsletter)
        self.priv = Privileges()


if __name__ == "__main__":

    while True:
        print("\n" + "="*70)
        print("МЕНЮ")
        print("="*70)
        print("1. Банк (Bank)")
        print("2. Монета (Coin)")
        print("3. Автомобіль (Car)")
        print("4. Собаки та улюбленці (Dog & Pets)")
        print("5. Буфер (Buffer)")
        print("6. Перевірка імені (NameTooShortError)")
        print("7. Римські числа (Roman)")
        print("8. Магазин (Shop)")
        print("9. Користувачі (User & Admin)")
        print("0. Вихід")
        print("="*70)

        choice = input("\nОберіть завдання (0-9): ")

        if choice == "0":
            print("До побачення!")
            break

        elif choice == "1":
            print("\n--- БАНК ---")
            balance = float(input("Введіть початковий баланс: "))
            account = Bank(balance)

            while True:
                print(f"\nПоточний баланс: {account.get_balance()} грн")
                print("1. Поповнити  2. Зняти  3. Назад")
                action = input("Дія: ")

                if action == "1":
                    amount = float(input("Сума поповнення: "))
                    account.deposit(amount)
                elif action == "2":
                    amount = float(input("Сума зняття: "))
                    account.withdraw(amount)
                elif action == "3":
                    break

        elif choice == "2":
            print("\n--- МОНЕТА ---")
            coin = Coin()
            n = int(input("Скільки разів підкинути монету? "))

            heads = 0
            tails = 0
            for i in range(n):
                result = coin.toss()
                result_ua = "Орел" if result == "heads" else "Решка"
                print(f"Підкидання {i + 1}: {result_ua}")
                if result == "heads":
                    heads += 1
                else:
                    tails += 1

            print(f"\nСтатистика: Орел - {heads}, Решка - {tails}")

        elif choice == "3":
            print("\n--- АВТОМОБІЛЬ ---")
            make = input("Марка: ")
            model = input("Модель: ")
            year = int(input("Рік: "))
            car = Car(make, model, year)

            while True:
                print(f"\nАвтомобіль: {car.make} {car.model} ({car.year})")
                print(f"Поточна швидкість: {car.get_speed()} км/год")
                print("1. Прискорити  2. Загальмувати  3. Назад")
                action = input("Дія: ")

                if action == "1":
                    car.accelerate()
                    print(f"Швидкість: {car.get_speed()} км/год")
                elif action == "2":
                    car.brake()
                    print(f"Швидкість: {car.get_speed()} км/год")
                elif action == "3":
                    break

        elif choice == "4":
            print("\n--- СОБАКИ ТА УЛЮБЛЕНЦІ ---")
            my_pets = Pets()

            while True:
                print("\n1. Додати Golden Retriever")
                print("2. Додати Bulldog")
                print("3. Додати Husky")
                print("4. Показати всіх улюбленців")
                print("5. Назад")
                action = input("Дія: ")

                if action in ["1", "2", "3"]:
                    name = input("Кличка: ")
                    age = int(input("Вік: "))

                    if action == "1":
                        dog = GoldenRetriever(name, age)
                    elif action == "2":
                        dog = Bulldog(name, age)
                    else:
                        dog = Husky(name, age)

                    my_pets.add_pet(dog)
                    print(f"{name} додано до списку!")
                elif action == "4":
                    my_pets.show_all_pets()
                elif action == "5":
                    break

        elif choice == "5":
            print("\n--- БУФЕР ---")
            buf = Buffer()

            while True:
                print(f"\nПоточний буфер: {buf.get_current_part()}")
                print("1. Додати числа  2. Назад")
                action = input("Дія: ")

                if action == "1":
                    numbers = input("Введіть числа через пробіл: ")
                    nums = [int(x) for x in numbers.split()]
                    buf.add(*nums)
                elif action == "2":
                    break

        elif choice == "6":
            print("\n--- ПЕРЕВІРКА ІМЕНІ ---")
            name = input("Введіть ім'я (мін. 10 символів): ")
            try:
                validate_name(name)
            except NameTooShortError as e:
                print(f"ПОМИЛКА: {e}")

        elif choice == "7":
            print("\n--- РИМСЬКІ ЧИСЛА ---")
            print("1. Десяткове → Римське")
            print("2. Римське → Десяткове")
            action = input("Дія: ")

            if action == "1":
                num = int(input("Введіть число (1-3999): "))
                converter = DecimalToRoman()
                try:
                    roman = converter.convert(num)
                    print(f"{num} = {roman}")
                except ValueError as e:
                    print(f"Помилка: {e}")
            elif action == "2":
                roman = input("Введіть римське число: ")
                converter = RomanToDecimal()
                try:
                    decimal = converter.convert(roman)
                    print(f"{roman} = {decimal}")
                except ValueError as e:
                    print(f"Помилка: {e}")

        elif choice == "8":
            print("\n--- МАГАЗИН ---")
            name = input("Назва магазину: ")
            store_type = input("Тип магазину: ")
            store = Shop(name, store_type)

            while True:
                print()
                store.describe_shop()
                print(f"Кількість видів товару: {store.number_of_units}")
                print("\n1. Відкрити магазин")
                print("2. Встановити кількість товарів")
                print("3. Збільшити кількість товарів")
                print("4. Назад")
                action = input("Дія: ")

                if action == "1":
                    store.open_shop()
                elif action == "2":
                    num = int(input("Кількість видів товару: "))
                    store.set_number_of_units(num)
                elif action == "3":
                    num = int(input("На скільки збільшити: "))
                    store.increment_number_of_units(num)
                elif action == "4":
                    break

        elif choice == "9":
            print("\n--- КОРИСТУВАЧІ ---")
            print("1. Створити звичайного користувача")
            print("2. Створити адміністратора")
            action = input("Дія: ")

            if action in ["1", "2"]:
                first_name = input("Ім'я: ")
                last_name = input("Прізвище: ")
                email = input("Email: ")
                nickname = input("Нікнейм: ")

                if action == "1":
                    user = User(first_name, last_name, email, nickname)
                    user.describe_user()
                    user.greeting_user()

                    print("\nСимуляція спроб входу...")
                    for i in range(3):
                        user.increment_login_attempts()
                        print(f"Спроба {i + 1}: {user.login_attempts}")

                    user.reset_login_attempts()
                    print(f"Після скидання: {user.login_attempts}")

                elif action == "2":
                    admin = Admin(first_name, last_name, email, nickname)
                    admin.describe_user()
                    admin.greeting_user()
                    print()
                    admin.priv.show_privileges()