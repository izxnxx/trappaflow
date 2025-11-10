
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))

print(f"Початковий список: {numbers}")
print(f"Парні елементи: {even_numbers}")
print(f"Непарні елементи: {odd_numbers}")
print(f"Кількість парних елементів: {len(even_numbers)}")
print(f"Кількість непарних елементів: {len(odd_numbers)}")