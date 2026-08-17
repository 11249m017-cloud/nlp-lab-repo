import nltk
from nltk import trigrams
from nltk.tokenize import word_tokenize
from collections import Counter
nltk.download('punkt')

text = input("Enter a sentence: ")
tokens = word_tokenize(text)
tg = list(trigrams(tokens))
freq = Counter(tg)
print("Trigram Frequencies:")
for k, v in freq.items():
    print(k, ":", v)