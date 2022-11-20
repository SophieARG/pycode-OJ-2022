n = int(input())
ai = input().split()
p = 0
read = set()
count = 0
while p < n:
    read.add(p)
    a = p
    while True:
        a = int(ai[a]) - 1
        if a in read: break
        read.add(a)
    while p in read:
        p += 1
    count += 1
print(count)
