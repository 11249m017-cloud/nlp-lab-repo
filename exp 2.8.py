import inflect

p = inflect.engine()

word = input("Enter a plural noun: ")

singular = p.singular_noun(word)

if singular:
    print("Singular:", singular)
else:
    print("The given word is already singular.")
