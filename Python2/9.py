n = int(input("Введіть число n: "))

result = 0
result_i = 0

for i in range(1, n + 100):
    square = i ** 2
    if square > n:
        result = square
        result_i = i
        break

if result is not None:
    print(f"Перше число з послідовності 1, 4, 9, 16, 25,    більше {n}: {result}")
    print(f"Це квадрат числа {result_i}: {result_i}^2 = {result}")
