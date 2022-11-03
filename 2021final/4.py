m = int(input().split()[-1])
ans = input().split()
for i in range(m):
    print(sum(map(lambda x, y: x == y, input().split(), ans)))
