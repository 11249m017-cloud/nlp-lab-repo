words = [
    "unhappy",
    "replay",
    "happiness",
    "teacher",
    "kindness"
]

prefixes = ["un", "re", "dis", "im"]
suffixes = ["ness", "er", "ing", "ed", "ly"]

print("PREFIX AND SUFFIX IDENTIFICATION")
print("--------------------------------")

for word in words:
    print("\nWord:", word)

    found_prefix = False
    found_suffix = False

    for prefix in prefixes:
        if word.startswith(prefix):
            print("Prefix:", prefix)
            found_prefix = True

    for suffix in suffixes:
        if word.endswith(suffix):
            print("Suffix:", suffix)
            found_suffix = True

    if not found_prefix:
        print("Prefix: None")

    if not found_suffix:
        print("Suffix: None")