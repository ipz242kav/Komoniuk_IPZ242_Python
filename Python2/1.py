import random

numbers = [random.randint(0, 100) for i in range(15)]
print("Всі числа:", numbers)

firsthalf = [num for num in numbers if num <= 50]
print("Числа першої половини 0-50:", firsthalf)
