from math import ceil
xs = input().split()
for num in xs:
    if num != '0':
        break
else:
    xs = ['0']
maxlx, sumlx = 0, 0
for l in map(len, xs):
    maxlx = max(maxlx, l)
    sumlx += l
ys = input().split()
for num in ys:
    if num != '0':
        break
else:
    ys = ['0']
maxly, sumly = 0, 0
for l in map(len, ys):
    maxly = max(maxly, l)
    sumly += l
if sumlx > sumly:
    print('Miao')
elif sumlx < sumly:
    print('Yan')
else:
    sx = ''.join(sorted(xs, key = lambda x: (x * ceil(maxlx / len(x)))[:maxlx], reverse = True))
    sy = ''.join(sorted(ys, key = lambda y: (y * ceil(maxly / len(y)))[:maxly], reverse = True))
    if sx > sy:
        print('Miao')
    elif sx < sy:
        print('Yan')
    else:
        print('Same')
