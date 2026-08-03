import inflect

# Create inflect engine
p = inflect.engine()

# Input number
number = int(input("Enter a number: "))

# Convert number to words
print(p.number_to_words(number))