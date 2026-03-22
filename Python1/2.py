a = float((input("Введіть перше число")))
b = float((input("Введіть друге число")))

addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b
power = a ** b
floor = a // b
modul = a % b

results = [addition, subtraction, multiplication, division, power, floor, modul]

print(f"Додавання: {a} + {b} = {addition}")
print(f"Віднімання: {a} - {b} = {subtraction}")
print(f"Множення: {a} * {b} = {multiplication}")
print(f"Ділення: {a} / {b} = {division}")
print(f"Піднесення до ступеня: {a} ** {b} = {power}")
print(f"Цілочисленне ділення: {a} // {b} = {floor}")
print(f"Остача від ділення: {a} % {b} = {modul}")
print(f"Список результатів: {results}")
