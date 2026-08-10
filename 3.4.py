from nltk.stem import PorterStemmer

ps = PorterStemmer()

words = ["unhappy", "playing", "played", "happiness", "connected"]

print("Word\t\tStem")
print("----------------------")

for word in words:
    print(word, "\t\t", ps.stem(word))