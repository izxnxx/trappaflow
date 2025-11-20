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


def check_passwords(password_dict: dict[str, str]) -> dict[str, bool | None]:
    results = {}
    for user, pwd in password_dict.items():
        result = check_password(pwd)
        if result == 0:
            results[user] = True
        elif result == -1:
            results[user] = None
        else:
            results[user] = False
    return results

if __name__ == "__main__":
    test_passwords = {
        "user1": "TestPass123!",
        "user2": "qwerty123",
        "user3": "abcdXYZ123!@"
    }

    results = check_passwords(test_passwords)
    print(results)
