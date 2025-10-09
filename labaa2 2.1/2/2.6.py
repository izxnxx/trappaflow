#6
print("\n6. XOR шифрування та розшифрування")
key = 42
text = "HELLO"
enc_bytes = bytes([b ^ key for b in text.encode()])
dec_bytes = bytes([b ^ key for b in enc_bytes])
print("Оригінал:", text)
print("Зашифровано:", enc_bytes)
print("Розшифровано:", dec_bytes.decode())
