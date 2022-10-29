n = int(input())
times = []
for i in range(n):
    times.append(tuple(map(int, input().split())))
times.sort()
p1, p2 = 0, 1
best = 0
while p2 < len(times):
    best = max(best, min(times[p1][1], times[p2][1]) - times[p2][0] + 1)
    if times[p2][1] > times[p1][1]: p1 = p2
    p2 += 1
print(best)
