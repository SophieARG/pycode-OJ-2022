from collections import deque
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0: break
    queue = deque(range(n, 0, -1))
    for i in range(n - 1):
        queue.rotate(m)
        queue.popleft()
    print(queue.pop())
