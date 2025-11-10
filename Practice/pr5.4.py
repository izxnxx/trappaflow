def reverse_string():
    word = input("Правильне слово: ")
    return ''.join(reversed(word))

result = reverse_string()
print(f"Зворотнє слово :{result}")