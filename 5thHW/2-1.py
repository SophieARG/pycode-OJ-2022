from math import ceil
from functools import lru_cache

M, N = map(int, input().split())

@lru_cache()
def put(m=M, n=N, p=M):
    if m == 0: return 1
    res = 0
    for i in range(min(m, p), ceil(m / n) - 1, -1):
        res += put(m - i, n - 1, i)
    return res

print(put())


