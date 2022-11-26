n = int(input())
data = []
for i in range(n):
    data.append(list(map(int, input().split())))
for i in range(1, n):
    data[i][0] += data[i-1][0]
    data[i][-1] += data[i-1][-1]
    for j in range(1, i):
        data[i][j] += max(data[i-1][j-1], data[i-1][j])
print(max(data[-1]))
