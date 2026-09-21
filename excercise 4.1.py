import nltk
from nltk.util import ngrams
from nltk.tokenize import word_tokenize

nltk.download('punkt')

text = input("Enter a sentence: ")

tokens = word_tokenize(text)

print("Unigrams:")
print(list(ngrams(tokens, 1)))

print("\nBigrams:")
print(list(ngrams(tokens, 2)))

print("\nTrigrams:")
print(list(ngrams(tokens, 3)))

