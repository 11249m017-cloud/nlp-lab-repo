
import inflect

# Create inflect engine
p = inflect.engine()

# Input word
word = input("Enter a word: ")

# Generate correct article (a/an)
print(p.a(word))