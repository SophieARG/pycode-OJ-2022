face = {'2': 0, 'A': 1, 'K': 2, 'Q': 3, 'J': 4, '10': 5, '9': 6, '8': 7, '7': 8, '6': 9, '5': 10, '4': 11, '3': 12}
suit = {'h': 0, 's': 1, 'd': 2, 'c': 3}

while True:
    try:
        print(' '.join(sorted(input().split(), key = lambda x: (face[x[1:]], suit[x[0]]))))
    except EOFError:
        break
