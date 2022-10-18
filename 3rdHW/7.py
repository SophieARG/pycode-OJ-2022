from collections import deque

n, m = map(int, input().split())
queue = deque(range(1, n + 1))
res = []
for i in range(n):
    for j in range(m - 1):
        queue.append(queue.popleft())
    res.append(str(queue.popleft()))
print(' '.join(res))
