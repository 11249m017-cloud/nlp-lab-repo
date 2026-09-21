from collections import Counter

# Training corpus
sentences = ["I like NLP", "I like Python", "I love NLP"]

# Tokenize sentences (lowercase and split into words)
tokenized_sentences = [sentence.lower().split() for sentence in sentences]

# Create vocabulary
vocabulary = set()
for sentence in tokenized_sentences:
    vocabulary.update(sentence)

V = len(vocabulary)

# Count unigrams and bigrams
unigram_counts = Counter()
bigram_counts = Counter()

for sentence in tokenized_sentences:
    for word in sentence:
        unigram_counts[word] += 1
    for i in range(len(sentence) - 1):
        bigram = (sentence[i], sentence[i + 1])
        bigram_counts[bigram] += 1


# Laplace (Add-1) smoothing function: P(w_i | w_{i-1}) = (Count(w_{i-1}, w_i) + 1) / (Count(w_{i-1}) + V)
def laplace_probability(previous_word, current_word):
    bigram_count = bigram_counts[(previous_word, current_word)]
    previous_count = unigram_counts[previous_word]
    probability = (bigram_count + 1) / (previous_count + V)
    return probability


# Execution and outputs
print("Vocabulary size (V):", V)
print("Vocabulary elements:", sorted(list(vocabulary)))

print("\nP(nlp | like):")
print(f"Calculation: (1 + 1) / (2 + {V}) = {laplace_probability('like', 'nlp'):.4f}")

print("\nP(love | like):")
print(f"Calculation: (0 + 1) / (2 + {V}) = {laplace_probability('like', 'love'):.4f}")