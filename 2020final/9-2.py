print(int(input()) - len(set(y for x, y in enumerate(map(int, input().split()), start=1) if x != y)))
