word = input("Enter a word: ")

prefixes = ["un", "re", "dis", "pre", "mis", "over", "under"]

print("\nGenerated Words")

for prefix in prefixes:
    print(prefix + word)
