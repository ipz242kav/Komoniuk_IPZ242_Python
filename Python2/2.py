num = float(input("Введіть суму покупки грн: "))

if num > 1000:
    discount = 0.05
    print("Знижка: 5%")
if num > 500:
    discount = 0.03
    print("Знижка: 3%")
else:
    discount = 0
    print("Знижка не надається")

fprice = num * (1 - discount)
damount = num * discount

print(f"Сума знижки: {damount:.2f} грн")
print(f"До сплати: {fprice:.2f} грн")