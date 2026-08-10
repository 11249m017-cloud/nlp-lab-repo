import nltk
from nltk.stem import WordNetLemmatizer

nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()

words = [
    ("playing", "v"),
    ("studies", "v"),
    ("better", "a"),
    ("cars", "n"),
    ("children", "n")
]

for word, pos in words:
    print(word, "->", lemmatizer.lemmatize(word, pos=pos))