from collections import defaultdict

training_data = [
    [("The", "DT"), ("dog", "NN"), ("runs", "VB")],
    [("The", "DT"), ("cat", "NN"), ("eats", "VB")],
    [("A", "DT"), ("dog", "NN"), ("eats", "VB")],
    [("A", "DT"), ("cat", "NN"), ("runs", "VB")]
]

transition_counts = defaultdict(lambda: defaultdict(int))
emission_counts = defaultdict(lambda: defaultdict(int))
tag_counts = defaultdict(int)

# Count transitions, emissions, and tags
for sentence in training_data:
    previous_tag = "<START>"

    for word, tag in sentence:
        transition_counts[previous_tag][tag] += 1
        emission_counts[tag][word.lower()] += 1
        tag_counts[tag] += 1
        previous_tag = tag


def transition_probability(previous_tag, current_tag):
    total = sum(transition_counts[previous_tag].values())

    if total == 0:
        return 0

    return transition_counts[previous_tag][current_tag] / total


def emission_probability(tag, word):
    total = tag_counts[tag]

    if total == 0:
        return 0

    return emission_counts[tag][word.lower()] / total


print("Transition Probability")
print("----------------------")

print("P(DT | START) =",
      transition_probability("<START>", "DT"))

print("P(NN | DT) =",
      transition_probability("DT", "NN"))

print("P(VB | NN) =",
      transition_probability("NN", "VB"))

print("\nEmission Probability")
print("--------------------")

print("P(The | DT) =",
      emission_probability("DT", "The"))

print("P(dog | NN) =",
      emission_probability("NN", "dog"))

print("P(eats | VB) =",
      emission_probability("VB", "eats"))
