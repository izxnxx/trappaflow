
def validate_password(password):
    uppercase_count = 0

    print("┌────────────────────────────────────────────┐")
    print("│            АНАЛІЗ ПАРОЛЯ                  │")
    print("├────────────────────────────────────────────┤")

    for char in password:
        if 'A' <= char <= 'Z':
            uppercase_count += 1

    print(f"│ Введений пароль: {password:<20} │")
    print("├────────────────────────────────────────────┤")
    print(f"│ Великих латинських літер: {uppercase_count:<4}          │")

    if uppercase_count >= 5:
        print("│ Статус: Пароль відповідає вимогам   │")
        print("└────────────────────────────────────────────┘")
        return True
    else:
        print("│ Статус: Пароль НЕ відповідає вимогам│")
        print("└────────────────────────────────────────────┘")
        return False


def main():
    print("=" * 50)
    print("          СИСТЕМА ПЕРЕВІРКИ ПАРОЛЯ")
    print("=" * 50)
    print("Вимоги до пароля:")
    print("• Не менше 5 великих латинських літер (A-Z)")
    print("=" * 50)

    while True:
        password = input("Введіть пароль для перевірки: ")

        if not password:
            print(" Пароль не може бути порожнім. Спробуйте ще раз.\n")
            continue

        print()

        is_valid = validate_password(password)

        print()

        if is_valid:
            print(" Пароль успішно пройшов перевірку!")
            break
        else:
            print(" Пароль не відповідає вимогам. Спробуйте інший пароль.\n")
            print("=" * 50)


# Запуск програми
if __name__ == "__main__":
    main()