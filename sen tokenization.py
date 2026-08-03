import nltk
from nltk.tokenize import sent_tokenize
nltk.download('punkt')
text= input("Enter a paragraph")
sentences= sent_tokenize(text)
for i, sentence in enumerate (sentences, start =1):
    print(f"Sentence {i}: {sentence}")
