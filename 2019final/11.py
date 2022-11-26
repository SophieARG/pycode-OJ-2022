m, n = map(int, input().split())
S = 0
dp = [[0 for j in range(n)] for i in range(m)]
for i in range(m):
    for j, num in enumerate(input().split()):
        if num == '0':
            dp[i][j] = dp[i][j - 1] + 1  # delicate at i = 0
            S = max(S, dp[i][j])
for i in range(1, m):
    for j in range(n):
        minv = float('inf')
        for di in range(i + 1):
            minv = min(minv, dp[i - di][j])
            S = max(S, minv * (di + 1))
            if minv * (i + 1) <= S: break
print(S)
