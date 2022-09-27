MAX = 200 + 2

a, b, c = map(float, input().split())
p = [[0 for i in range(MAX)] for j in range(MAX)]
x, y, xy = min(a, b+c), min(b, a+c), c
            
for i in range(1,MAX):
    p[i][0], p[0][i] = x * i, y * i

for i in range(1, MAX):
    for j in range(1, MAX):
        p[i][j] = min(x + p[i-1][j], y + p[i][j-1], xy + p[i-1][j-1])

def dis(x1, y1, x2, y2, x3, y3):
    res = p[abs(x1)][abs(y1)]
    res += p[abs(x2-x1)][abs(y2-y1)]
    res += p[abs(x3-x2)][abs(y3-y2)]
    res += p[abs(100-x3)][abs(100-y3)]
    return res

n1, x1, y1 = input().split()
n2, x2, y2 = input().split()
n3, x3, y3 = input().split()
x1, x2, x3 = int(x1), int(x2), int(x3)
y1, y2, y3 = int(y1), int(y2), int(y3)

allpath = [(dis(x1,y1,x2,y2,x3,y3), n1, n2, n3),
           (dis(x1,y1,x3,y3,x2,y2), n1, n3, n2),
           (dis(x2,y2,x1,y1,x3,y3), n2, n1, n3),
           (dis(x2,y2,x3,y3,x1,y1), n2, n3, n1),
           (dis(x3,y3,x1,y1,x2,y2), n3, n1, n2),
           (dis(x3,y3,x2,y2,x1,y1), n3, n2, n1)]

allpath.sort()
best = allpath[0]
print(' '.join(best[1:]))
print('%.2f' % best[0])
