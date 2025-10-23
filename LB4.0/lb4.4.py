def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None


def affine_decrypt(ciphertext, a, b):

    ukr_letters = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'
    m = len(ukr_letters)  # 33

    a_inv = mod_inverse(a, m)
    if a_inv is None:
        raise ValueError(f"Число {a} не має оберненого елемента mod {m}")

    decrypted_text = ""

    for char in ciphertext:
        if char.lower() in ukr_letters:
            c_index = ukr_letters.index(char.lower())

            p_index = (a_inv * (c_index - b)) % m

            decrypted_char = ukr_letters[p_index]

            if char.isupper():
                decrypted_text += decrypted_char.upper()
            else:
                decrypted_text += decrypted_char
        else:
            decrypted_text += char

    return decrypted_text

a = 14
b = 19
ciphertext = "sxyuxi_wen@ cuikneq ur ynie uxneii"

print("Параметри шифру:")
print(f"a = {a}, b = {b}")
print(f"Шифротекст: {ciphertext}")
print()

try:
    decrypted_text = affine_decrypt(ciphertext, a, b)
    print("Результат розшифрування:")
    print(decrypted_text)


except ValueError as e:
    print(f"Помилка: {e}")