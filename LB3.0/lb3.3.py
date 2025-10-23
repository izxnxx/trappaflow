import secrets

print("Гресько Владислав Ігорович, КБ-106, 2025. Варіант 8")
print("low_char(5) + upp_char(4)")

upp_count = int(input("Введіть кількість великих латинських літер в паролі: "))
low_count = int(input("Введіть кількість малих латинських літер в паролі: "))
dig_count = int(input("Введіть кількість цифр в паролі: "))
spec_count = int(input("Введіть кількість спеціальних символів !@#$_-%^&* в паролі: "))

upp_char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
low_char = "abcdefghijklmnopqrstuvwxyz"
num_char = "0123456789"
spc_char = "!@#$_-%^&*"

password = ''.join(secrets.choice(upp_char) for _ in range(upp_count)) + \
           ''.join(secrets.choice(low_char) for _ in range(low_count)) + \
           ''.join(secrets.choice(num_char) for _ in range(dig_count)) + \
           ''.join(secrets.choice(spc_char) for _ in range(spec_count))

password_list = list(password)
secrets.SystemRandom().shuffle(password_list)
final_password = ''.join(password_list)

print(f"Password: {final_password}")