import nltk
from nltk import bigrams
from nltk.tokenize import word_tokenize
from collections import Counter
nltk.download('punkt')
text = input("Enter a sentence: ")
tokens = word_tokenize(text)
bg = list(bigrams(tokens))

freq = Counter(bg)
print("Bigram Frequencies:")
for k, v in freq.items():
    print(k, ":", v)