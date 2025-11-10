def count_letters():
    text = input("Введіть рядок для аналізу: ")
    upper_count = 0
    lower_count = 0

    for char in text:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

    print(f"Рядок: '{text}'")
    print(f"Великих літер: {upper_count}")
    print(f"Малих літер: {lower_count}")

    return upper_count, lower_count

count_letters()