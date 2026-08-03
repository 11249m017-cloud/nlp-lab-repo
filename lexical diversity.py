# Lexical Diversity Calculation

# Input text
text = input("Enter a text: ")

# Split text into words
words = text.split()

# Calculate total words
total_words = len(words)

# Calculate unique words
unique_words = len(set(words))

# Calculate lexical diversity
lexical_diversity = unique_words / total_words

# Display result
print("Total Words =", total_words)
print("Unique Words =", unique_words)
print("Lexical Diversity =", round(lexical_diversity, 2))