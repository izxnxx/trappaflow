# 3. Перетворення дати народження
print("\n3. Перетворення дати народження у число, біти і байти")
birth_number = 20080615
bits = birth_number.bit_length()
print(f"Число: {birth_number}\nКількість бітів: {bits}\nКількість байтів: {(bits + 7) // 8}")
