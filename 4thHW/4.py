n = int(input())
for i in range(n):
    l, s = input().split()
    lenl, lens = len(l), len(s)
    i = 0
    res = []
    while i <= lenl - lens:
        if l[i: i + lens] == s:
            res.append(str(i))
            i += lens
        else:
            i += 1
    print(' '.join(res) if res else 'no')
