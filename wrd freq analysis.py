from collections import Counter
import nltk
from nltk.tokenize import word_tokenize

# Download tokenizer data (only the first time)
nltk.download('punkt')

# Input document
text = input("Enter a document: ")

# Convert text into words
words = word_tokenize(text)

# Count word frequency
frequency = Counter(words)

# Display word frequencies
print("Word Frequency:")

for word, count in frequency.items():
    if word.isalpha():
        print(word, ":", count)
