a1, a2, a3 = 0, 0, 0
n = int(input())
for i in range(n):
    b1, b2, b3 = map(int, input().split())
    a1 += b1
    a2 += b2
    a3 += b3
print(a1, a2, a3, a1 + a2 + a3)
