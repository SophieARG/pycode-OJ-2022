n, m, k = map(int, input().split())
A, B = [], []
for i in range(n):
    A.append(list(map(int, input().split())))
for i in range(m):
    B.append(list(map(int, input().split())))
for i in range(n):
    line = []
    for j in range(k):
        thesum = 0
        for _ in range(m):
            thesum += A[i][_] * B[_][j]
        line.append(thesum)
    print(*line)
