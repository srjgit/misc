page = """the first line
        second one here
        the final one's here..."""

unique_words = ()
for line in page:
    for word in line.split():
        unique_words.append(word)

print set(unique_words)
