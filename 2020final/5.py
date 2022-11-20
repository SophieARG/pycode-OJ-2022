x, y = map(int, input().split())
s = 0
while y > x:
    if y % 2 != 0 or y // 2 < x:
        y -= 1
    else:
        y = y // 2
    s += 1
print(s)
