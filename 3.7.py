from lemminflect import getInflection

word = "child"

print("Noun Morphology")
print("----------------")

print("Singular :", word)
print("Plural :", getInflection(word, tag="NNS")[0])

verb = "play"

print("\nVerb Morphology")
print("----------------")

print("Base :", getInflection(verb, tag="VB")[0])
print("Past :", getInflection(verb, tag="VBD")[0])
print("Present :", getInflection(verb, tag="VBZ")[0])
print("Participle :", getInflection(verb, tag="VBG")[0])