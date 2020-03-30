
def count_e(testtext, case_sensitive=False):
    with open("testtext", "r") as f:
      text= f.read ()
    if case_sensitive:
        alphabet_set="e"
        text = original_text
    else:
        alphabet = "!e"
        text = original_text.lower()
    alphabet_set = set(alphabet)
    counts = collections.Counter(c for c in text if c in alphabet_set)

    for letter in alphabet:
        print(letter, counts[letter])
    print("total:", sum(counts.values()))

    return counts
    print(counts)