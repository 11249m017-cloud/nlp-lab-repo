from nltk.stem import PorterStemmer
ps= PorterStemmer()
words=["playing","played","plays","Studies","Connected"]
for word in words:
    print (word,">",ps.stem(word))