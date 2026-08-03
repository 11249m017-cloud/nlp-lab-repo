# Word Length Analysis

# Input sentence
text = input("Enter a sentence: ")

# Split sentence into words
words = text.split()

# Find word lengths
word_lengths = [len(word) for word in words]

# Find longest and shortest words
longest_word = max(words, key=len)
shortest_word = min(words, key=len)

# Calculate average word length
average_length = sum(word_lengths) // len(words)

# Display results
print("Longest Word:", longest_word)
print("Shortest Word:", shortest_word)
print("Average Length:", average_length)
