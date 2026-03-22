A = int(input("Введіть число A: "))
B = int(input("Введіть число B<A: "))

if A > B:
    A, B = B, A

sum = 0

for i in range(A, B + 1):
    sum += i ** 2

print(f"Сума квадратів всіх цілих чисел від {A} до {B} включно: {sum}")
