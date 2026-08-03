root=input("Enter the root word")
prefixes=["un","re","dis","pre","mis"]
suffixes=["ing", "ed", "er", "ly","ness"]
print("\n Generated words using prefixes")
for p in prefixes:
    print(p+root)
print("\nGenerated words using suffixes\n")
for s in suffixes:
    print(root +s)