n = int(input())
root = pow(n, 0.5)
res = 0
for i in range(1, int(root) + 1):
    if n % i == 0:
        res += 2
if pow(int(root), 2) == n:
    res -= 1
print(res)
