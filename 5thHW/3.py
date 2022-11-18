for i in range(int(input())):
    words = {}
    for j in range(10 * int(input())):
        word, score = input().split()
        if word not in words:
            words[word] = []
        words[word].append(int(score))
    minv = float('inf')
    best = None
    for word, scores in words.items():
        v = sum(scores) / len(scores)
        if v < minv:
            minv = v
            best = word
    print(best)
