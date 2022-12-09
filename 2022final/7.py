*p, n = map(int, input().split())
data = [tuple(map(int, input().split())) for i in range(n)]

def choose(p, i=0, l=()):
    if min(p) >= 0 and i < n:
        if p == (0, 0, 0, 0):
            print(*l)
            return True
        else:
            bool1 = choose(tuple(x - y for x, y in zip(p, data[i])), i, l + (i + 1,))
            bool2 = choose(p, i + 1, l)
            return bool1 or bool2
    return False

if not choose(p):
    print("NO")
