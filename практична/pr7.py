a = int(input("Введіть перше число (1-1000): "))
b = int(input("Введіть друге число (1-1000): "))

max_value = a * (a >= b) + b * (b > a)

print("Найбільше значення:", max_value)