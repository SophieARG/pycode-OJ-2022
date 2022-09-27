k, n = map(int, input().split())

s = [[0 for j in range(n+1)] for i in range(k+1)]

for i in range(3, k+1):
    s[i][1] = 1
for j in range(1, n+1):
    s[3][j] = pow(2, j) - 1
for i in range(4, k+1):
    for j in range(1, n+1):
        res = s[i-1][j]
        for r in range(1, j):
            res = min(res, 2 * s[i][j-r] + s[i-1][r])
        s[i][j] = res

print(s[k][n])
