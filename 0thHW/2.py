n, x, y = map(int, input().split())
print(n - y//x - (0 if y%x==0 else 1))
