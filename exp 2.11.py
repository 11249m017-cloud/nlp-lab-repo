import inflect

# Create inflect engine
p = inflect.engine()

# Input number
number = int(input("Enter a number: "))

# Convert number to ordinal form
print("Ordinal:", p.ordinal(number))
