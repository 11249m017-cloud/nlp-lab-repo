import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')
text=input("Enter a sentence")
tokens = word_tokenize(text)
print("Tokens")
print(tokens)