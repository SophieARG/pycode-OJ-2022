n = int(input())
if n <= 5:
    p = n * 2
elif n <= 10:
    p = n * 1.9
elif n <= 15:
    p = n * 1.8
elif n <= 20:
    p = n * 1.7
else:
    p = n * 1.6
print('%.2f' % p)
