x0, y0 = map(float, input().split())
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())
print('%.3f' % (abs((x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0)) / 2))
