list = [11, 4, 22, 13, 21, 9, 14, 3, 20]

length = len(list)
print(f"Кількість елементів у списку: {length}")

print("Парні елементи списку:")
for element in list:
    if element % 2 == 0:
        print(element, end=" ")