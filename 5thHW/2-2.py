from functools import lru_cache

M, N = map(int, input().split())

@lru_cache()
def put(m=M, n=N):
    if m == 0 or n == 1: return 1
    if m < n: return put(m, m)
    return put(m - n, n) + put(m, n - 1)

print(put())
