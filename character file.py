# Character Analysis

# Input text
text = input("Enter a text: ")

# Initialize counters
vowels = 0
consonants = 0
digits = 0
spaces = 0
special_characters = 0

# Define vowels
vowel_list = "aeiouAEIOU"

# Analyze each character
for char in text:
    if char.isalpha():
        if char in vowel_list:
            vowels += 1
        else:
            consonants += 1
    elif char.isdigit():
        digits += 1
    elif char.isspace():
        spaces += 1
    else:
        special_characters += 1

# Display results
print("Vowels =", vowels)
print("Consonants =", consonants)
print("Letters =", vowels + consonants)
print("Digits =", digits)
print("Spaces =", spaces)
print("Special Characters =", special_characters)