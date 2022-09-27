m = int(input().split()[-1])
ans = input().split()
for i in range(m):
    print(sum(map(lambda x: x[0] == x[1], zip(input().split(), ans))))
