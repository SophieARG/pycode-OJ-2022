n = int(input())
count = 0
for uid in map(int, input().split()):
    for num in (2, 3, 5):
        while True:
            div, mod = divmod(uid, num)
            if div == 0 or mod != 0: break
            uid = div
    if uid == 1:
        count += 1
print(count)
