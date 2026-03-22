import csv
from datetime import date

class Person:
    def __init__(self, surname, first_name, birth_date, nickname=None):

        self.surname = surname
        self.first_name = first_name
        self.nickname = nickname

        if isinstance(birth_date, str):
            year, month, day = birth_date.split('-')
            year = int(year)
            month = int(month)
            day = int(day)
            self.birth_date = date(year, month, day)
        else:
            self.birth_date = birth_date

    def get_age(self):

        today = date.today()
        age = today.year - self.birth_date.year

        if (today.month, today.day) < (self.birth_date.month, self.birth_date.day):
            age -= 1

        return str(age)

    def get_fullname(self):

        return f"{self.surname} {self.first_name}"


def modifier(filename):

    persons = []

    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        original_fieldnames = reader.fieldnames

        for row in reader:
            person = Person(
                surname=row['surname'],
                first_name=row['first_name'],
                birth_date=row['birth_date'],
                nickname=row.get('nickname', None)
            )
            persons.append(person)

    new_fieldnames = []
    for field in original_fieldnames:
        new_fieldnames.append(field)
        if field == 'first_name':
            new_fieldnames.append('fullname')

    if 'age' not in new_fieldnames:
        new_fieldnames.append('age')

    with open(filename, 'w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=new_fieldnames)
        writer.writeheader()

        for person in persons:
            row_data = {
                'surname': person.surname,
                'first_name': person.first_name,
                'fullname': person.get_fullname(),
                'birth_date': person.birth_date.strftime('%Y-%m-%d'),
                'age': person.get_age()
            }

            if 'nickname' in new_fieldnames:
                row_data['nickname'] = person.nickname if person.nickname else ''

            writer.writerow(row_data)

    print(f"Файл {filename} успішно модифіковано!")
    print(f"Додано колонки: 'fullname' (після first_name) та 'age' (в кінці)")


if __name__ == "__main__":
    print("ЗАВДАННЯ 1: Тестування класу Person")
    person1 = Person("Шевченко", "Тарас", "2000-03-09", "Кобзар")
    print(f"Повне ім'я: {person1.get_fullname()}")
    print(f"Вік: {person1.get_age()}")
    print(f"Псевдонім: {person1.nickname}")

    person2 = Person("Іваненко", "Іван", "1995-12-31")
    print(f"\nПовне ім'я: {person2.get_fullname()}")
    print(f"Вік: {person2.get_age()}")
    print(f"Псевдонім: {person2.nickname}")

    print("\nЗАВДАННЯ 2: Модифікація файлу")
    modifier('contacts.csv')
