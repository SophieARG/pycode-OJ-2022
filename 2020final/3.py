x0, y0 = map(float, input().split())
x1, y1 = map(float, input().split())
v = float(input())
print('%.5f' % (pow(pow(x1 - x0, 2) + pow(y1 - y0, 2), 0.5) / v))
