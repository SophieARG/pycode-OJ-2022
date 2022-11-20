def isSub(seq, sub):
    p1, p2 = 0, 0
    l1, l2 = len(seq), len(sub)
    while p1 < l1 and p2 < l2:
        if seq[p1] == sub[p2]:
            p2 += 1
        p1 += 1
    return p2 == l2
for i in range(int(input())):
    print('YES' if isSub(*map(str.lower, input().split())) else 'NO')
