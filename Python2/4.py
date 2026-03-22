A = int(input("Введіть число A: "))
B = int(input("Введіть число B (B > A): "))

total = 0
for i in range(A, B + 1):
    total += i

print(f"Сума всіх чисел від {A} до {B}: {total}")

