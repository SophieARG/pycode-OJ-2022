words = set()
while True:
    try:
        words.add(input())
    except EOFError:
        print(len(words))
        break
