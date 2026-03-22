a = float(input("Введіть основу трикутника: "))
h = float(input("Введіть висоту трикутника: "))

area = 0.5 * a * h

print(f"Площа трикутника: {area}")

if area % 2 == 0:
    print(f"Площа ділена на 2: {area / 2}")
else:
    print("Не можу ділити на 2!")
