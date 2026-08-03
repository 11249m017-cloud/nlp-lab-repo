# Multilingual Word Analysis

import re

# Input Unicode text
text = input("Enter a sentence: ")

# Extract words using Unicode pattern
tokens = re.findall(r'\w+', text, re.UNICODE)

# Display tokens
print("Tokens:")

for token in tokens:
    print(token)