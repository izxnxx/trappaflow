lst = ["Java", "Algol", "Python"]


result = max(lst, key=lambda word: word.lower().count('a'))

print(f"Елемент з максимальною частотою 'а': {result}")
print(f"Кількість 'а' в слові '{result}': {result.lower().count('a')}")