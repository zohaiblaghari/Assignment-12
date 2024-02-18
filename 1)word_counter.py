def word_counter(sentence):
    sentence = sentence.lower()
    words = sentence.split()
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts

sentence = input("Enter a sentence:")
word_counts = word_counter(sentence)
print("Word counts:")
for word, count in word_counts.items():
    print(f"{word}:{count}")