from collections import Counter
counter = Counter(input())
for char, count in sorted(counter.items(), key = lambda x: (-x[1], x[0])):
    print(char, count)
