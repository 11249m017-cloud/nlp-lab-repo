# Vocabulary Analysis

# Input document
text = input("Enter a document: ")

# Split text into words
words = text.split()

# Count total words
total_words = len(words)

# Count unique words
unique_words = len(set(words))

# Display results
print("Total Words =", total_words)
print("Unique Words =", unique_words)