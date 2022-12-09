n = int(input())
c1 = input()
c2 = input()
m1 = c1.count('1')
m2 = c2.count('1')
res = -1
if m1 == m2:
    count = 0
    for char1, char2 in zip(c1, c2):
        if char1 == '1' and char2 == '0':
            count += 1
    res = count * 2
if m1 + m2 == n + 1:
    count = 0
    for char1, char2 in zip(c1, c2):
        if char1 == '1' and char2 == '1':
            count += 1
    res = count * 2 - 1 if res == -1 else min(res, count * 2 - 1)
print(res)
