import re
from collections import Counter

with open('Енеїда.txt', 'r', encoding='utf-8') as file:
    text = file.read()

text = re.sub(r'[^\w\s]', '', text)
text = re.sub(r'\d+', '', text)
text = text.lower().strip()

words = text.split()
words = [word for word in words if len(word) >= 3]
word_freq = Counter(words)

bigrams = []
for word in words:
    for i in range(len(word) - 1):
        bigram = word[i:i+2]
        bigrams.append(bigram)

bigram_freq = Counter(bigrams)

sorted_words = sorted(word_freq.items(), key=lambda x: x[1])
least_common_words = sorted_words[:100]

sorted_bigrams = sorted(bigram_freq.items(), key=lambda x: x[1], reverse=True)
most_common_bigrams = sorted_bigrams[:50]

print("100 слів з найменшою частотою:")
for word, freq in least_common_words:
    print(f"{word}: {freq}")

print("\n50 пар літер з найбільшою частотою:")
for bigram, freq in most_common_bigrams:
    print(f"{bigram}: {freq}")