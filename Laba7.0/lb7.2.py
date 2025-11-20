from typing import Dict, Tuple, List, Any

def count_chars(password: str) -> Tuple[int, int]:
    lower = sum(1 for c in password if 'a' <= c <= 'z')
    upper = sum(1 for c in password if 'A' <= c <= 'Z')
    return lower, upper

def check_charset(password: str) -> bool:
    return all(('a' <= c <= 'z') or ('A' <= c <= 'Z') for c in password)

def check_repeating_chars(password: str) -> List[str]:
    errors: List[str] = []

    for char in set(password):
        count = password.count(char)
        if 'a' <= char <= 'z' and count > 2:
            errors.append(f"Більше 2 однакових маленьких літер '{char}'")
    max_seq = 1
    curr_seq = 1
    for i in range(1, len(password)):
        if ('a' <= password[i] <= 'z' and
                'a' <= password[i - 1] <= 'z' and
                password[i] == password[i - 1]):
            curr_seq += 1
            max_seq = max(max_seq, curr_seq)
        else:
            curr_seq = 1
    if max_seq > 3:
        errors.append("Більше 3 однакових маленьких літер підряд")

    return errors

def validate_password(password: str) -> Tuple[bool, Dict[str, Any]]:
    result: Dict[str, Any] = {'is_valid': True, 'errors': [], 'stats': {}}

    if len(password) != 9:
        result['errors'].append("Некоректна довжина")

    if not check_charset(password):
        result['errors'].append("Містить заборонені символи")

    lower, upper = count_chars(password)
    result['stats'] = {'lower': lower, 'upper': upper, 'total': len(password)}

    if lower < 3:
        result['errors'].append("Менше 3 маленьких латинських літер")
    if lower > 6:
        result['errors'].append("Більше 6 маленьких латинських літер")
    if upper < 2:
        result['errors'].append("Менше 2 великих латинських літер")
    if upper > 5:
        result['errors'].append("Більше 5 великих латинських літер")

    result['errors'].extend(check_repeating_chars(password))

    result['is_valid'] = len(result['errors']) == 0
    return result['is_valid'], result

def print_result(password: str, result: Dict[str, Any]) -> None:
    print("АНАЛІЗ ПАРОЛЯ")
    print(f"Введений пароль: {password:<25} │")
    print(f"Загальна довжина: {result['stats']['total']:<4} символи")
    print(f"Маленьких латинських літер: {result['stats']['lower']:<4}")
    print(f"Великих латинських літер: {result['stats']['upper']:<4}")
    if result['is_valid']:
        print("Статус: Пароль відповідає вимогам")
    else:
        print("Статус: Пароль НЕ відповідає вимогам")
        if result['errors']:
            print("ПОМИЛКИ:")
            for error in result['errors']:
                if len(error) > 38:
                    for i in range(0, len(error), 38):
                        line = error[i:i + 38]
                        prefix = "" if i == 0 else ""
                        print(f"{prefix}{line:<37}")
                else:
                    print(f"{error:<37}")

def main() -> None:
    print("СИСТЕМА ПЕРЕВІРКИ ПАРОЛЯ")
    print("=" * 50)
    print("Вимоги до пароля (варіант 8):")
    print("• Довжина: 9 символів")
    print("• Тільки латинські літери (a-z, A-Z)")
    print("• 3-6 маленьких літер, 2-5 великих літер")
    print("• Максимум 2 однакові маленькі літери")
    print("• Максимум 3 однакові маленькі літери підряд")
    print("=" * 50)

    while True:
        password = input("Введіть пароль для перевірки: ").strip()
        if not password:
            print("Пароль не може бути порожнім\n")
            continue

        is_valid, result = validate_password(password)
        print_result(password, result)

        if is_valid:
            print("Пароль успішно пройшов перевірку!")
            break
        else:
            print("Спробуйте інший пароль\n")

if __name__ == "__main__":
    main()