from collections import Counter
for i in range(int(input())):
    c1, c2 = input().split()
    print('YES' if len(c1) == len(c2) and Counter(c1) == Counter(c2) else 'NO')
