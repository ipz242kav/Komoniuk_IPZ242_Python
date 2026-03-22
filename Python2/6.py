a = int(input("Введіть число a: "))
b = int(input("Введіть число b (b >= a): "))

while b < a:
    print("Помилка: b повинно бути більше або дорівнювати a")
    b = int(input("Введіть число b ще раз (b >= a): "))

sumofn = 0
i = a

while i <= b:
    sumofn += i
    i += 1

print(f"Сума всіх цілих чисел від {a} до {b}: {sumofn}")
