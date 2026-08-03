import nltk
from nltk.stem import WordNetLemmatizer

nltk.download('wordnet')

verb = input("Enter a verb: ")

lemmatizer = WordNetLemmatizer()

past = lemmatizer.lemmatize(verb, pos="v")

print("Base Form :", past)