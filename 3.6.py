import spacy

nlp = spacy.load("en_core_web_sm")

doc = nlp("The boys played games")

for token in doc:
    print(token.text, "->", token.lemma_, "->", token.morph)