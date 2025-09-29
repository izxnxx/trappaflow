
surname = input("Введіть прізвище: ").strip()
name = input("Введіть ім'я: ").strip()
year_str = input("Введіть рік народження: ").strip()


try:
    year = int(year_str)
except ValueError:
    year = year_str
print ()

print(f"{surname} {name}, {year} р. н.")
print()

print(f"Прізвище: {surname}")
print(f"Ім'я: {name}")
print(f"Рік народження: {year}")

