n = int(input())
c = 1
for i in range(n):
    c = c * (4 * i + 2) // (i + 2)
print(c)
