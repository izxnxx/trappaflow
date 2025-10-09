import math

#5
print("\n5. Генерація RSA ключа та шифрування")

p = 92082699061035365227
q = 26211616892502183343
e = 19094582240573146889

n = p * q
phi = (p - 1) * (q - 1)
d = pow(e, -1, phi)

print(f"p = {p}\nq = {q}\nn = {n}\ne = {e}\nd = {d}")
print(f"Довжина n (цифр): {len(str(n))}, в бітах: {n.bit_length()}")
print(f"Hex n: {hex(n)}")
print(f"gcd(e, φ(n)) = {math.gcd(e, phi)}")

msg = "whats up wid it"
msg_bytes = msg.encode('utf-8')
m_int = int.from_bytes(msg_bytes, 'big')
c_int = pow(m_int, e, n)

dec_int = pow(c_int, d, n)

orig_len = len(msg_bytes)
dec_bytes = dec_int.to_bytes((dec_int.bit_length() + 7) // 8, 'big')
dec_bytes = dec_bytes.rjust(orig_len, b'\x00')
msg_dec = dec_bytes.decode('utf-8')

print("\nПовідомлення:", msg)
print("Число для шифрування:", m_int)
print("Зашифровано (int):", c_int)
print("Розшифровано (int):", dec_int)
print("Розшифровано (текст):", msg_dec)