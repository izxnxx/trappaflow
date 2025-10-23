import hashlib
import string
import itertools


def brute_force_single_hash(target_hash):

    characters = string.ascii_lowercase + string.digits
    password_length = 6

    print(" Початок brute-force атаки...")
    print(f" Цільовий хеш: {target_hash}")
    print(f" Можливі символи: {characters}")
    print(f" Довжина паролю: {password_length}")
    print(f" Кількість комбінацій: {len(characters) ** password_length:,}")
    print(" Пошук...")

    attempts = 0

    # Генеруємо всі можливі комбінації
    for password_tuple in itertools.product(characters, repeat=password_length):
        password = ''.join(password_tuple)
        attempts += 1

        # Обчислюємо хеш поточного паролю
        password_hash = hashlib.sha256(password.encode()).hexdigest()

        # Перевіряємо чи збігається з цільовим хешем
        if password_hash == target_hash:
            print(f" ПАРОЛЬ ЗНАЙДЕНО!")
            print(f" Пароль: {password}")
            print(f" Витрачено спроб: {attempts:,}")
            return password, attempts

        # Виводимо прогрес кожні 1 000 000 спроб
        if attempts % 1000000 == 0:
            print(f"🔍 Перевірено {attempts:,} комбінацій...")

    print(" Пароль не знайдено")
    return None, attempts


def optimized_brute_force(target_hash):
    """
    Оптимізована версія з вкладеними циклами (швидше)
    """
    characters = string.ascii_lowercase + string.digits
    attempts = 0

    print("🚀 Запуск оптимізованого пошуку...")

    for a in characters:
        for b in characters:
            for c in characters:
                for d in characters:
                    for e in characters:
                        for f in characters:
                            password = a + b + c + d + e + f
                            password_hash = hashlib.sha256(password.encode()).hexdigest()
                            attempts += 1

                            if password_hash == target_hash:
                                print(f" ПАРОЛЬ ЗНАЙДЕНО!")
                                print(f" Пароль: {password}")
                                print(f" Витрачено спроб: {attempts:,}")
                                return password, attempts

                            if attempts % 1000000 == 0:
                                print(f"🔍 Перевірено {attempts:,} комбінацій...")

    return None, attempts


def main():
    target_hash = "d97a630ec8cbf645e93426bb0b1ab2a19bc7c18d35a4a0873381f18f273fee22"

    print("=" * 60)
    print("           BRUTE-FORCE АТАКА SHA-256")
    print("=" * 60)
    print("Параметри пошуку:")
    print("• Довжина паролю: 6 символів")
    print("• Символи: a-z, 0-9")
    print("• Кількість комбінацій: 36^6 = 2 176 782 336")
    print("=" * 60)

    password, attempts = optimized_brute_force(target_hash)

    if password:
        print("\n АТАКА УСПІШНА!")
        print(f" Знайдений пароль: {password}")
        print(f" Загальна кількість спроб: {attempts:,}")
    else:
        print("\n Пароль не знайдено серед 6-символьних комбінацій")


if __name__ == "__main__":
    main()