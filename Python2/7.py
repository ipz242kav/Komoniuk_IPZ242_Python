a = int(input("Введіть число a: 0<= a<= 50: "))
while a < 0 or a > 50:
    print("a повинно бути в діапазоні від 0 до 50")
    a = int(input("Введіть число a ще раз (0 <= a <= 50): "))

sumofsq = 0

for i in range(a, 51):
    sumofsq += i ** 2

print(f"Сума квадратів всіх цілих чисел від {a} до 50: {sumofsq}")
