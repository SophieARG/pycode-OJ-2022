x = float(input())
if x < 5:
    ans = -x + 2.5
elif x < 10:
    ans = 2 - 1.5 * (x-3) * (x-3)
else:
    ans = x / 2 - 1.5
print('%.3f' % ans)
