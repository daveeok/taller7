paragraph = "python es versatil y python es legible y practico"
words = paragraph.split()
print(words)

counter = {}

for word in words:
    if word in counter:
        counter[word] += 1
    else:
        counter[word] = 1

print(counter)