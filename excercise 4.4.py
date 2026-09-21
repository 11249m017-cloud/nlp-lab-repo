import nltk
from nltk.util import  trigrams
from nltk.tokenize import word_tokenize
from collections import Counter
nltk.download('punkt')

text = input("Enter a sentence: ")

tokens = word_tokenize(text)
tg= list(trigrams(tokens))
freq= Counter(tg)
print ("Trigram frequencies")
for K,v in freq.items():
    print(K,":",v)