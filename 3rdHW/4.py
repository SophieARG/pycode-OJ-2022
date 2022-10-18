words = {}
while True:
    try:
        word = input()
        if word not in words: words[word] = 0
        words[word] += 1
    except EOFError:
        for word, count in sorted(words.items(), key = lambda x: (-x[1], x[0])):
            print(count, word)
        break
