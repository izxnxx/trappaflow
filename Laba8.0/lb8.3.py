import zipfile

with zipfile.ZipFile("Variant 8.zip") as zf:
    with open("10-million-password-list-top-100000.txt", "r") as f:
        for line in f:
            password = line.strip()
            if len(password) == 4:
                try:
                    zf.extractall(pwd=password.encode())
                    print("Пароль:", password)
                    break
                except:
                    pass