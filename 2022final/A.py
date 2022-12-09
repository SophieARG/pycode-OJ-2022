from collections import deque
n, k = map(int, input().split())
a = deque(map(int, input().split()))
a.rotate(- k % n)
print(*a)
