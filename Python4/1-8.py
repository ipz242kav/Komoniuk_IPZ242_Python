import random

print("Завдання 1: Знайти максимальний елемент та вивести список у зворотному порядку")
print()

while True:
    try:
        n = int(input("Введіть кількість елементів списку (N): "))
        if n > 0:
            break
        else:
            print("Кількість елементів має бути більше 0, спробуйте ще раз")
    except ValueError:
        print("Будь ласка, введіть ціле число")

numbers = []
print(f"Введіть {n} цілих чисел:")
for i in range(n):
    while True:
        try:
            num = int(input(f"Елемент {i + 1}: "))
            numbers.append(num)
            break
        except ValueError:
            print("Будь ласка, введіть ціле число")

max_element = numbers[0]
for num in numbers:
    if num > max_element:
        max_element = num

reversed_list = []
for i in range(len(numbers) - 1, -1, -1):
    reversed_list.append(numbers[i])

print(reversed_list.reverse())

print()
print("Оригінальний список:")
print(numbers)
print()
print(f"Максимальний елемент: {max_element}")
print()
print("Список у зворотному порядку:")
print(reversed_list)
print()
print()

print("Завдання 2: Розділити список на додатні та недодатні елементи")
print()

while True:
    try:
        n = int(input("Введіть кількість елементів списку (N): "))
        if n > 0:
            break
        else:
            print("Кількість елементів має бути більше 0, спробуйте ще раз")
    except ValueError:
        print("Будь ласка, введіть ціле число")

numbers = []
print(f"Введіть {n} цілих чисел:")
for i in range(n):
    while True:
        try:
            num = int(input(f"Елемент {i + 1}: "))
            numbers.append(num)
            break
        except ValueError:
            print("Будь ласка, введіть ціле число")

positive_list = []
other_list = []

for num in numbers:
    if num > 0:
        positive_list.append(num)
    else:
        other_list.append(num)

print()
print("Оригінальний список:")
print(numbers)
print()
print("Додатні елементи:")
print(positive_list)
print()
print("Недодатні елементи (нуль та від'ємні):")
print(other_list)
print()
print()

print("Завдання 3: Обчислити суму елементів з непарними індексами")
print()

numbers = []
print("Введіть 20 цілих чисел:")
for i in range(20):
    while True:
        try:
            num = int(input(f"Елемент {i + 1}: "))
            numbers.append(num)
            break
        except ValueError:
            print("Будь ласка, введіть ціле число")

sum_odd_indices = 0
for i in range(len(numbers)):
    if i % 2 == 1:
        sum_odd_indices = sum_odd_indices + numbers[i]

print()
print("Список:")
print(numbers)
print()
print(f"Сума елементів з непарними індексами: {sum_odd_indices}")
print()
print()

print("Завдання 4: Робота з випадковим списком: максимум та непарні числа")
print()

numbers = []
for i in range(30):
    num = random.randint(-100, 100)
    numbers.append(num)

print("Сформований список:")
print(numbers)
print()

max_element = numbers[0]
max_index = 0
for i in range(len(numbers)):
    if numbers[i] > max_element:
        max_element = numbers[i]
        max_index = i

print(f"Максимальний елемент: {max_element}")
print(f"Порядковий номер (індекс): {max_index}")
print()

odd_numbers = []
for num in numbers:
    if num % 2 != 0:
        odd_numbers.append(num)

if len(odd_numbers) == 0:
    print("У списку немає непарних чисел")
else:
    for i in range(len(odd_numbers)):
        for j in range(len(odd_numbers) - 1 - i):
            if odd_numbers[j] < odd_numbers[j + 1]:
                temp = odd_numbers[j]
                odd_numbers[j] = odd_numbers[j + 1]
                odd_numbers[j + 1] = temp

    print("Непарні числа в порядку зменшення:")
    print(odd_numbers)
print()
print()

print("Завдання 5: Вивести пари від'ємних чисел, що стоять поруч")
print()

numbers = []
for i in range(30):
    num = random.randint(-100, 100)
    numbers.append(num)

print("Сформований список:")
print(numbers)
print()

pairs_found = False
print("Пари від'ємних чисел, що стоять поруч:")

for i in range(len(numbers) - 1):
    if numbers[i] < 0 and numbers[i + 1] < 0:
        print(f"Пара на позиціях {i} та {i + 1}: ({numbers[i]}, {numbers[i + 1]})")
        pairs_found = True

if pairs_found == False:
    print("Пар від'ємних чисел не знайдено")
print()
print()

print("Завдання 6: Квадрати менших за максимум чисел")
print()

numbers = []
print("Введіть 10 цілих чисел:")
for i in range(10):
    while True:
        try:
            num = int(input(f"Елемент {i + 1}: "))
            numbers.append(num)
            break
        except ValueError:
            print("Будь ласка, введіть ціле число")

print()
print("Введений список:")
print(numbers)
print()

max_element = numbers[0]
for num in numbers:
    if num > max_element:
        max_element = num

print(f"Максимальний елемент: {max_element}")
print()

squares = []
for num in numbers:
    if num < max_element:
        square = num * num
        squares.append(square)

for i in range(len(squares)):
    for j in range(len(squares) - 1 - i):
        if squares[j] < squares[j + 1]:
            temp = squares[j]
            squares[j] = squares[j + 1]
            squares[j + 1] = temp

print("Квадрати чисел, менших за максимум (в порядку зменшення):")
print(squares)
print()
print()

print("Завдання 7: Мінімальний по модулю елемент та сортування")
print()

numbers = []
for i in range(30):
    if random.choice([True, False]):
        num = random.randint(-100, 100)
    else:
        num = random.uniform(-100, 100)
    numbers.append(num)

print("Сформований список:")
for i in range(len(numbers)):
    print(f"{numbers[i]:.2f}", end=" ")
print()
print()

min_abs_element = numbers[0]
for num in numbers:
    if abs(num) < abs(min_abs_element):
        min_abs_element = num

print(f"Мінімальний по модулю елемент: {min_abs_element:.2f}")
print()

for i in range(len(numbers)):
    for j in range(len(numbers) - 1 - i):
        if numbers[j] > numbers[j + 1]:
            temp = numbers[j]
            numbers[j] = numbers[j + 1]
            numbers[j + 1] = temp

print("Список в порядку збільшення:")
for i in range(len(numbers)):
    print(f"{numbers[i]:.2f}", end=" ")
print()
print()
print()

print("Завдання 8: Розділення списку на підсписки та сортування за сумою модулів")
print()

numbers = []
for i in range(30):
    if random.choice([True, False]):
        num = random.randint(-100, 100)
    else:
        num = random.uniform(-100, 100)
    numbers.append(num)

print("Сформований список:")
for i in range(len(numbers)):
    print(f"{numbers[i]:.2f}", end=" ")
print()
print()

sublists = []
for i in range(10):
    sublist = []
    for j in range(3):
        index = i * 3 + j
        sublist.append(numbers[index])
    sublists.append(sublist)

sums = []
for sublist in sublists:
    sum_abs = 0
    for num in sublist:
        sum_abs = sum_abs + abs(num)
    sums.append(sum_abs)

for i in range(len(sublists)):
    for j in range(len(sublists) - 1 - i):
        if sums[j] > sums[j + 1]:
            temp_sublist = sublists[j]
            sublists[j] = sublists[j + 1]
            sublists[j + 1] = temp_sublist
            temp_sum = sums[j]
            sums[j] = sums[j + 1]
            sums[j + 1] = temp_sum

print("Підсписки в порядку зростання за сумою абсолютних значень:")
for i in range(len(sublists)):
    print(f"Підсписок {i + 1}: ", end="")
    for num in sublists[i]:
        print(f"{num:.2f}", end=" ")
    print(f" | Сума модулів: {sums[i]:.2f}")
print()
print()


print("Всі завдання виконано")