import math

print("Гресько Владислав (Варіант №8)")
print("Формула: (sin(z + x) + (x + y)^e - sin(ln(1 + |y|))) / cos(y - z)")
print("\nВведіть значення змінних:")

x = float(input("x = "))
y = float(input("y = "))
z = float(input("z = "))

num = math.sin(z + x) + pow(x + y, math.e) - math.sin(math.log(1 + abs(y)))
denominator = math.cos(y - z)
F = num / denominator

F_rounded = round(F, 2)

print("\n=== РЕЗУЛЬТАТ ===")
print(f"x = {x}, y = {y}, z = {z}")
print(f"F (без округлення) = {F}")
print(f"F (округлено до 2 знаків) = {F_rounded}")
