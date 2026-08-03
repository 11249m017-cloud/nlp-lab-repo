import nltk
from nltk.corpus import stopwords

# Download stopwords dataset (only the first time)
nltk.download('stopwords')

# Get English stop words
english_stopwords = stopwords.words('english')

# Display the list of stop words
print("English Stop Words:")
print(english_stopwords)