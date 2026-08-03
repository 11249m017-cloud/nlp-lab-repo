adj = input("Enter an adjective: ")

if len(adj) <= 5:
    print("Comparative:", adj + "er")
    print("Superlative:", adj + "est")

else:
    print("Comparative: more", adj)
    print("Superlative: most", adj)