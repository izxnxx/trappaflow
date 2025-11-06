last_name = "Гресько"
first_name = "Владислав"
middle_name = "Ігорович"

set1 = set(last_name)
set2 = set(first_name)
set3 = set(middle_name)

ukr_alphabet = set("абвтдеежамйіїклинопрстуфхцчищьюя")

print("set1 (прізвище):", set1)
print("set2 (ім'я):", set2)
print("set3 (по батькові):", set3)
print("a) Літери, які є в set2 і set3:", set2 & set3)
print("b) Літери, які є в set1 або set2:", set1 | set2)
print("c) Літери set2, яких немає в set1:", set2 - set1)
print("d) Чи є set1 підмножиною set3:", set1.issubset(set3))
print("e) Симетрична різниця set1 і set2:", set1 ^ set2)

only_one = (set1 ^ set2 ^ set3) - (set1 & set2) - (set1 & set3) - (set2 & set3)
print("f) Літери лише в одній множині:", only_one)

print("g) Літери алфавіту, яких немає у ПІБ:", ukr_alphabet - (set1 | set2 | set3))