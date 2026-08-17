import nltk
from nltk.util import ngrams
from nltk.tokenize import word_tokenize
nltk.download('punkt')
text = input("Enter a sentence: ")
n = int(input("Enter the value of n: "))
tokens = word_tokenize(text)
print(f"{n}-Grams:")

for gram in ngrams(tokens, n):
    print(gram)