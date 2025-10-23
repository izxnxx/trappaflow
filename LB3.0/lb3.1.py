ukr_letters = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'
key = 8

anon_text = "цщцзуоип иочжйто хк ьжтп цщцзуоип, ґцз чцшюгюижьо чшжиоуж."

def caesar_decrypt(text, alphabet, key):
    alph_idx = {ch: i for i, ch in enumerate(alphabet)}
    n = len(alphabet)
    result = []
    for ch in text:
        if ch in alph_idx:
            i = alph_idx[ch]
            new_i = (i - key) % n
            result.append(alphabet[new_i])
        else:
            result.append(ch)
    return ''.join(result)

plaintext = caesar_decrypt(anon_text, ukr_letters, key)
print(plaintext)