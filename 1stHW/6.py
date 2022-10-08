a, b, c = map(float, input().split())
delta = b * b - 4 * a * c
m = 0 - b / 2 / a
n = pow(abs(delta), 0.5) / 2 / abs(a)
if delta == 0:
    print('x1=x2=%.5f' % m)
elif delta > 0:
    print('x1=%.5f;x2=%.5f' % (m + n, m - n))
else:
    print('x1=%.5f+%.5fi;x2=%.5f-%.5fi' % (m, n, m, n))
