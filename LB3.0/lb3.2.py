from colorama import Fore, Style

up_c = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
low_c = "abcdefghijklmnopqrstuvwxyz"
num_c = "0123456789"
spc_c = "!@#$%^&*_-"

print("Введіть пароль довжиною не менше 9 символів.")
print("Вимоги до паролю:")
print("1. Великі літери")
print("2. Маленькі літери")
print("3. Цифри")
print("4. Спеціальні символи !@#$%^&*_-")

password = input("> ")

has_upper = sum(map(str.isupper, password)) > 0
has_lower = sum(map(str.islower, password)) > 0
has_digit = sum(map(str.isdigit, password)) > 0
has_special = len(password.strip(low_c + up_c)) > 0
has_length = len(password) <= 9

print((Fore.GREEN + "Довжина не менше 9 символів – OK!" + Style.RESET_ALL) * has_length +
      (Fore.RED + "Довжина не менше 9 символів – FAIL!" + Style.RESET_ALL) * (not has_length))
print((Fore.GREEN + "Великі літери – OK!" + Style.RESET_ALL) * has_upper +
      (Fore.RED + "Великі літери – FAIL!" + Style.RESET_ALL) * (not has_upper))
print((Fore.GREEN + "Маленькі літери – OK!" + Style.RESET_ALL) * has_lower +
      (Fore.RED + "Маленькі літери – FAIL!" + Style.RESET_ALL) * (not has_lower))
print((Fore.GREEN + "Цифри – OK!" + Style.RESET_ALL) * has_digit +
      (Fore.RED + "Цифри – FAIL!" + Style.RESET_ALL) * (not has_digit))
print((Fore.GREEN + "Спеціальні символи – OK!" + Style.RESET_ALL) * has_special +
      (Fore.RED + "Спеціальні символи – FAIL!" + Style.RESET_ALL) * (not has_special))

is_valid = all([has_length, has_upper, has_lower, has_digit, has_special])

print((Fore.GREEN + "\nПароль валідний!" + Style.RESET_ALL) * is_valid +
      (Fore.RED + "\nПароль не валідний!" + Style.RESET_ALL) * (not is_valid))