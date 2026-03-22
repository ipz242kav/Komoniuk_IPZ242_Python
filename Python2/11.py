D = int(input("Введіть день (D): "))
M = int(input("Введіть місяць (M): "))

zodiac = ""

if (M == 1 and D >= 20) or (M == 2 and D <= 18):
    zodiac = "Водолій"
elif (M == 2 and D >= 19) or (M == 3 and D <= 20):
    zodiac = "Риби"
elif (M == 3 and D >= 21) or (M == 4 and D <= 19):
    zodiac = "Овен"
elif (M == 4 and D >= 20) or (M == 5 and D <= 20):
    zodiac = "Телець"
elif (M == 5 and D >= 21) or (M == 6 and D <= 21):
    zodiac = "Близнюки"
elif (M == 6 and D >= 22) or (M == 7 and D <= 22):
    zodiac = "Рак"
elif (M == 7 and D >= 23) or (M == 8 and D <= 22):
    zodiac = "Лев"
elif (M == 8 and D >= 23) or (M == 9 and D <= 22):
    zodiac = "Діва"
elif (M == 9 and D >= 23) or (M == 10 and D <= 22):
    zodiac = "Терези"
elif (M == 10 and D >= 23) or (M == 11 and D <= 22):
    zodiac = "Скорпіон"
elif (M == 11 and D >= 23) or (M == 12 and D <= 21):
    zodiac = "Стрілець"
elif (M == 12 and D >= 22) or (M == 1 and D <= 19):
    zodiac = "Козеріг"

print(f"Дата: {D}.{M}")
print(f"Знак Зодіаку: {zodiac}")
