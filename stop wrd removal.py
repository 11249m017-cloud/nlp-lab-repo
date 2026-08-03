import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Download required NLTK data (only the first time)
nltk.download('punkt')
nltk.download('stopwords')

# Input sentence
text = input("Enter a sentence: ")

# Tokenize the sentence
words = word_tokenize(text)

# Load English stop words
stop_words = set(stopwords.words('english'))

# Remove stop words and punctuation
filtered_words = [
    word for word in words
    if word.lower() not in stop_words and word.isalpha()
]

# Display the result
print(filtered_words)