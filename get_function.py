counts = dict()
text = input("enter a line of text")
words = text.split()
print(words)
for word in words:
    counts[word] = counts.get('word',0)+1
print(counts)
