import nltk
from nltk.util import bigrams
from nltk.tokenize import word_tokenize
from collections import defaultdict
nltk.download('punkt')

text = input("Enter a sentence: ")

tokens = word_tokenize(text)
model= defaultdict(list)
for w1,w2 in bigrams (tokens):
    model[w1].append(w2)
word= input("enter a word")
if word in model:
    print("possible next words:", model[word])
else:
    print("no pred available")