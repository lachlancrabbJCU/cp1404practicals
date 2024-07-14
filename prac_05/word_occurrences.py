"""
Word occurrences
Estimate: 20 minutes
Actual:   23 minutes
"""

text = input("Text: ")
words = text.split(" ")
word_to_count = {}
for word in words:
    try:
        word_to_count[word] += 1
    except KeyError:
        word_to_count[word] = 1
word_to_count = dict(sorted(word_to_count.items()))
max_word_width = max((len(word) for word in list(word_to_count.keys())))
for word, count in word_to_count.items():
    print(f"{word:{max_word_width}} : {count}")
