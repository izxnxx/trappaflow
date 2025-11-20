import hashlib
import requests

def check_password(password: str) -> int:

    try:
        sha1 = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
        prefix = sha1[:5]
        suffix = sha1[5:]

        url = f"https://api.pwnedpasswords.com/range/{prefix}"
        response = requests.get(url)
        if response.status_code != 200:
            return -1

        hashes = response.text.splitlines()
        for line in hashes:
            hash_suffix, count = line.split(":")
            if hash_suffix == suffix:
                return int(count)

        return 0
    except Exception:
        return -1


def check_passwords_generator(password_dict: dict[str, str]):

    for user, pwd in password_dict.items():
        result = check_password(pwd)
        if result == 0:
            yield user

if __name__ == "__main__":
    test_passwords = {
        "user1": "TestPassword123!",
        "user2": "qwerty123",
        "user3": "abcdXYZ123!@"
    }

    for valid_user in check_passwords_generator(test_passwords):
        print(f"Пароль користувача {valid_user} валідний і не знайдений у витоках")
