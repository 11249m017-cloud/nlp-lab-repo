import nltk
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')
lemmatizer = WordNetLemmatizer()
words = ["cars", "studies", "playing", "better", "children"]
for word in words:
    print(word, "->", lemmatizer.lemmatize(word))
