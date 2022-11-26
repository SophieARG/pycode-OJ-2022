n = int(input())
p, c, maxc = 0, 0, 0
for num in map(int, input().split()):
    if p + 1 == num:
        c += 1
    else:
        maxc = max(maxc, c)
        c = 1
    p = num
print(max(maxc, c))
