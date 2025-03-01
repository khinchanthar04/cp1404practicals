"""
Word Occurrences
Estimate: 20 minutes
Actual:   37 minutes
"""

user_string = input("Please enter text: ")
words = user_string.lower().split()
word_counts = {}

for word in words:
    word = word.strip('.,!?;:"\'')
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

sorted_word_counts = dict(sorted(word_counts.items()))
max_word_length = max(len(word) for word in sorted_word_counts.keys())

# Print the input string
print(f"Text: {user_string}")

# Print the word counts in a sorted and aligned format
for word, count in sorted_word_counts.items():
    print(f"{word:{max_word_length}} : {count}")
