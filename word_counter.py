with open('timestamp.txt', 'r') as file:
    content = file.read()
words = content.split()
word_count = {}
for word in words:
    word = word.lower()
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
for word, count in word_count.items():
    print(f'{word}: {count}')
